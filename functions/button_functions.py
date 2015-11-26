# -*- coding: utf-8 -*-

import os, urllib
import tempfile
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget, QLabel
from PyQt4.QtGui import QCursor
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_imagewindow import Ui_ImageWindow
from ui.Ui_addcheckbox import Ui_Addcheckbox
from PIL import Image
from PyQt4.QtCore import SIGNAL


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
    self.infoWindow = MyAdd()
    self.infoWindow.setMinimumSize(QtCore.QSize(300, self.infoWindow.sizeHint().height()))
    self.infoWindow.setMaximumSize(QtCore.QSize(300, self.infoWindow.sizeHint().height()))
    self.infoWindow.setGeometry(QCursor.pos().x() - 150, QCursor.pos().y() + 50, 300, self.infoWindow.
                                sizeHint().height())
    if self.infoWindow.exec_():
        font1 = QtGui.QFont()
        font1.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        tmp = QtGui.QCheckBox()
        tmp.setFont(font2)
        tmp.setObjectName(_fromUtf8(self.infoWindow.ck_inputLine.text()))
        tmp.setText(self.infoWindow.ck_inputLine.text())
        tmp.setStyleSheet(""".QCheckBox {margin-left: 10px;}""")
        labelTitle = QtGui.QLabel()
        labelTitle.setFont(font1)
        labelTitle.setObjectName(_fromUtf8("labelTitle"))
        labelTitle.setText("User-defined:")    
        
        if self.ck_xy_dict.get(str(self.sender().objectName()[:2]))[0] == 0 and self.ck_xy_dict.get(
                str(self.sender().objectName()[:2]))[1] == 0:
            self.ck_lay_dict.get(str(self.sender().objectName()[:2])).addWidget(labelTitle, self.
                ck_xy_dict.get(str(self.sender().objectName()[:2]))[1], self.ck_xy_dict.get(str(self.
                sender().objectName()[:2]))[0])
            self.ck_xy_dict.get(str(self.sender().objectName()[:2]))[1] += 1
        self.ck_list_dict.get(str(self.sender().objectName()[:2])).append(tmp)    
        self.ck_lay_dict.get(str(self.sender().objectName()[:2])).addWidget(tmp, self.ck_xy_dict.get
            (str(self.sender().objectName()[:2]))[1], self.ck_xy_dict.get(str(self.sender().
            objectName()[:2]))[0]) 
        self.ck_xy_dict.get(str(self.sender().objectName()[:2]))[0] += 1
        if self.ck_xy_dict.get(str(self.sender().objectName()[:2]))[0] > 3:
            self.ck_xy_dict.get(str(self.sender().objectName()[:2]))[0] = 0
            self.ck_xy_dict.get(str(self.sender().objectName()[:2]))[1] += 1
        self.modified = True
        self.make_window_title()
    else:
        return

def add_read(self, parent, text):
    font1 = QtGui.QFont()
    font1.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
    font1.setPointSize(10)
    font1.setBold(True)
    font1.setUnderline(True)
    font1.setWeight(75)
    font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font2 = QtGui.QFont()
    font2.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
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
    
    if self.ck_xy_dict.get(str(parent).lower())[0] == 0 and self.ck_xy_dict.get(str(parent).lower())[1] == 0:
        self.ck_lay_dict.get(str(parent).lower()).addWidget(labelTitle, self.ck_xy_dict.get(str(parent).
            lower())[1], self.ck_xy_dict.get(str(parent).lower())[0])
        self.ck_xy_dict.get(str(parent).lower())[1] += 1
    self.ck_list_dict.get(str(parent).lower()).append(tmp)    
    self.ck_lay_dict.get(str(parent).lower()).addWidget(tmp, self.ck_xy_dict.get(str(parent).lower
        ())[1], self.ck_xy_dict.get(str(parent).lower())[0]) 
    self.ck_xy_dict.get(str(parent).lower())[0] += 1
    if self.ck_xy_dict.get(str(parent).lower())[0] > 3:
        self.ck_xy_dict.get(str(parent).lower())[0] = 0
        self.ck_xy_dict.get(str(parent).lower())[1] += 1


