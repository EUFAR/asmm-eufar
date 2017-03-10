# -*- coding: utf-8 -*-

import webbrowser
import tempfile
import shutil
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QWidget
from ui.Ui_mainwindow import Ui_MainWindow
from ui.Ui_aboutwindow import Ui_aboutWindow
from ui.Ui_aboutstandard import Ui_aboutStandard
from ui.Ui_logwindow import Ui_Changelog
from ui.Ui_presavewindow import Ui_presaveWindow
from ui.Ui_addsite import Ui_Addsite
from ui.Ui_addUrl import Ui_AddURL
from ui._version import _asmm_version
from ui._version import _xml_version
from ui._version import _py_version
from ui._version import _report_version
from ui._version import _qt_version
from ui._version import _eclipse_version
from functions.asmm_xml import create_asmm_xml
from functions.asmm_xml import read_asmm_xml
from functions.asmm_pdf import create_asmm_pdf
from functions.netcdf_lite import NetCdf
from functions.button_functions import add_clicked
from functions.button_functions import button_clicked
from functions.button_functions import add_image
from functions.button_functions import delete_image
from functions.button_functions import display_image
from functions.sql_functions import objectsInit
from functions.check_functions import fill_all_fields


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        objectsInit(self)
        self.dirpath = tempfile.mkdtemp()
        all_check_boxes = self.findChildren(QCheckBox)
        for check_box in all_check_boxes:
            check_box.stateChanged.connect(lambda: self.set_modified())
        all_text_edits = self.findChildren(QTextEdit)
        for widget in all_text_edits:
            widget.textChanged.connect(lambda: self.set_modified())
        all_line_edits = self.findChildren(QLineEdit)
        for widget in all_line_edits:
            widget.textChanged.connect(lambda: self.set_modified())
        self.date_dt.dateChanged.connect(lambda: self.set_modified()) 
        all_tool_buttons = self.findChildren(QToolButton)
        for widget in all_tool_buttons:
            widget.clicked.connect(lambda: self.toolButton_clicked())
        all_rolbox_edits = self.findChildren(QComboBox)
        for widget in all_rolbox_edits:
            widget.activated.connect(lambda: self.set_modified())
        self.operator_cb.activated.connect(lambda: self.operator_changed())
        self.location_cb.addItems(self.locations)
        self.location_cb.activated.connect(lambda: self.location_changed())
        self.newOperator_ln.hide()
        self.newAircraft_ln.hide()
        self.label_38.hide()
        self.label_39.hide()
        self.make_window_title()


    @pyqtSlot()
    def on_actionNew_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box("Clear")
            if result == "iw_saveButton":
                self.save_document()
                self.reset_all_fields()
            elif result == "iw_nosaveButton":
                self.reset_all_fields()
        else:
            self.reset_all_fields()


    @pyqtSlot()
    def on_actionSave_triggered(self):
        self.save_document()


    @pyqtSlot()
    def on_actionSave_As_triggered(self):
        pass
        self.save_document(save_as=True)


    @pyqtSlot()
    def on_actionPrint_triggered(self):
        pass
        self.out_file_name_pdf = self.get_file_name_pdf()
        if not self.out_file_name_pdf:
            return
        if '.pdf' not in self.out_file_name_pdf:
            self.out_file_name_pdf = self.out_file_name_pdf + '.pdf'
        create_asmm_pdf(self, self.out_file_name_pdf)


    @pyqtSlot()
    def on_actionOpen_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box("Open")
            if result == "iw_saveButton":
                self.save_document()
                self.open_file()
            elif result == "iw_nosaveButton":
                self.open_file()
        else:
            self.open_file()


    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()


    @pyqtSlot()
    def on_actionEUFAR_N7SP_triggered(self):
        webbrowser.open('http://www.eufar.net/cms/standards-and-protocols/')
        
        
    @pyqtSlot()
    def on_actionHelp_triggered(self):
        webbrowser.open('http://www.eufar.net/cms/airborne-science-mission-metadata-help/')


    @pyqtSlot()
    def on_actionASMM_CreatorAbout_triggered(self):
        aboutText = ("The Airborne Science Mission Metadata (ASMM) Creator v%s offline version, was "
        + "developed by EUFAR using Eclipse %s, Python %s and PyQt %s. XML files generated by this "
        + "version conform to v%s of the ASMM XML standard. The opensource reporting library (v%s) "
        + "used for PDF report generation is provided and owned by <a href=http://www.reportlab.com"
        + "/opensource><span style=\" text-decoration: underline; color:#0000ff;\">Reportlab</a>.<b"
        + "r><br>For more information, or to report a bug, please contact <a href='mailto:olivier.h"
        + "enry.at.meteo.fr'><span style=\" text-decoration: underline; color:#0000ff;\">olivier.he"
        + "nry.at.meteo.fr</a>.<br><br>The latest offline version and source code of the ASMM Creat"
        + "or can be found at <a href=https://github.com/eufarn7sp/asmm-eufar><span style=\" text-d"
        + "ecoration: underline; color:#0000ff;\">https://github.com/eufarn7sp/asmm-eufar</a>.") % (_asmm_version, 
                                                                                                   _eclipse_version, 
                                                                                                   _py_version, 
                                                                                                   _qt_version, 
                                                                                                   _xml_version,
                                                                                                   _report_version)
        self.aboutWindow = MyAbout(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()

    
    @pyqtSlot()
    def on_actionASMM_XML_Standard_triggered(self):
        aboutText = ("<html><head/><body><p align=justify>The Airborne Science Mission Metadata (ASM"
        + "M) standard aims to harmonise descriptive information of science research flights. This "
        + "common description will allow users of the airborne science data to search past datasets"
        + " for specific meteorological conditions, geographical regions, cloud-types encountered, "
        + "particles sampled, and other parameters not evident from the data itself.<br> <br> For m"
        + "ore information, please read the following document: <a href=https://github.com/eufarn7s"
        + "p/asmm-eufar/blob/master/Documentation/ASMM%20-%20XML%20Implementation%20Rules.pdf   >AS"
        + "MM - XML Implementation Rules.pdf</a></p></body></html>")
        self.aboutWindow = MyStandard(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(460, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(460, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()
 

    @pyqtSlot()
    def on_actionChangelog_triggered(self):
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.logWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.logWindow.setGeometry(x2, y2, w2, h2)
        self.logWindow.exec_()


    @pyqtSlot()
    def on_readBoundingBoxButton_clicked(self):
        lat_min = None
        lat_max = None
        lon_min = None
        lon_max = None
        alt_min = None
        alt_max = None
        filename, fileext = QFileDialog.getOpenFileName(self,'Open associated NetCDF','','NetCDF files (*.nc'  # @UnusedVariable
                                               ' *.cdf);;All Files (*.*)')
        if not filename:
            return
        f = NetCdf(str(filename))
        var_list = f.get_variable_list()

        try:
            lat_min = f.get_attribute_value("geospatial_lat_min")
            lat_max = f.get_attribute_value("geospatial_lat_max")
        except KeyError:
            [var_name, ok] = QInputDialog.getItem(self, "Latitude Variable Name", "ERROR: Latitude "
                                                  "values not found. Please enter latitude variable"
                                                  " name.", var_list, current=0, editable=False)
            if var_name and ok:
                lat_values = f.read_variable(str(var_name))
                lat_min = min(lat_values[lat_values != 0])
                lat_max = max(lat_values[lat_values != 0])
        try:
            lon_min = f.get_attribute_value("geospatial_lon_min")
            lon_max = f.get_attribute_value("geospatial_lon_max")
        except KeyError:
            [var_name, ok] = QInputDialog.getItem(self, "Longitude Variable Name", "ERROR: Longitud"
                                                  "e values not found. Please select longitude vari"
                                                  "able name.", var_list, current=0, editable=False)
            if var_name and ok:
                lon_values = f.read_variable(str(var_name))
                lon_min = min(lon_values[lon_values != 0])
                lon_max = max(lon_values[lon_values != 0])
        try:
            alt_min = f.get_attribute_value("geospatial_vertical_min")
            alt_max = f.get_attribute_value("geospatial_vertical_max")
        except KeyError:
            [var_name, ok] = QInputDialog.getItem(self, "Altitude Variable Name", "ERROR: Altitude "
                                                  "values not found. Please enter altitude variable"
                                                  " name.", var_list, current=0, editable=False)
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
        self.westBoundLongitudeLine.setCursorPosition(0)
        self.eastBoundLongitudeLine.setCursorPosition(0)
        self.northBoundLatitudeLine.setCursorPosition(0)
        self.southBoundLatitudeLine.setCursorPosition(0)
        self.minAltitudeLine.setCursorPosition(0)
        self.maxAltitudeLine.setCursorPosition(0)


    @pyqtSlot()
    def on_imageAddButton_clicked(self):
        if self.verticalLayout_52.count() < 10:
            filename, fileext = QFileDialog.getOpenFileName(self,'Open an image','','All Files (*.*);;Images'  # @UnusedVariable
                                                   ' (*.jpg *.jpeg *.bmp *.png *.gif *.tiff)')
            if filename:
                add_image(self, filename)
                self.im_del[-1].clicked.connect(lambda: self.del_image())
                self.im_label[-1].clicked.connect(lambda: self.show_image())
        else:    
            alertBox = QMessageBox()
            alertBox.about(self, "Warning", "You can't add more than 10 images.")

    
    @pyqtSlot()
    def on_urlAddButton_clicked(self):
        if self.verticalLayout_52.count() < 10:
            x = QCursor.pos().x()
            y = QCursor.pos().y()
            x = x - 150
            y = y + 50
            self.urlWindow = MyURL()
            self.urlWindow.setMinimumSize(QtCore.QSize(420, self.urlWindow.sizeHint().height()))
            self.urlWindow.setMaximumSize(QtCore.QSize(420, self.urlWindow.sizeHint().height()))
            self.urlWindow.setGeometry(x, y, 420, self.urlWindow.sizeHint().height())
            if self.urlWindow.exec_():
                add_image(self, self.urlWindow.ck_inputLine.text())
                self.im_del[-1].clicked.connect(lambda: self.del_image())
                self.im_label[-1].clicked.connect(lambda: self.show_image())
        else:    
            alertBox = QMessageBox()
            alertBox.about(self, "Warning", "You can't add more than 10 images.")
    
    
    def del_image(self):
        delete_image(self)
        
    
    def show_image(self):
        display_image(self)


    def closeEvent(self, event):
        if self.modified:
            result = self.make_onsave_msg_box("Close")
            if result == "iw_saveButton":
                self.save_document()
                shutil.rmtree(self.dirpath)
                event.accept()
            elif result == "iw_nosaveButton":
                shutil.rmtree(self.dirpath)
                event.accept()
            else:
                event.ignore()
        else:
            shutil.rmtree(self.dirpath)
            self.close()


    def make_window_title(self):
        if self.saved:
            title_string = "ASMM Creator v{0} - ".format(_asmm_version) + self.out_file_name
        else:
            title_string = "ASMM Creator v{0} - unsaved".format(_asmm_version)
        if self.modified:
            title_string += ' - modified'
        self.setWindowTitle(title_string)


    def set_modified(self):
        if not self.modified:
            self.modified = True
            self.make_window_title()


    def save_document(self, save_as=False):
        cancel = fill_all_fields(self)
        if cancel == True:
            return
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
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, "Save XML File","!!!Flight identifier!!!_xxxxxxxxxx.xml"  # @UnusedVariable
                                                                  , filter='XML Files (*.xml)')
        return out_file_name


    def get_file_name_pdf(self):
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('pdf')
        out_file_name_pdf, out_file_ext = file_dialog.getSaveFileName(self, "Save PDF File", filter='PDF Files (*.pdf)')  # @UnusedVariable
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
        for i in reversed(range(self.gridLayout_16.count())):
            self.gridLayout_16.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_14.count())):
            self.gridLayout_14.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_15.count())):
            self.gridLayout_15.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_25.count())):
            self.gridLayout_25.itemAt(i).widget().deleteLater()
        self.operator_cb.setCurrentIndex(0)
        self.newOperator_ln.clear()
        self.newAircraft_ln.clear()
        self.newOperator_ln.hide()
        self.newAircraft_ln.hide()
        self.label_38.hide()
        self.label_39.hide()
        self.aircraft_cb.clear()
        self.aircraft_cb.setEnabled(False)    
        self.location_cb.setCurrentIndex(0)
        self.detailList.clear()
        self.detailList.setEnabled(False)
        for i in reversed(range(0, len(self.images_pdf_path))):
            delete_image(self, i)
        objectsInit(self)
        self.make_window_title()


    def make_onsave_msg_box(self, string):
        self.presaveWindow = MyWarning(string)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.presaveWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.presaveWindow.setGeometry(x2, y2, w2, h2)
        self.presaveWindow.setMinimumSize(QtCore.QSize(450, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.setMaximumSize(QtCore.QSize(452, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.exec_()
        return self.presaveWindow.buttonName


    def open_file(self):
        out_file_name, out_file_ext = QFileDialog.getOpenFileName(self,'Open XML File','','XML Files (*.xml)')  # @UnusedVariable
        if out_file_name:
            read_asmm_xml(self, out_file_name)
            self.saved = True
            self.modified = False
            self.out_file_name = out_file_name
            self.make_window_title()


    def addListItem(self, title, label, listWidget, item_list):
        x = QCursor.pos().x()
        y = QCursor.pos().y()
        x = x - 150
        y = y + 50
        self.siteWindow = MySite()
        self.siteWindow.setMinimumSize(QtCore.QSize(340, self.siteWindow.sizeHint().height()))
        self.siteWindow.setMaximumSize(QtCore.QSize(340, self.siteWindow.sizeHint().height()))
        self.siteWindow.setGeometry(x, y, 340, self.siteWindow.sizeHint().height())
        self.siteWindow.label.setText(label)
        self.siteWindow.setWindowTitle(title)
        if self.siteWindow.exec_():
            self.modified = True
            self.make_window_title()
            item_list.append(self.siteWindow.ck_inputLine.text())
            listWidget.addItem(self.siteWindow.ck_inputLine.text())


    def removeListItem(self, listWidget, item_list):
        selected_line = listWidget.currentRow()
        if selected_line >= 0:
            selected_item = listWidget.currentItem()
            item_list.remove(selected_item.text())
            listWidget.takeItem(selected_line)
            self.modified = True
            self.make_window_title()

    
    def toolButton_clicked(self):
        if "infoButton" in self.sender().objectName():
            button_clicked(self)
        elif "groundAddButton" in self.sender().objectName():
            self.addListItem("Add a Ground Site", "Please, enter a name for the new Ground Site.", 
                             self.groundListWidget, self.ground_site_list)
        elif "armAddButton" in self.sender().objectName():
            self.addListItem("Add an ARM Site", "Please, enter a name for the new ARM Site.", 
                             self.armListWidget, self.arm_site_list)
        elif "armMobileAddButton" in self.sender().objectName():
            self.addListItem("Add an ARM Mobile Site", "Please, enter a name for the new ARM Mobile Site.", 
                             self.armMobileListWidget, self.arm_mobile_list)
        elif "vesselAddButton" in self.sender().objectName():
            self.addListItem("Add a Research Vessel", "Please, enter a name for the new Research Vessel.", 
                             self.vesselListWidget, self.research_vessel_list)
        elif "groundRemoveButton" in self.sender().objectName():
            self.removeListItem(self.groundListWidget, self.ground_site_list)
        elif "armRemoveButton" in self.sender().objectName():
            self.removeListItem(self.armListWidget, self.arm_site_list)
        elif "armMobileRemoveButton" in self.sender().objectName():
            self.removeListItem(self.armMobileListWidget, self.arm_mobile_list)
        elif "vesselRemoveButton" in self.sender().objectName():
            self.removeListItem(self.vesselListWidget, self.research_vessel_list)
        elif "addButton" in self.sender().objectName():
            if len(self.ck_list_dict.get(str(self.sender().objectName()[:2]))) < 12:
                add_clicked(self)
            else:
                alertBox = QMessageBox()
                alertBox.about(self, "Warning", "You can't add more than 12 checkboxes.")
                return
    
    
    def location_changed(self):
        if self.location_cb.currentText() == "Make a choice...":
            self.detailList.clear()
            self.detailList.setEnabled(False)
        elif self.location_cb.currentText() == "Continents":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.continents) 
        elif self.location_cb.currentText() == "Countries":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.countries)
        elif self.location_cb.currentText() == "Oceans":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.oceans)
        elif self.location_cb.currentText() == "Regions":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.regions)


    def operator_changed(self):
        if self.operator_cb.currentText() == "Make a choice...":
            self.newAircraft_ln.hide()
            self.newOperator_ln.hide()
            self.label_38.hide()
            self.label_39.hide()
            self.aircraft_cb.clear()
            self.aircraft_cb.setEnabled(False)
        elif self.operator_cb.currentText() == "Other...":
            self.newOperator_ln.show()
            self.newAircraft_ln.show()
            self.label_38.show()
            self.label_39.show()
            self.aircraft_cb.clear()
            self.aircraft_cb.addItem("Other...")
            self.aircraft_cb.setEnabled(True)
        else:
            self.newOperator_ln.hide()
            self.newAircraft_ln.hide()
            self.label_38.hide()
            self.label_39.hide()
            self.aircraft_cb.clear()
            self.aircraft_cb.addItem("Make a choice...")
            self.aircraft_cb.setEnabled(True)
            for i in range(len(self.operators_aircraft)):
                if self.operator_cb.currentText() == self.operators_aircraft[i][0]:
                    self.aircraft_cb.addItem(self.operators_aircraft[i][1])
            if self.aircraft_cb.count() < 3:
                self.aircraft_cb.removeItem(0)
            self.aircraft_cb.setCurrentIndex(0)


class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()
        
        
class MyLog(QtWidgets.QDialog, Ui_Changelog):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.log_txBrower.setPlainText(open("Documentation/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()
 
 
class MyStandard(QtWidgets.QDialog, Ui_aboutStandard):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close() 
 
 
class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, string):
        QWidget.__init__(self)
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QToolButton)
        for widget in all_buttons:
            widget.clicked.connect(self.closeWindow)
        self.iw_nosaveButton.setText(string + " without saving")

    def closeWindow(self):
        self.buttonName = self.sender().objectName()
        self.close()
 
     
class MySite(QtWidgets.QDialog, Ui_Addsite):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ck_cancelButton.clicked.connect(self.closeWindow)
        self.ck_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()
        

class MyURL(QtWidgets.QDialog, Ui_AddURL):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ck_cancelButton.clicked.connect(self.closeWindow)
        self.ck_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()
        