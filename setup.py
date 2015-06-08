#!/usr/bin/env python
"""Airborne Science Mission Metadata creator.

The ASMM (Airborne Science Mission Metadata) Creator is a Python and PyQt based
GUI utility intended to generate and display XML files conforming to the ASMM standard.
The purpose of these files is to provide a standard method to describe the various
parameters and observations of airborne atmospheric science missions, which can then
be used for dataset discovery after the data has been archived. 

This utility is maintained by EUFAR.
"""
from ui._version import _version


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = """\
Development Status :: 4 - Beta
Environment :: X11 Applications :: Qt
Environment :: Win32 (MS Windows)
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: BSD License
Natural Language :: English
Programming Language :: Python
Topic :: Scientific/Engineering :: Atmospheric Science
Topic :: Text Processing :: Markup :: XML
"""

doclines = __doc__.split('\n')


setup(name='asmm_creator',
      version=_version,
      description=doclines[0],
      long_description='\n'.join(doclines[2:]),
      author='EUFAR',
      author_email='bureau@eufar.net',
      maintainer='Olivier Henry',
      maintainer_email='olivier.henry@meteo.fr',
      url='http://www.eufar.net',
      download_url='http://code.google.com/p/asmm-creator',
      license='New BSD License',
      keywords=['airbornescience', 'xml', 'eufar', 'science', 'metadata'],
      packages=['ui','fonts','functions'],
      classifiers=filter(None, classifiers.split("\n")),
      requires=['PyQt','reportlab (>=3.1.31)'],
      install_requires=['PyQt','reportlab (>=3.1.31)']
      )
