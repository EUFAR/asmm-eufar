# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDate
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QString
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QInputDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QRadioButton
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QCursor
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_addcheckbox import Ui_Addcheckbox


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


def add_clicked(self):
    senderName = self.sender().objectName()[:2]     
    x = QCursor.pos().x()
    y = QCursor.pos().y()
    x1, y1, w1, h1 = self.geometry().getRect()
    x = x - 150
    y = y + 50
    self.infoWindow = MyAdd()
    self.infoWindow.setMinimumSize(QtCore.QSize(300, self.infoWindow.sizeHint().height()))
    self.infoWindow.setMaximumSize(QtCore.QSize(300, self.infoWindow.sizeHint().height()))
    self.infoWindow.setGeometry(x, y, 300, self.infoWindow.sizeHint().height())
    if self.infoWindow.exec_():
        self.modified = True
        ckText = self.infoWindow.ck_inputLine.text()
        self.make_window_title()
        font1 = QtGui.QFont()
        font1.setFamily(_fromUtf8(self.progPath + "/font/DroidSansFallbackFull.ttf"))
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8(self.progPath + "/font/DroidSansFallbackFull.ttf"))
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        tmp = QtGui.QCheckBox()
        tmp.setFont(font2)
        tmp.setObjectName(_fromUtf8(ckText))
        tmp.setText(ckText)
        tmp.setStyleSheet(""".QCheckBox {margin-left: 10px;}""")
        labelTitle = QtGui.QLabel()
        labelTitle.setFont(font1)
        labelTitle.setObjectName(_fromUtf8("labelTitle"))
        labelTitle.setText("User-defined:")      
        if senderName == "sa":
            if self.sa_y ==0 & self.sa_x == 0:
                self.gridLayout_5.addWidget(labelTitle, self.sa_y, self.sa_x)
                self.sa_y += 1
            self.sa_ck_list.append(tmp)
            self.gridLayout_5.addWidget(self.sa_ck_list[self.sa_ckL], self.sa_y, self.sa_x)
            self.sa_x += 1
            if self.sa_x > 3:
                self.sa_x = 0
                self.sa_y += 1;
            self.sa_ckL += 1
        elif senderName == "gr":
            if self.gr_y ==0 & self.gr_x == 0:
                self.gridLayout_8.addWidget(labelTitle, self.gr_y, self.gr_x)
                self.gr_y += 1
            self.gr_ck_list.append(tmp)
            self.gridLayout_8.addWidget(self.gr_ck_list[self.gr_ckL], self.gr_y, self.gr_x)
            self.gr_x += 1
            if self.gr_x > 3:
                self.gr_x = 0
                self.gr_y += 1;
            self.gr_ckL += 1
        elif senderName == "af":
            if self.af_y ==0 & self.af_x == 0:
                self.gridLayout_9.addWidget(labelTitle, self.af_y, self.af_x)
                self.af_y += 1
            self.af_ck_list.append(tmp)
            self.gridLayout_9.addWidget(self.af_ck_list[self.af_ckL], self.af_y, self.af_x)
            self.af_x += 1
            if self.af_x > 3:
                self.af_x = 0
                self.af_y += 1;
            self.af_ckL += 1
        elif senderName == "ct":
            if self.ct_y ==0 & self.ct_x == 0:
                self.gridLayout_10.addWidget(labelTitle, self.ct_y, self.ct_x)
                self.ct_y += 1
            self.ct_ck_list.append(tmp)
            self.gridLayout_10.addWidget(self.ct_ck_list[self.ct_ckL], self.ct_y, self.ct_x)
            self.ct_x += 1
            if self.ct_x > 3:
                self.ct_x = 0
                self.ct_y += 1;
            self.ct_ckL += 1
        elif senderName == "ps":
            if self.ps_y ==0 & self.ps_x == 0:
                self.gridLayout_11.addWidget(labelTitle, self.ps_y, self.ps_x)
                self.ps_y += 1
            self.ps_ck_list.append(tmp)
            self.gridLayout_11.addWidget(self.ps_ck_list[self.ps_ckL], self.ps_y, self.ps_x)
            self.ps_x += 1
            if self.ps_x > 3:
                self.ps_x = 0
                self.ps_y += 1;
            self.ps_ckL += 1
        elif senderName == "so":
            if self.so_y ==0 & self.so_x == 0:
                self.gridLayout_13.addWidget(labelTitle, self.so_y, self.so_x)
                self.so_y += 1
            self.so_ck_list.append(tmp)
            self.gridLayout_13.addWidget(self.so_ck_list[self.so_ckL], self.so_y, self.so_x)
            self.so_x += 1
            if self.so_x > 3:
                self.so_x = 0
                self.so_y += 1;
            self.so_ckL += 1
        elif senderName == "ar":
            if self.ar_y ==0 & self.ar_x == 0:
                self.gridLayout_14.addWidget(labelTitle, self.ar_y, self.ar_x)
                self.ar_y += 1
            self.ar_ck_list.append(tmp)
            self.gridLayout_14.addWidget(self.ar_ck_list[self.ar_ckL], self.ar_y, self.ar_x)
            self.ar_x += 1
            if self.ar_x > 3:
                self.ar_x = 0
                self.ar_y += 1;
            self.ar_ckL += 1
        elif senderName == "fm":
            if self.fm_y ==0 & self.fm_x == 0:
                self.gridLayout_15.addWidget(labelTitle, self.fm_y, self.fm_x)
                self.fm_y += 1
            self.fm_ck_list.append(tmp)
            self.gridLayout_15.addWidget(self.fm_ck_list[self.fm_ckL], self.fm_y, self.fm_x)
            self.fm_x += 1
            if self.fm_x > 3:
                self.fm_x = 0
                self.fm_y += 1;
            self.fm_ckL += 1
        elif senderName == "sc":
            if self.sc_y ==0 & self.sc_x == 0:
                self.gridLayout_25.addWidget(labelTitle, self.sc_y, self.sc_x)
                self.sc_y += 1
            self.sc_ck_list.append(tmp)
            self.gridLayout_25.addWidget(self.sc_ck_list[self.sc_ckL], self.sc_y, self.sc_x)
            self.sc_x += 1
            if self.sc_x > 3:
                self.sc_x = 0
                self.sc_y += 1;
            self.sc_ckL += 1         
    else:
        return

