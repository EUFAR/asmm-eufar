# asmm-eufar

A detailed changelog can be found in the Documentation directory.
Current version: 1.0.1

Overview

This project intends to develop a tool for creating, modifying and viewing Airborne Science Mission Metadata (ASMM) XML files. Executables for Windows and Linux, once they are available, will be provided in the EXE directory. The related documentation, including a changelog and an XML schema file, is located in the Documentation directory. 

Motivation

Within airborne atmospheric science, mission reports provide valuable details about research flights that are not evident from the instrument data itself. These reports can include environmental details such as types of clouds encountered, surfaces overflown and synoptic features, or mission details such as overall scientific aims, flight manoeuvres undertaken and supporting surface based observations, among many other things. Currently, mission reports take the form of handwritten or electronic notes, thus the quality and content varies greatly between authors, making the reports less useful for filtering or searching of specific flight details in the months and years after the flight.

This project - Airborne Science Mission Metadata (ASMM) - was motivated by the need to create a standard set of mission reports, aiding in classification and searches of data sets based on flight phenomena, mission parameters or other criteria. To meet this goal, an XML format has been developed to store the mission report data in a standard manner, and an easy-to-use graphical user interface has been developed to facilitate creation and display of the standard XML files. This project contains the source code and executables for the ASMM creator as well as documentation describing the ASMM XML schema.

Libraries

This software needs the following libraries to allow proper operation:
  - Python 2.7.10
  - PyQt4 4.11.4+ -> http://www.riverbankcomputing.co.uk/software/pyqt/download
  - netCDF4 for python 1.1.9+ -> https://pypi.python.org/pypi/netCDF4
  - Reportlab PDF Toolkit 3.2.8+ -> https://bitbucket.org/rptlab/reportlab
  - Pillow 2.9.0+ -> https://pypi.python.org/pypi/Pillow/2.9.0