def button_clicked(self):
    x = QCursor.pos().x()
    y = QCursor.pos().y()
    textInfo = ("<p align=justify>Use this button to add a new checkbox. Each activated checkbox is "
    + "then saved in the XML file with the code <b>xx_User</b>.</p><p align=center style='color:#C80"
    + "000'><b>All non-activated checkboxes will not be saved and will be lost.</b></p><p align=jus"
    + "tify>As the PDF report generator is limited to 12 checkboxes per section, you cannot create "
    + "more than 12 checkboxes per section in ASMM Creator Online.</p>")
    x = x - 175
    y = y + 50
    self.infoWindow = MyInfo(textInfo)
    self.infoWindow.setMinimumSize(QtCore.QSize(350, self.infoWindow.sizeHint().height()))
    self.infoWindow.setMaximumSize(QtCore.QSize(350, self.infoWindow.sizeHint().height()))
    self.infoWindow.setGeometry(x, y, 350, self.infoWindow.sizeHint().height())
    self.infoWindow.exec_()
 

def add_image(self, filename):
    if "http://" in filename or "www." in filename:
        temp_name = next(tempfile._get_candidate_names())
        imagename = self.dirpath + "/" + temp_name + ".jpg"
        urllib.urlretrieve(str(filename), imagename)
        tmp0 = Image.open(imagename)
        filename = imagename
    else:
        tmp0 = Image.open(filename)
    w1, h1 = tmp0.size
    tmp0 = tmp0.transpose(Image.FLIP_TOP_BOTTOM)
    filename2 = self.dirpath + "/flip_" + os.path.basename(filename)
    tmp0.save(filename2)
    ratio = float(w1) / float(h1)
    if ratio > 1:
        w2 = 300
        h2 = float(w2) / float(ratio)
    else:
        h2 = 300
        w2 = float(h2) * float(ratio)
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
    font.setPointSize(10)
    font.setBold(True)
    font.setUnderline(True)
    font.setWeight(75)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    tmp2 = QtGui.QHBoxLayout()
    self.im_horlay.append(tmp2)
    self.im_horlay[self.im_number].setObjectName(_fromUtf8("im_horlay" + str(self.im_number)))
    tmp3 = ExtendedQLabel()
    self.im_label.append(tmp3)
    self.im_label[self.im_number].setObjectName(_fromUtf8("im_label" + str(self.im_number)))
    self.im_label[self.im_number].setMinimumSize(QtCore.QSize(w2, h2))
    self.im_label[self.im_number].setMaximumSize(QtCore.QSize(w2, h2))
    self.im_label[self.im_number].setPixmap(QtGui.QPixmap(filename))
    self.im_label[self.im_number].setScaledContents(True)
    self.im_horlay[self.im_number].addWidget(self.im_label[self.im_number])
    spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    self.im_horlay[self.im_number].addItem(spacerItem1)
    tmp4 = QtGui.QVBoxLayout()
    self.im_verlay.append(tmp4)
    self.im_verlay[self.im_number].setObjectName(_fromUtf8("im_verlay" + str(self.im_number)))
    self.im_horlay[self.im_number].addLayout(self.im_verlay[self.im_number])
    spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    self.im_verlay[self.im_number].addItem(spacerItem4)
    tmp5 = QtGui.QLabel()
    self.im_caption.append(tmp5)
    self.im_caption[self.im_number].setObjectName(_fromUtf8("im_caption" + str(self.im_number)))
    self.im_caption[self.im_number].setMinimumSize(QtCore.QSize(100, 27))
    self.im_caption[self.im_number].setMaximumSize(QtCore.QSize(100, 27))
    self.im_caption[self.im_number].setFont(font)
    self.im_caption[self.im_number].setText("Caption:")
    self.im_verlay[self.im_number].addWidget(self.im_caption[self.im_number])
    tmp6 = QtGui.QLineEdit()
    self.im_textbox.append(tmp6)
    self.im_textbox[self.im_number].setMinimumSize(QtCore.QSize(300, 27))
    self.im_textbox[self.im_number].setMaximumSize(QtCore.QSize(300, 27))
    self.im_textbox[self.im_number].setFrame(False)
    self.im_textbox[self.im_number].setObjectName(_fromUtf8("im_textbox" + str(self.im_number)))
    self.im_verlay[self.im_number].addWidget(self.im_textbox[self.im_number])
    spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    self.im_verlay[self.im_number].addItem(spacerItem5)
    spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    self.im_horlay[self.im_number].addItem(spacerItem2)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/del_icon.png")), QtGui.QIcon.
                    Normal, QtGui.QIcon.Off)
    tmp7 = QtGui.QToolButton()
    self.im_del.append(tmp7)
    self.im_del[self.im_number].setMinimumSize(QtCore.QSize(27, 27))
    self.im_del[self.im_number].setMaximumSize(QtCore.QSize(27, 27))
    self.im_del[self.im_number].setText(_fromUtf8(""))
    self.im_del[self.im_number].setIcon(icon1)
    self.im_del[self.im_number].setIconSize(QtCore.QSize(27, 27))
    self.im_del[self.im_number].setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    self.im_del[self.im_number].setAutoRaise(True)
    self.im_del[self.im_number].setObjectName(_fromUtf8("im_del" + str(self.im_number)))
    self.im_horlay[self.im_number].addWidget(self.im_del[self.im_number])
    spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    self.im_horlay[self.im_number].addItem(spacerItem3)
    self.verticalLayout_52.addLayout(self.im_horlay[self.im_number])
    self.im_number += 1
    self.images_pdf_path.append(filename2)
    self.images_display_path.append(filename)


