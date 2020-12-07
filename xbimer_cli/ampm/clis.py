from os import path
from sys import path as sysPath

 
here = path.abspath(path.dirname(__file__))
parentDir=path.dirname(here)
sysPath.append(parentDir)


import click
import signup
import _utils_ as _utils

@click.group()
def main():
    pass

@click.command()
def version():
    click.echo("xbimer-cli "+_utils.VERSION)

main.add_command(signup.main,"signup")
main.add_command(version,"version")

if __name__ == "__main__":
    main()

