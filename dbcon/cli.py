from argparse import RawTextHelpFormatter
import importlib
import importlib.machinery
import argh
import argh.dispatching
import yaml
from dbcon.util import echo
import os.path

@argh.arg('dbms', help='DBMS type. postgres or mysql')
def status(dbms):
    module = importlib.import_module('dbcon.dbms.' + dbms)
    module.status()


def parse_config(file, format=None):
    if format == 'django':
        settings = importlib.machinery.SourceFileLoader('settings', file).load_module()
        db = settings.DATABASES['default']
        return {
            'dbms': parse_django_database_engine(db['ENGINE']),
            'database': db['NAME'],
            'user': db['USER'],
            'password': db['PASSWORD'],
        }

    if os.path.splitext(file)[1] in ['yml', 'json']:
        return yaml.load(open(file))

    raise Exception("configuration file format error: %s" % file)


def parse_django_database_engine(engine):
    if 'postgres' in engine:
        return 'postgres'

    if 'mysql' in engine:
        return 'mysql'

    raise Exception("%s is not supported" % engine)


@argh.arg('file', help='Database configuration file.')
@argh.arg('--format', help='configuration file format. yaml|json|django.')
def configure(file, format='yaml'):
    '''
    configure database as given configuration file. YAML, JSON or Django settings.py are supported.
    Try stub command to see sample file.
    '''
    execute('configure', parse_config(file, format))


def drop(file, format='yaml'):
    '''
    drop database and user as given configuration file
    '''
    execute('drop', parse_config(file, format))


def stub():
    echo('''Save this as yaml file.
=====================
dbms: postgres
database: myapp
user: myuser
password: mypassword
======================
''')


def execute(command, config):
    try:
        module = importlib.import_module('dbcon.dbms.' + config['dbms'])
        getattr(module, command)(**config)
    except:
        echo('not supported config: %s' % config)


parser = argh.ArghParser()
parser.add_commands([status, configure, stub, drop])
# TODO add --echo option


def main():
    parser.dispatch()


if __name__ == '__main__':
    main()