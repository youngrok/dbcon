import envoy
from dbcon import env


def echo(message):
    print('[dbcon] %s' % message)


def run(command):
    if env.get('echo', False):
        print(command)
    return envoy.run(command)
