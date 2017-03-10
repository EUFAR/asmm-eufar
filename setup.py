#!/usr/bin/env python
"""Airborne Science Mission Metadata creator.

The ASMM (Airborne Science Mission Metadata) Creator is a Python and PyQt based
GUI utility intended to generate and display XML files conforming to the ASMM standard.
The purpose of these files is to provide a standard method to describe the various
parameters and observations of airborne atmospheric science missions, which can then
be used for dataset discovery after the data has been archived. 

This utility is maintained by EUFAR.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: X11 Applications :: Qt
Environment :: Win32 (MS Windows)
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: BSD License
Natural Language :: English
Programming Language :: Python :: 3.5
Topic :: Scientific/Engineering :: Atmospheric Science
Topic :: Text Processing :: Markup :: XML
"""

doclines = __doc__.split('\n')


setup(name='asmm',
      version='1.2.1',
      description=doclines[0],
      long_description='\n'.join(doclines[2:]),
      author='EUFAR',
      author_email='bureau@eufar.net',
      maintainer='Olivier Henry',
      maintainer_email='olivier.henry@meteo.fr',
      url='http://www.eufar.net',
      download_url='https://github.com/eufarn7sp/asmm-eufar',
      license='New BSD License',
      keywords=['airbornescience', 'xml', 'eufar', 'science', 'metadata'],
      packages=['ui','fonts','functions','icons', 'Documentation'],
      classifiers=filter(None, classifiers.split("\n")),
      requires=['PyQt5 (>=5.6)','reportlab (>=3.3.9)','netCDF4 (>=1.2.4)', 'Pillow (>=3.2)'],
      install_requires=['PyQt5 >= 5.6','reportlab >= 3.3.9','netCDF4 >= 1.2.4', 'Pillow >= 3.2']
      )
