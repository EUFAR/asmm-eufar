# -*- coding: utf-8 -*-

import webbrowser
import datetime
import os, sys
from PyQt4 import QtGui, QtCore
#from PyQt4.QtCore import QDate
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QString
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QInputDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QTextEdit
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QCursor
from Ui_mainwindow import Ui_MainWindow
from Ui_aboutwindow import Ui_aboutWindow
from Ui_aboutstandard import Ui_aboutStandard
from Ui_logwindow import Ui_Changelog
from _version import _version
from _version import _xml_version
from functions.asmm_xml import create_asmm_xml
from functions.asmm_xml import read_asmm_xml
from functions.asmm_pdf import create_asmm_pdf
from functions.netcdf_lite import NetCdf
from functions import button_functions
from functions.button_functions import add_clicked
from functions.button_functions import button_clicked
from functions.sql_functions import objectsInit


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        objectsInit(self)
        all_check_boxes = self.findChildren(QCheckBox)
        for check_box in all_check_boxes:
            QObject.connect(check_box, SIGNAL("stateChanged(int)"), self.set_modified)
        all_text_edits = self.findChildren(QTextEdit)
        for widget in all_text_edits:
            QObject.connect(widget, SIGNAL("textChanged()"), self.set_modified) 
        all_line_edits = self.findChildren(QLineEdit)
        for widget in all_line_edits:
            QObject.connect(widget, SIGNAL("textChanged(QString)"), self.set_modified)   
        QObject.connect(self.dateLine, SIGNAL("dateChanged(QDate)"), self.set_modified)
        all_info_boxes = self.findChildren(QToolButton)
        for widget in all_info_boxes:
            QObject.connect(widget, SIGNAL("clicked()"), self.infoButton_clicked)
        all_add_boxes = self.findChildren(QPushButton)
        for widget in all_add_boxes:
            QObject.connect(widget, SIGNAL("clicked()"), self.addButton_clicked)
        self.make_window_title()


    @pyqtSignature("")
    def on_groundAddButton_clicked(self):
        self.addListItem("Add Ground Site", "Ground Site Name:", self.groundListWidget, self.ground_site_list)


    @pyqtSignature("")
    def on_groundRemoveButton_clicked(self):
        self.removeListItem(self.groundListWidget, self.ground_site_list)


    @pyqtSignature("")
    def on_armAddButton_clicked(self):
        self.addListItem("Add ARM Site", "ARM Site Name:", self.armListWidget, self.arm_site_list)


    @pyqtSignature("")
    def on_armRemoveButton_clicked(self):
        self.removeListItem(self.armListWidget, self.arm_site_list)


    @pyqtSignature("")
    def on_armMobileAddButton_clicked(self):
        self.addListItem("Add ARM Mobile Site", "ARM Mobile Site Name:", self.armMobileListWidget, self.arm_mobile_list)


    @pyqtSignature("")
    def on_armMobileRemoveButton_clicked(self):
        self.removeListItem(self.armMobileListWidget, self.arm_mobile_list)


    @pyqtSignature("")
    def on_vesselAddButton_clicked(self):
        self.addListItem("Add Research Vessel", "Research Vessel Name:", self.vesselListWidget, self.research_vessel_list)


    @pyqtSignature("")
    def on_vesselRemoveButton_clicked(self):
        self.removeListItem(self.vesselListWidget, self.research_vessel_list)


    @pyqtSignature("")
    def on_generateXMLButton_clicked(self):
        self.save_document()


    @pyqtSignature("")
    def on_exitButton_clicked(self):
        self.close()


    @pyqtSignature("")
    def on_actionNew_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box()
            if result == QMessageBox.Save:
                self.save_document()
		self.reset_all_fields()
            elif result == QMessageBox.Discard:
                self.reset_all_fields()
            else:
                return
        self.reset_all_fields()


    @pyqtSignature("")
    def on_actionSave_triggered(self):
        self.save_document()


    @pyqtSignature("")
    def on_actionSave_As_triggered(self):
	self.save_document(save_as=True)


    @pyqtSignature("")
    def on_actionPrint_triggered(self):
        self.out_file_name_pdf = self.get_file_name_pdf()
        if not self.out_file_name_pdf:
	    return
	if '.pdf' not in self.out_file_name_pdf:
	    self.out_file_name_pdf = self.out_file_name_pdf + '.pdf'
	create_asmm_pdf(self, self.out_file_name_pdf)


    @pyqtSignature("")
    def on_actionOpen_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box()
            if result == QMessageBox.Save:
                self.save_document()
	    elif result == QMessageBox.Cancel:
		return
        self.open_file()


    @pyqtSignature("")
    def on_actionExit_triggered(self):
        self.close()


    @pyqtSignature("")
    def on_actionEUFAR_N7SP_triggered(self):
        webbrowser.open('http://www.eufar.net/')


    @pyqtSignature("")
    def on_actionASMM_CreatorAbout_triggered(self):
        aboutText = "<html><head/><body><p align=justify>The ASMM Creator V%s was developed by EUFAR using Python and PyQT. XML files generated by this version conform to V%s of the ASMM XML standard. The opensource PDF plugin used for PDF report generation is provided and owned by Reportlab (<a href=http://www.reportlab.com/opensource>http://www.reportlab.com/opensource</a>).</p><p>For more information, or to submit a bug report, please contact <a href='mailto:xxxxxxxxxxxxxxxxx'>xxxxxxxxxxxxxxxxxxxxx</a></p><p>The latest version and source code of the ASMM creator can be found at <a href=https://github.com/eufarn7sp/asmm-eufar>https://github.com/ eufarn7sp/asmm-eufar</a></p></body></html>" % (_version, _xml_version)
        self.aboutWindow = MyAbout(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(452, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()

    
    @pyqtSignature("")
    def on_actionASMM_XML_Standard_triggered(self):
        aboutText = "<html><head/><body><p align=justify>The Airborne Science Mission Metadata (ASMM) standard is intended to unify descriptions of science research flights. This common description will allow users of the airborne science data to search past datasets for specific meteorological conditions, geographical regions, cloud-types encountered, particles sampled, and other parameters not evident from the data itself.<br> <br> For more information, please read the following document: <a href=https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>ASMM - XML Implementation Rules.pdf</a></p></body></html>"
        self.aboutWindow = MyStandard(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(452, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()
 

    @pyqtSignature("")
    def on_actionChangelog_triggered(self):
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.logWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.logWindow.setGeometry(x2, y2, w2, h2)
        self.logWindow.exec_()


    @pyqtSignature("")
    def on_readBoundingBoxButton_clicked(self):
        lat_min = None
        lat_max = None
        lon_min = None
        lon_max = None
        alt_min = None
        alt_max = None
        filename = QFileDialog.getOpenFileName(self,'Open associated NetCDF','','NetCDF files (*.nc *.cdf);;All Files (*.*)')
	if not filename:
		return
        f = NetCdf(str(filename))
        var_list = f.get_variable_list()
        var_list.sort()
        try:
            lat_min = f.get_attribute_value("geospatial_lat_min")
            lat_max = f.get_attribute_value("geospatial_lat_max")
        except KeyError:
            [var_name, ok] = QInputDialog.getItem(self, "Latitude Variable Name", "ERROR: Latitude values not found. Please enter latitude variable name.", var_list, current=0, editable=False)
            if var_name and ok:
                lat_values = f.read_variable(str(var_name))
                lat_min = min(lat_values[lat_values != 0])
                lat_max = max(lat_values[lat_values != 0])
        try:
            lon_min = f.get_attribute_value("geospatial_lon_min")
            lon_max = f.get_attribute_value("geospatial_lon_max")
        except KeyError:
            [var_name, ok] = QInputDialog.getItem(self, "Longitude Variable Name", "ERROR: Longitude values not found. Please select longitude variable name.", var_list, current=0, editable=False)
            if var_name and ok:
                lon_values = f.read_variable(str(var_name))
                lon_min = min(lon_values[lon_values != 0])
                lon_max = max(lon_values[lon_values != 0])
        try:
            alt_min = f.get_attribute_value("geospatial_vertical_min")
            alt_max = f.get_attribute_value("geospatial_vertical_max")
        except KeyError:
            [var_name, ok] = QInputDialog.getItem(self, "Altitude Variable Name", "ERROR: Altitude values not found. Please enter altitude variable name.", var_list, current=0, editable=False)
            if var_name and ok:
                alt_values = f.read_variable(str(var_name))
                alt_min = min(alt_values[alt_values != 0])
                alt_max = max(alt_values[alt_values != 0])
        self.westBoundLongitudeLine.setText(str(lon_min))
        self.eastBoundLongitudeLine.setText(str(lon_max))
        self.northBoundLatitudeLine.setText(str(lat_max))
        self.southBoundLatitudeLine.setText(str(lat_min))
        self.minAltitudeLine.setText(str(alt_min))
        self.maxAltitudeLine.setText(str(alt_max))


    def closeEvent(self, event):
        if self.modified:
            result = self.make_onsave_msg_box()
            if result == QMessageBox.Save:
                self.save_document()
                print 'closing ASMM Metadata Creator V{0} ...'.format(_version)
                event.accept()
            elif result == QMessageBox.Discard:
                print 'closing ASMM Metadata Creator V{0} ...'.format(_version)
                event.accept()
            else:
                event.ignore()
        else:
            print 'closing ASMM Metadata Creator V{0} ...'.format(_version)
            self.close()


    def make_window_title(self):
        if self.saved:
            title_string = "ASMM Creator V{0} - ".format(_version) + self.out_file_name
        else:
            title_string = "ASMM Creator V{0} - unsaved".format(_version)
        if self.modified:
            title_string += ' - modified'
        self.setWindowTitle(title_string)

    def set_modified(self):
        if not self.modified:
            self.modified = True
            self.make_window_title()


    def save_document(self, save_as=False):
        if not self.out_file_name or save_as:
            self.out_file_name = self.get_file_name()
            if not self.out_file_name:
                return
            if '.xml' not in self.out_file_name:
                self.out_file_name = self.out_file_name + '.xml'
        create_asmm_xml(self, self.out_file_name)
        self.make_window_title()


    def get_file_name(self):
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('xml')
        out_file_name = unicode(file_dialog.getSaveFileName(self, "Save XML File", filter='XML Files (*.xml);;Text Files (*.txt)'))
        return out_file_name


    def get_file_name_pdf(self):
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('pdf')
        out_file_name_pdf = unicode(file_dialog.getSaveFileName(self, "Save PDF File", filter='PDF Files (*.pdf)'))
        return out_file_name_pdf


    def reset_all_fields(self):
        all_check_boxes = self.findChildren(QCheckBox)
        for check_box in all_check_boxes:
            check_box.setCheckState(False)
        all_text_edits = self.findChildren(QTextEdit)
        for widget in all_text_edits:
            widget.clear()
        all_line_edits = self.findChildren(QLineEdit)
        for widget in all_line_edits:
            widget.clear()
        all_list_widgets = self.findChildren(QListWidget)
        for widget in all_list_widgets:
            widget.clear()
        objectsInit(self)
        for i in reversed(range(self.gridLayout_5.count())):
            self.gridLayout_5.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_8.count())):
            self.gridLayout_8.itemAt(i).widget().deleteLater()    
        for i in reversed(range(self.gridLayout_9.count())):
            self.gridLayout_9.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_10.count())):
            self.gridLayout_10.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_11.count())):
            self.gridLayout_11.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_13.count())):
            self.gridLayout_13.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_14.count())):
            self.gridLayout_14.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_15.count())):
            self.gridLayout_15.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_25.count())):
            self.gridLayout_25.itemAt(i).widget().deleteLater()
        self.make_window_title()


    def make_onsave_msg_box(self):
        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setIcon(QMessageBox.Warning)
        screen_center = QtGui.QDesktopWidget().availableGeometry().center()
        msgBox.move(screen_center)
        result = msgBox.exec_()
        return result


    def open_file(self):
        (out_file_name, filter) = QFileDialog.getOpenFileNameAndFilter(self, "Open XML File", filter="XML Files (*.xml)")
        out_file_name = unicode(out_file_name)
        if out_file_name:
            read_asmm_xml(self, out_file_name)
            self.saved = True
            self.modified = False
            self.out_file_name = out_file_name
            self.make_window_title()


    def addListItem(self, title, label, listWidget, item_list):
        (new_item, response) = QInputDialog.getText(self, title, label, text=QString(),)
        if new_item and response:
            self.modified = True
            item_list.append(new_item)
            listWidget.addItem(new_item)
            self.make_window_title()


    def removeListItem(self, listWidget, item_list):
        selected_line = listWidget.currentRow()
        if selected_line >= 0:
            selected_item = listWidget.currentItem()
            item_list.remove(unicode(selected_item.text()))
            listWidget.takeItem(selected_line)
            self.modified = True
            self.make_window_title()


    def infoButton_clicked(self):
        if "infoButton" in self.sender().objectName():
            button_clicked(self)
            
            
    def addButton_clicked(self):
        if "addButton" in self.sender().objectName():
              add_clicked(self)


class MyAbout(QtGui.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()
        
        
class MyLog(QtGui.QDialog, Ui_Changelog):
    def __init__(self):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.log_txBrower.setPlainText(open(self.progPath + "/" + "Documentation/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()
 
 
class MyStandard(QtGui.QDialog, Ui_aboutStandard):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close() 
 

        