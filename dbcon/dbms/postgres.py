from dbcon import util


def psql(query, options=''):
    command = 'psql postgres %s -c "%s"' % (options, query)
    return util.run(command)


def status():
    '''
    check postgres installed
    check postgres running
    list database
    '''
    util.echo(psql("\\l").std_out)
    util.echo(psql("\\du").std_out)


def configure(dbms, database, user, password):
    util.echo('Configure: %s %s %s %s' % (dbms, database, user, password))

    if user_exists(user):
        util.echo('User %s already exists.' % user)
    else:
        create_user(user, password)
        util.echo('Created user %s.' % user)

    if database_exists(database):
        util.echo('Database %s already exists.' % database)
    else:
        util.echo('Created database %s.' % database)
        create_database(database, user)


def drop(dbms, database, user, password):
    util.echo('Drop: %s %s %s %s' % (dbms, database, user, password))
    drop_database(database)
    drop_user(user)


def reconfigure(dbms, database, user, password):
    drop(dbms, database, user, password)
    configure(dbms, database, user, password)


def user_exists(name):
    """
    Check if a PostgreSQL user exists.
    """

    res = psql("SELECT COUNT(*) FROM pg_user WHERE usename = '%(name)s';" % locals(), '-t -A')
    return (res.std_out.strip() == "1")


def create_user(name, password, superuser=False, createdb=False,
                createrole=False, inherit=True, login=True,
                connection_limit=None, encrypted_password=False):
    options = [
        'SUPERUSER' if superuser else 'NOSUPERUSER',
        'CREATEDB' if createdb else 'NOCREATEDB',
        'CREATEROLE' if createrole else 'NOCREATEROLE',
        'INHERIT' if inherit else 'NOINHERIT',
        'LOGIN' if login else 'NOLOGIN',
    ]
    if connection_limit is not None:
        options.append('CONNECTION LIMIT %d' % connection_limit)
    password_type = 'ENCRYPTED' if encrypted_password else 'UNENCRYPTED'
    options.append("%s PASSWORD '%s'" % (password_type, password))
    options = ' '.join(options)
    psql("CREATE USER %(name)s %(options)s;" % locals())


def drop_user(name):
    psql("DROP USER %(name)s;" % locals())


def database_exists(name):
    """
    Check if a PostgreSQL database exists.
    """
    return psql('\\l %s' % name, '-t -A').std_out


def create_database(name, owner, template='template0', encoding='UTF8',
                    locale='en_US.UTF-8'):
    util.run('''createdb --owner %(owner)s --template %(template)s \
                  --encoding=%(encoding)s --lc-ctype=%(locale)s \
                  --lc-collate=%(locale)s %(name)s''' % locals())


def drop_database(name):
    util.run('''dropdb %(name)s''' % locals())



