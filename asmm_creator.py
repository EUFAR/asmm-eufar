'''
Created on Mar 6, 2012
Modified on Sep 1, 2014

@author: freer, henry
'''
import netCDF4 # pyinstaller modification
import numpy # pyinstaller modification
from PyQt4 import QtCore, QtGui
from ui.mainwindow import MainWindow
from ui._version import _version

def launch_asmm_creator():
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    print 'launching ASMM Metadata Creator V{0} ...'.format(_version)
    launch_asmm_creator()
