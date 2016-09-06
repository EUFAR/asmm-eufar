# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtCore import QDate
from ui.Ui_fillwindow import Ui_fillWindow
import os


def fill_all_fields(self):
    self.fillInfo = False
    self.incompleteElements = []
    self.incorrectElements = []
    incompleteElements = 0
    incorrectElements = 0
    writeElements = ""
    all_lines = 1
    all_lists = 1
    
    # preparing labels -> all black
    labels = self.findChildren(QLabel)
    for label in labels:
        label.setStyleSheet("color: black")
           
    # check: all QLine Edit in Tab1 and Tab2
    all_line_edits = self.tabWidgetPage1.findChildren(QLineEdit) + self.tabWidgetPage2.findChildren(QLineEdit)
    for widget in all_line_edits:
        text = widget.text()
        if not text:
            if widget.objectName() != "newAircraft_ln" and widget.objectName() != "newOperator_ln":
                all_lines = 0
                linked_labels = self.findChildren(QLabel, widget.objectName()[:-2] + "lb")
                if linked_labels:
                    linked_labels[0].setStyleSheet("color: rgb(200,0,0)")
                self.incompleteElements.append(widget.objectName())
    
    # check: location 
    if self.location_cb.currentText() == 'Make a choice...':
        self.incompleteElements.append("location_cb")
        self.location_lb.setStyleSheet("color: rgb(200,0,0)")
        all_lists = 0
    if self.detailList.currentText() == 'Make a choice...':
        self.incompleteElements.append("detailList")
        self.location_lb.setStyleSheet("color: rgb(200,0,0)")
        all_lists = 0
    
    # check: operator/aircraft
    if self.aircraft_cb.currentText() == 'Make a choice...' or self.aircraft_cb.currentText() == '':
        self.incompleteElements.append("aircraft_cb")
        self.aircraft_lb.setStyleSheet("color: rgb(200,0,0)")
        all_lists = 0
    if self.operator_cb.currentText() == 'Make a choice...':
        self.incompleteElements.append("operator_cb")
        self.operator_lb.setStyleSheet("color: rgb(200,0,0)")
        all_lists = 0
    elif self.operator_cb.currentText() == 'Other...':
        if self.newOperator_ln.text() == "":
            self.incompleteElements.append("newOperator_ln")
            self.operator_lb.setStyleSheet("color: rgb(200,0,0)")
            all_lines = 0
        if self.newAircraft_ln.text() == "":
            self.incompleteElements.append("newAircraft_ln")
            self.aircraft_lb.setStyleSheet("color: rgb(200,0,0)")
            all_lines = 0
                
    # check: contact role
    if self.contact_cb.currentText() == 'Make a choice...':
        self.incompleteElements.append("contact_cb")
        self.contact_lb.setStyleSheet("color: rgb(200,0,0)")
        all_lists = 0
    
    # preparing report
    if all_lines == 0 or all_lists == 0:  
        fillElements = []
        for name in self.incompleteElements:
            for sublist in self.check_information:
                if sublist[1] == name:
                    fillElements.append([sublist[0], sublist[3], sublist[2]])
        fillElements = sorted(fillElements, key=lambda element: element[0])
        writeElements = r"<font color=#C80000><b><u>Incomplete fields<\u></b></font>"
        item_bf = 0
        i = 0
        for item in fillElements:
            if item[1] == item_bf:
                writeElements = writeElements + '<li>' + item[2] + '</li>'
            else:
                if i != 0:
                    writeElements = writeElements + "</ul></blockquote>"
                writeElements = writeElements + '<blockquote>In "' + item[1] + '", check:<ul><li>' + item[2] + '</li>'
                item_bf = item[1]
            i += 1
        writeElements = writeElements + "</blockquote><br>"
        incompleteElements = 1
        
    
    if incompleteElements == 1 or incorrectElements == 1:
        self.fillInfo = True
        self.fillWindow = MyFill(writeElements)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.fillWindow.geometry().getRect()  # @UnusedVariable
        self.fillWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.fillWindow.setMinimumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
        self.fillWindow.setMaximumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
        self.fillWindow.exec_()
        return self.fillWindow.cancel
    else:
        return False    
    
    
class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self, fillElements):
        QWidget.__init__(self)
        self.setupUi(self)
        self.fw_okButton.clicked.connect(self.closeWindow)
        self.fw_detailButton.clicked.connect(self.detailElements_show)
        self.fw_cancelButton.clicked.connect(self.cancelWindow)
        self.incompleteElements = fillElements
        self.cancel = False
        self.fw_cancelButton.setFocus(True)

    def detailElements_show(self):
        self.fw_detailButton.setText("Hide details")
        self.fw_detailButton.clicked.disconnect(self.detailElements_show)
        self.fw_detailButton.clicked.connect(self.detailElements_hide)
        x1, y1, self.w, self.h = self.geometry().getRect()  # @UnusedVariable
        if os.name == "nt":
            self.h1 = 470
            self.h2 = self.h1 - 236
        else:
            self.h1 = 400
            self.h2 = self.h1 - 186
        self.setMinimumHeight(self.h1+20)
        self.setMaximumHeight(self.h1+20)
        self.textBrowser = QtWidgets.QTextBrowser()
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setMinimumHeight(self.h2)
        self.textBrowser.setMaximumHeight(self.h2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.textBrowser.setText(self.incompleteElements)

    def detailElements_hide(self):
        self.fw_detailButton.setText("Show details")
        self.fw_detailButton.clicked.disconnect(self.detailElements_hide)
        self.fw_detailButton.clicked.connect(self.detailElements_show)
        self.textBrowser.clear()
        self.textBrowser.deleteLater()
        self.verticalLayout.removeWidget(self.textBrowser)
        self.setMinimumHeight(self.h)
        self.setMaximumHeight(self.h)

    def cancelWindow(self):
        self.cancel = True
        self.close()

    def closeWindow(self):
        self.close()    