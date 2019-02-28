import os

from setuptools import setup


LICENSE = 'MIT'
AUTHOR = "HerveMignot"
EMAIL = "HerveMignot@github.com"
URL = "http://github.com/HerveMignot/switch_magic"
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Framework :: IPython',
    'Framework :: Jupyter',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Education',
    'Topic :: Scientific/Engineering',
]


# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='switch_magic',
      version='0.1.0',
      description='Magic command to switch cell execution or other magic commands',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords='switch devops production magic command IPython Jupyter Jupyterlab',
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      license=LICENSE,
      packages=['switch_magic'],
      classifiers=CLASSIFIERS,
      install_requires=[
          ],
      include_package_date=False,
      zip_safe=False
      )
