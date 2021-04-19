from os.path import join, dirname
from shutil import copytree

ARCHICAD_SUPPORT = [22, 23]


def assetsCopy(srcName, destDir):
    here = dirname(__file__)
    srcHome = join(here, 'assets', srcName)
    copytree(srcHome, destDir)