def add_read(self, parent, text):
    self.modified = True
    self.make_window_title()
    font1 = QtGui.QFont()
    font1.setFamily(_fromUtf8(self.progPath + "/font/DroidSansFallbackFull.ttf"))
    font1.setPointSize(10)
    font1.setBold(True)
    font1.setUnderline(True)
    font1.setWeight(75)
    font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font2 = QtGui.QFont()
    font2.setFamily(_fromUtf8(self.progPath + "/font/DroidSansFallbackFull.ttf"))
    font2.setPointSize(10)
    font2.setBold(False)
    font2.setWeight(50)
    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
    tmp = QtGui.QCheckBox()
    tmp.setFont(font2)
    tmp.setObjectName(_fromUtf8(text))
    tmp.setText(text)
    tmp.setStyleSheet(""".QCheckBox {margin-left: 10px;}""")
    tmp.setChecked(True)
    labelTitle = QtGui.QLabel()
    labelTitle.setFont(font1)
    labelTitle.setObjectName(_fromUtf8("labelTitle"))
    labelTitle.setText("User-defined:")      
    if parent == "SA":
        if self.sa_y ==0 & self.sa_x == 0:
            self.gridLayout_5.addWidget(labelTitle, self.sa_y, self.sa_x)
            self.sa_y += 1
        self.sa_ck_list.append(tmp)
        self.gridLayout_5.addWidget(self.sa_ck_list[self.sa_ckL], self.sa_y, self.sa_x)
        self.sa_x += 1
        if self.sa_x > 3:
            self.sa_x = 0
            self.sa_y += 1;
        self.sa_ckL += 1
    elif parent == "GR":
        if self.gr_y ==0 & self.gr_x == 0:
            self.gridLayout_8.addWidget(labelTitle, self.gr_y, self.gr_x)
            self.gr_y += 1
        self.gr_ck_list.append(tmp)
        self.gridLayout_8.addWidget(self.gr_ck_list[self.gr_ckL], self.gr_y, self.gr_x)
        self.gr_x += 1
        if self.gr_x > 3:
            self.gr_x = 0
            self.gr_y += 1;
        self.gr_ckL += 1
    elif parent == "AF":
        if self.af_y ==0 & self.af_x == 0:
            self.gridLayout_9.addWidget(labelTitle, self.af_y, self.af_x)
            self.af_y += 1
        self.af_ck_list.append(tmp)
        self.gridLayout_9.addWidget(self.af_ck_list[self.af_ckL], self.af_y, self.af_x)
        self.af_x += 1
        if self.af_x > 3:
            self.af_x = 0
            self.af_y += 1;
        self.af_ckL += 1
    elif parent == "CT":
        if self.ct_y ==0 & self.ct_x == 0:
            self.gridLayout_10.addWidget(labelTitle, self.ct_y, self.ct_x)
            self.ct_y += 1
        self.ct_ck_list.append(tmp)
        self.gridLayout_10.addWidget(self.ct_ck_list[self.ct_ckL], self.ct_y, self.ct_x)
        self.ct_x += 1
        if self.ct_x > 3:
            self.ct_x = 0
            self.ct_y += 1;
        self.ct_ckL += 1
    elif parent == "PS":
        if self.ps_y ==0 & self.ps_x == 0:
            self.gridLayout_11.addWidget(labelTitle, self.ps_y, self.ps_x)
            self.ps_y += 1
        self.ps_ck_list.append(tmp)
        self.gridLayout_11.addWidget(self.ps_ck_list[self.ps_ckL], self.ps_y, self.ps_x)
        self.ps_x += 1
        if self.ps_x > 3:
            self.ps_x = 0
            self.ps_y += 1;
        self.ps_ckL += 1
    elif parent == "SO":
        if self.so_y ==0 & self.so_x == 0:
            self.gridLayout_13.addWidget(labelTitle, self.so_y, self.so_x)
            self.so_y += 1
        self.so_ck_list.append(tmp)
        self.gridLayout_13.addWidget(self.so_ck_list[self.so_ckL], self.so_y, self.so_x)
        self.so_x += 1
        if self.so_x > 3:
            self.so_x = 0
            self.so_y += 1;
        self.so_ckL += 1
    elif parent == "AR":
        if self.ar_y ==0 & self.ar_x == 0:
            self.gridLayout_14.addWidget(labelTitle, self.ar_y, self.ar_x)
            self.ar_y += 1
        self.ar_ck_list.append(tmp)
        self.gridLayout_14.addWidget(self.ar_ck_list[self.ar_ckL], self.ar_y, self.ar_x)
        self.ar_x += 1
        if self.ar_x > 3:
            self.ar_x = 0
            self.ar_y += 1;
        self.ar_ckL += 1
    elif parent == "FM":
        if self.fm_y ==0 & self.fm_x == 0:
            self.gridLayout_15.addWidget(labelTitle, self.fm_y, self.fm_x)
            self.fm_y += 1
        self.fm_ck_list.append(tmp)
        self.gridLayout_15.addWidget(self.fm_ck_list[self.fm_ckL], self.fm_y, self.fm_x)
        self.fm_x += 1
        if self.fm_x > 3:
            self.fm_x = 0
            self.fm_y += 1;
        self.fm_ckL += 1
    elif parent == "SC":
        if self.sc_y ==0 & self.sc_x == 0:
            self.gridLayout_25.addWidget(labelTitle, self.sc_y, self.sc_x)
            self.sc_y += 1
        self.sc_ck_list.append(tmp)
        self.gridLayout_25.addWidget(self.sc_ck_list[self.sc_ckL], self.sc_y, self.sc_x)
        self.sc_x += 1
        if self.sc_x > 3:
            self.sc_x = 0
            self.sc_y += 1;
        self.sc_ckL += 1 
    else:
        return



            

def button_clicked(self):
    x = QCursor.pos().x()
    y = QCursor.pos().y()
    x1, y1, w1, h1 = self.geometry().getRect()
    textInfo =  "Use this button to add a new checkbox. Each activated checkbox is then saved in the xml file with the code 'xx_User'. All unactivated checkboxes will not be saved and will be lost."
    x = x - 175
    y = y + 50
    self.infoWindow = MyInfo(textInfo)
    self.infoWindow.setMinimumSize(QtCore.QSize(350, self.infoWindow.sizeHint().height()))
    self.infoWindow.setMaximumSize(QtCore.QSize(350, self.infoWindow.sizeHint().height()))
    self.infoWindow.setGeometry(x, y, 350, self.infoWindow.sizeHint().height())
    self.infoWindow.exec_()


class MyAdd(QtGui.QDialog, Ui_Addcheckbox):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.ck_cancelButton.clicked.connect(self.closeWindow)
        self.ck_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()
        
        

class MyInfo(QtGui.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()
 