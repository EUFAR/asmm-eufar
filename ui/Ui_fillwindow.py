# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fillwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fillWindow(object):
    def setupUi(self, fillWindow):
        fillWindow.setObjectName("fillWindow")
        fillWindow.resize(460, 280)
        fillWindow.setMinimumSize(QtCore.QSize(460, 200))
        fillWindow.setMaximumSize(QtCore.QSize(460, 280))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        fillWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/warning_icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fillWindow.setWindowIcon(icon)
        fillWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(fillWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fw_label_2 = QtWidgets.QLabel(fillWindow)
        self.fw_label_2.setMinimumSize(QtCore.QSize(55, 55))
        self.fw_label_2.setMaximumSize(QtCore.QSize(55, 55))
        self.fw_label_2.setText("")
        self.fw_label_2.setPixmap(QtGui.QPixmap("icons/warning_icon2.png"))
        self.fw_label_2.setScaledContents(True)
        self.fw_label_2.setObjectName("fw_label_2")
        self.verticalLayout_2.addWidget(self.fw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fw_label_1 = QtWidgets.QLabel(fillWindow)
        self.fw_label_1.setMinimumSize(QtCore.QSize(341, 120))
        self.fw_label_1.setMaximumSize(QtCore.QSize(341, 200))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fw_label_1.setFont(font)
        self.fw_label_1.setWordWrap(True)
        self.fw_label_1.setObjectName("fw_label_1")
        self.horizontalLayout.addWidget(self.fw_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.fw_okButton = QtWidgets.QToolButton(fillWindow)
        self.fw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.fw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_okButton.setFont(font)
        self.fw_okButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.fw_okButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.fw_okButton.setObjectName("fw_okButton")
        self.horizontalLayout_2.addWidget(self.fw_okButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.fw_cancelButton = QtWidgets.QToolButton(fillWindow)
        self.fw_cancelButton.setMinimumSize(QtCore.QSize(93, 27))
        self.fw_cancelButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_cancelButton.setFont(font)
        self.fw_cancelButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.fw_cancelButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.fw_cancelButton.setObjectName("fw_cancelButton")
        self.horizontalLayout_2.addWidget(self.fw_cancelButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.fw_detailButton = QtWidgets.QToolButton(fillWindow)
        self.fw_detailButton.setMinimumSize(QtCore.QSize(120, 27))
        self.fw_detailButton.setMaximumSize(QtCore.QSize(140, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_detailButton.setFont(font)
        self.fw_detailButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.fw_detailButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.fw_detailButton.setObjectName("fw_detailButton")
        self.horizontalLayout_2.addWidget(self.fw_detailButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(fillWindow)
        QtCore.QMetaObject.connectSlotsByName(fillWindow)

    def retranslateUi(self, fillWindow):
        _translate = QtCore.QCoreApplication.translate
        fillWindow.setWindowTitle(_translate("fillWindow", "Warning"))
        self.fw_label_1.setText(_translate("fillWindow", "<html><head/><body><p align=\"justify\">All mandatory fields have not been filled in, or have been incorrectly filled in. You can save your file if you want to complete/correct it later. All fields which have not been completely filled in are indicated in <span style=\" font-weight:600; color:#c80000;\">red</span>, and in <span style=\" font-weight:600; color:#0000c8;\">blue</span> for those incorrectly filled in (see Details to have a complete list). <span style=\" font-weight:600;\">Do not use an incomplete/incorrect xml file for storage and/or sql queries.</span></p></body></html>"))
        self.fw_okButton.setText(_translate("fillWindow", "Save"))
        self.fw_cancelButton.setText(_translate("fillWindow", "Cancel"))
        self.fw_detailButton.setText(_translate("fillWindow", "Show details"))
