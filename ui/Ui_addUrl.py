# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_AddURL(object):
    def setupUi(self, Ui_AddURL):
        Ui_AddURL.setObjectName("Ui_AddURL")
        Ui_AddURL.resize(296, 179)
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Ui_AddURL.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Ui_AddURL)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Ui_AddURL)
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.ck_inputLine = QtWidgets.QLineEdit(Ui_AddURL)
        self.ck_inputLine.setMinimumSize(QtCore.QSize(275, 27))
        self.ck_inputLine.setMaximumSize(QtCore.QSize(275, 27))
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ck_inputLine.setFont(font)
        self.ck_inputLine.setFrame(False)
        self.ck_inputLine.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(255, 255, 255);\n"
"}")
        self.ck_inputLine.setObjectName("ck_inputLine")
        self.verticalLayout.addWidget(self.ck_inputLine)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ck_submitButton = QtWidgets.QPushButton(Ui_AddURL)
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ck_submitButton.setFont(font)
        self.ck_submitButton.setObjectName("ck_submitButton")
        self.horizontalLayout.addWidget(self.ck_submitButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ck_cancelButton = QtWidgets.QPushButton(Ui_AddURL)
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ck_cancelButton.setFont(font)
        self.ck_cancelButton.setObjectName("ck_cancelButton")
        self.horizontalLayout.addWidget(self.ck_cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Ui_AddURL)
        QtCore.QMetaObject.connectSlotsByName(Ui_AddURL)

    def retranslateUi(self, Ui_AddURL):
        Ui_AddURL.setWindowTitle(_translate("Ui_AddURL", "Add an Image", None))
        self.label.setText(_translate("Ui_AddURL", "Please, enter the URL of the image. Depending on the size of the image, the downloading may take some time.", None))
        self.ck_submitButton.setText(_translate("Ui_AddURL", "Submit", None))
        self.ck_cancelButton.setText(_translate("Ui_AddURL", "Cancel", None))