def delete_image(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[-1:])
    self.im_horlay[index].deleteLater()
    self.im_horlay.pop(index)
    self.im_verlay[index].deleteLater()
    self.im_verlay.pop(index)
    self.im_label[index].deleteLater()
    self.im_label.pop(index)
    self.im_caption[index].deleteLater()
    self.im_caption.pop(index)
    self.im_textbox[index].deleteLater()
    self.im_textbox.pop(index)
    self.im_del[index].deleteLater()
    self.im_del.pop(index)
    self.images_pdf_path.pop(index)
    self.images_display_path.pop(index)
    self.im_number -= 1
    if len(self.im_horlay) > 0:
        i = 0
        for i in range(0, len(self.im_horlay)):
            self.im_horlay[i].setObjectName(_fromUtf8("im_horlay" + str(i)))
            self.im_verlay[i].setObjectName(_fromUtf8("im_verlay" + str(i)))
            self.im_label[i].setObjectName(_fromUtf8("im_label" + str(i)))
            self.im_caption[i].setObjectName(_fromUtf8("im_caption" + str(i)))
            self.im_textbox[i].setObjectName(_fromUtf8("im_textbox" + str(i)))
            self.im_del[i].setObjectName(_fromUtf8("im_del" + str(i)))


def display_image(self):
    index = int(self.sender().objectName()[-1:])
    tmp0 = Image.open(self.images_display_path[index])
    filename = self.images_display_path[index] 
    w1, h1 = tmp0.size
    tmp0 = tmp0.transpose(Image.FLIP_TOP_BOTTOM)
    ratio = float(w1) / float(h1)
    if ratio > 1:
        w2 = 800
        h2 = float(w2) / float(ratio)
    else:
        h2 = 600
        w2 = float(h2) * float(ratio)
    pos_x = float(QtGui.QDesktopWidget().screenGeometry().width()) / 2 - (float(w2) + 30) / 2
    pos_y = float(QtGui.QDesktopWidget().screenGeometry().height()) / 2 - (float(h2) + 75) / 2
    self.imageWindow = MyImage(filename, w2, h2)
    self.imageWindow.setMinimumSize(QtCore.QSize(w2 + 30, h2 + 75))
    self.imageWindow.setMaximumSize(QtCore.QSize(w2 + 30, h2 + 75))
    self.imageWindow.setGeometry(pos_x, pos_y, w2 + 30, h2 + 75)
    self.imageWindow.exec_()


class MyAdd(QtGui.QDialog, Ui_Addcheckbox):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
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
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()


class MyImage(QtGui.QDialog, Ui_ImageWindow):
    def __init__(self, imagePath, w2, h2):
        QWidget.__init__(self)
        self.setupUi(self)
        self.label.setPixmap(QtGui.QPixmap(imagePath))
        self.label.setScaledContents(True)
        self.label.setMinimumSize(QtCore.QSize(w2, h2))
        self.label.setMaximumSize(QtCore.QSize(w2, h2))
        self.pushButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()


class ExtendedQLabel(QLabel):
    def __init(self, parent):
        QLabel.__init__(self, parent)
 
    def mouseReleaseEvent(self, ev):
        self.emit(SIGNAL('clicked()'))