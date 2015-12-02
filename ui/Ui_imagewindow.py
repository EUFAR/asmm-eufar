# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagewindow.ui'
#
# Created: Tue Sep 15 09:14:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImageWindow(object):
    def setupUi(self, Ui_ImageWindow):
        Ui_ImageWindow.setObjectName(_fromUtf8("Ui_ImageWindow"))
        Ui_ImageWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Ui_ImageWindow.setFont(font)
        Ui_ImageWindow.setWindowTitle(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui_ImageWindow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Ui_ImageWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtGui.QLabel(Ui_ImageWindow)
        self.label.setMinimumSize(QtCore.QSize(750, 520))
        self.label.setMaximumSize(QtCore.QSize(750, 520))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton = QtGui.QPushButton(Ui_ImageWindow)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Ui_ImageWindow)
        QtCore.QMetaObject.connectSlotsByName(Ui_ImageWindow)

    def retranslateUi(self, Ui_ImageWindow):
        Ui_ImageWindow.setWindowTitle(_translate("Ui_ImageWindow", "Zoom", None))
        self.label.setText(_translate("Ui_ImageWindow", "image", None))
        self.pushButton.setText(_translate("Ui_ImageWindow", "Ok", None))

