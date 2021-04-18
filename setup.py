from setuptools import setup, find_packages
from io import open
from os import path
from xbimer_cli import version

here = path.abspath(path.dirname(__file__))

# get the dependencies
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [
    x.strip() for x in all_reqs if ('git+' not in x) and (
        not x.startswith('#')) and (not x.startswith('-'))
]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' in x]

with open(path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()

setup(name='xbimer-cli',
      version=version.CURRENT_VERSION,
      description='archicad mini program command line interface',
      long_description=long_description,
      keywords='archicad, xbimer, xbimer-cli',
      author='beanjs',
      author_email='502554248@qq.com',
      url='https://github.com/xbimer/xbimer-cli.git',
      license='MIT',
      packages=['xbimer_cli'],
      include_package_data=True,
      install_requires=install_requires,
      dependency_links=dependency_links,
      entry_points={'console_scripts': [
          'xbimer = xbimer_cli.clis:main',
      ]},
      classifiers=[
          'Programming Language :: Python :: 3.7',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: '
          'Libraries :: Application Frameworks',
      ],
      python_requires=">=3.7.5")
