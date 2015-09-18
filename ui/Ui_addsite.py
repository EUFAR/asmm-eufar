# -*- coding: utf-8 -*-

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

class Ui_Addsite(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(296, 179)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "Droid Sans Fallback"))
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Form.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "Droid Sans Fallback"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.ck_inputLine = QtGui.QLineEdit(Form)
        self.ck_inputLine.setMinimumSize(QtCore.QSize(275, 27))
        self.ck_inputLine.setMaximumSize(QtCore.QSize(275, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "Droid Sans Fallback"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ck_inputLine.setFont(font)
        self.ck_inputLine.setFrame(False)
        self.ck_inputLine.setObjectName(_fromUtf8("ck_inputLine"))
        self.verticalLayout.addWidget(self.ck_inputLine)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ck_submitButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "Droid Sans Fallback"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ck_submitButton.setFont(font)
        self.ck_submitButton.setObjectName(_fromUtf8("ck_submitButton"))
        self.horizontalLayout.addWidget(self.ck_submitButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ck_cancelButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "Droid Sans Fallback"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ck_cancelButton.setFont(font)
        self.ck_cancelButton.setObjectName(_fromUtf8("ck_cancelButton"))
        self.horizontalLayout.addWidget(self.ck_cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Add a new Site", None))
        self.label.setText(_translate("Form", "Please, enter a name for the new site", None))
        self.ck_submitButton.setText(_translate("Form", "Submit", None))
        self.ck_cancelButton.setText(_translate("Form", "Cancel", None))

