import re
import logging
from PyQt5 import QtCore, QtWidgets, Qt
from ui.Ui_fillwindow import Ui_fillWindow


def fill_all_fields(self):
    logging.debug('check_functions.py - fill_all_fields')
    all_texts = 1
    all_lists = 1
    all_dates = 1
    
    # preparing labels -> all black
    labels = self.findChildren(QtWidgets.QLabel)
    for label in labels:
        label.setStyleSheet("color: black")
    for i in range(self.tabWidget.count()):
        self.tabWidget.tabBar().setTabTextColor(i, Qt.QColor(0,0,0))
    
    # check : all Text Areas
    for sublist in self.mandatory_line_edit_list:
        if not sublist[0].isHidden():
            if sublist[0].text() == "":
                all_texts = 0
                sublist[1].setStyleSheet("color: rgb(200,0,0)")
                self.tabWidget.tabBar().setTabTextColor(sublist[3], Qt.QColor(200,0,0))
            else:
                if not check_field_correct_line(sublist[0], sublist[2]):
                    all_texts = 0
                    sublist[1].setStyleSheet("color: rgb(0,0,200)")
                    if self.tabWidget.tabBar().tabTextColor(sublist[3]).red() != 200:
                        self.tabWidget.tabBar().setTabTextColor(sublist[3], Qt.QColor(0,0,200))    
    
    # check: all Comboboxes
    for sublist in self.mandatory_combobox_list:
        if not sublist[0].isHidden():
            if sublist[0].currentText() == "Make a choice...":
                all_lists = 0
                sublist[1].setStyleSheet("color: rgb(200,0,0)")
                self.tabWidget.tabBar().setTabTextColor(sublist[2], Qt.QColor(200,0,0))
    
    # check : all dateboxes
    current_date = QtCore.QDate.currentDate().toString(Qt.Qt.ISODate)
    for sublist in self.mandatory_datebox_list:
        if not sublist[0].isHidden():
            date = sublist[0].date().toString(Qt.Qt.ISODate)
            if date > current_date:
                all_dates = 0
                sublist[1].setStyleSheet("color: rgb(0,0,200)")
                if self.tabWidget.tabBar().tabTextColor(sublist[2]).red() != 200:
                    self.tabWidget.tabBar().setTabTextColor(sublist[2], Qt.QColor(0,0,200))  
        
    
    if all_texts == 0 or all_lists == 0 or all_dates == 0:
        self.fillInfo = True
        self.fillWindow = MyFill()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.fillWindow.geometry().getRect()
        self.fillWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.fillWindow.setMinimumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
        self.fillWindow.setMaximumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
        self.fillWindow.exec_()
        return self.fillWindow.cancel
    else:
        return False    
    
    
def check_field_correct_line(widget, field_format):
    logging.debug('check_functions.py - check_field_correct_line - field_format ' + str(field_format))
    result = True
    if field_format == "text":
        try:
            float(widget.text())
            result = False
        except ValueError:
            result = True
    elif field_format == "float":
        try:
            float(widget.text())
            result = True
        except ValueError:
            result = False
    elif field_format == "email":
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', widget.text()):
            result = False
    return result
    
    
class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('check_functions.py - MyFill')
        self.setupUi(self)
        self.fw_okButton.clicked.connect(self.closeWindow)
        self.fw_cancelButton.clicked.connect(self.cancelWindow)
        self.cancel = False
        self.fw_cancelButton.setFocus(True)

    def cancelWindow(self):
        self.cancel = True
        self.close()

    def closeWindow(self):
        self.close()    
        