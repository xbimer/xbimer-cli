from os import mkdir, unlink
from os.path import expanduser, join, exists
from click import secho

usrHome = expanduser('~')
xirHome = join(usrHome, '.xbimer-xir')
xirFile = join(xirHome, '.cli')


def setToken(token):
    if not exists(xirHome):
        mkdir(xirHome)

    with open(xirFile, 'w') as f:
        f.write(token)
        f.close()


def getToken():

    if not exists(xirFile):
        secho('Error: No tokens available!!', fg='red')
        return None

    with open(xirFile) as f:
        token = f.read()
        f.close()

    return token


def delToken():
    if exists(xirFile):
        unlink(xirFile)
