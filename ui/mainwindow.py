# -*- coding: utf-8 -*-

import webbrowser
import os
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QCursor
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QInputDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QTextEdit
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QWidget
from Ui_mainwindow import Ui_MainWindow
from Ui_aboutwindow import Ui_aboutWindow
from Ui_aboutstandard import Ui_aboutStandard
from Ui_logwindow import Ui_Changelog
from Ui_presavewindow import Ui_presaveWindow
from Ui_addsite import Ui_Addsite
from Ui_addUrl import Ui_AddURL
from _version import _asmm_version
from _version import _xml_version
from _version import _py_version
from _version import _report_version
from _version import _qt_version
from _version import _eclipse_version
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


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS  # @UndefinedVariable
        else:
            self.progPath = os.path.abspath(".")
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.tabLayout = 0
        if resolution.height() < 1000:
            self.tabLayout = 1
            self.setupUi_tab(self)
        else:
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
        all_rolbox_edits = self.findChildren(QComboBox)
        for widget in all_rolbox_edits:
            QObject.connect(widget, SIGNAL("activated(QString)"), self.set_modified)
        QObject.connect(self.operatorList, SIGNAL("activated(QString)"), self.operator_changed)
        self.locationList.addItems(self.locations)
        QObject.connect(self.locationList, SIGNAL("activated(QString)"), self.location_changed)
        self.make_window_title()


    @pyqtSignature("")
    def on_generateXMLButton_clicked(self):
        #self.save_document()
        self.toolBox = QtGui.QTabWidget(self.scrollAreaWidgetContents)


    @pyqtSignature("")
    def on_exitButton_clicked(self):
        self.close()


    @pyqtSignature("")
    def on_actionNew_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box("Clear","new_icon.png")
            if result == "iw_saveButton":
                self.save_document()
                self.reset_all_fields()
            elif result == "iw_nosaveButton":
                self.reset_all_fields()
        else:
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
            result = self.make_onsave_msg_box("Open","open_icon.png")
            if result == "iw_saveButton":
                self.save_document()
                self.open_file()
            elif result == "iw_nosaveButton":
                self.open_file()
        else:
            self.open_file()


    @pyqtSignature("")
    def on_actionExit_triggered(self):
        self.close()


    @pyqtSignature("")
    def on_actionEUFAR_N7SP_triggered(self):
        webbrowser.open('http://www.eufar.net/')


    @pyqtSignature("")
    def on_actionASMM_CreatorAbout_triggered(self):
        aboutText = "The Airborne Science Mission Metadata (ASMM) Creator v%s offline version, was "
        + "developed by EUFAR using Eclipse %s, Python %s and PyQt %s. XML files generated by this "
        + "version conform to v%s of the ASMM XML standard. The opensource reporting library (v%s) "
        + "used for PDF report generation is provided and owned by <a href=http://www.reportlab.com"
        + "/opensource><span style=\" text-decoration: underline; color:#0000ff;\">Reportlab</a>.<b"
        + "r><br>For more information, or to report a bug, please contact <a href='mailto:olivier.h"
        + "enry.at.meteo.fr'><span style=\" text-decoration: underline; color:#0000ff;\">olivier.he"
        + "nry.at.meteo.fr</a>.<br><br>The latest offline version and source code of the ASMM Creat"
        + "or can be found at <a href=https://github.com/eufarn7sp/asmm-eufar><span style=\" text-d"
        + "ecoration: underline; color:#0000ff;\">https://github.com/eufarn7sp/asmm-eufar</a>." % (_asmm_version, 
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
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(452, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()

    
    @pyqtSignature("")
    def on_actionASMM_XML_Standard_triggered(self):
        aboutText = "<html><head/><body><p align=justify>The Airborne Science Mission Metadata (ASM"
        + "M) standard aims to harmonise descriptive information of science research flights. This "
        + "common description will allow users of the airborne science data to search past datasets"
        + " for specific meteorological conditions, geographical regions, cloud-types encountered, "
        + "particles sampled, and other parameters not evident from the data itself.<br> <br> For m"
        + "ore information, please read the following document: <a href=https://github.com/eufarn7s"
        + "p/asmm-eufar/blob/master/Documentation/ASMM%20-%20XML%20Implementation%20Rules.pdf   >AS"
        + "MM - XML Implementation Rules.pdf</a></p></body></html>"
        self.aboutWindow = MyStandard(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()  # @UnusedVariable
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(452, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()
 

    @pyqtSignature("")
    def on_actionChangelog_triggered(self):
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.logWindow.geometry().getRect()  # @UnusedVariable
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
        filename = QFileDialog.getOpenFileName(self,'Open associated NetCDF','','NetCDF files (*.nc'
                                               ' *.cdf);;All Files (*.*)')
        if not filename:
            return
        f = NetCdf(str(filename))
        var_list = f.get_variable_list()
        var_list.sort()
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


    @pyqtSignature("")
    def on_imageAddButton_clicked(self):
        if self.verticalLayout_52.count() < 10:
            filename = QFileDialog.getOpenFileName(self,'Open an image','','All Files (*.*);;Images'
                                                   ' (*.jpg *.jpeg *.bmp *.png *.gif *.tiff)')
            filename = unicode(filename)
            if filename:
                add_image(self, filename)
                for widget in self.im_del:
                    QObject.disconnect(widget, SIGNAL("clicked()"), self.del_image)
                for widget in self.im_del:
                    QObject.connect(widget, SIGNAL("clicked()"), self.del_image)
                for widget in self.im_label:
                    QObject.disconnect(widget, SIGNAL("clicked()"), self.show_image)
                for widget in self.im_label:
                    QObject.connect(widget, SIGNAL("clicked()"), self.show_image)
        else:    
            alertBox = QMessageBox()
            alertBox.about(self, "Warning", "You can't add more than 10 images.")

    
    @pyqtSignature("")
    def on_urlAddButton_clicked(self):
        if self.verticalLayout_52.count() < 10:
            x = QCursor.pos().x()
            y = QCursor.pos().y()
            x = x - 150
            y = y + 50
            self.urlWindow = MyURL()
            self.urlWindow.setMinimumSize(QtCore.QSize(300, self.urlWindow.sizeHint().height()))
            self.urlWindow.setMaximumSize(QtCore.QSize(300, self.urlWindow.sizeHint().height()))
            self.urlWindow.setGeometry(x, y, 300, self.urlWindow.sizeHint().height())
            if self.urlWindow.exec_():
                add_image(self, self.urlWindow.ck_inputLine.text())
                for widget in self.im_del:
                    QObject.disconnect(widget, SIGNAL("clicked()"), self.del_image)
                for widget in self.im_del:
                    QObject.connect(widget, SIGNAL("clicked()"), self.del_image)
        else:    
            alertBox = QMessageBox()
            alertBox.about(self, "Warning", "You can't add more than 10 images.")
    
    
    def del_image(self):
        delete_image(self)
        
    
    def show_image(self):
        display_image(self)


    def closeEvent(self, event):
        if self.modified:
            result = self.make_onsave_msg_box("Close", "exit_icon.png")
            if result == "iw_saveButton":
                self.save_document()
                event.accept()
            elif result == "iw_nosaveButton":
                event.accept()
            else:
                event.ignore()
        else:
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
        out_file_name = unicode(file_dialog.getSaveFileName(self, "Save XML File", filter='XML Files'
                                                            ' (*.xml);;Text Files (*.txt)'))
        return out_file_name


    def get_file_name_pdf(self):
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('pdf')
        out_file_name_pdf = unicode(file_dialog.getSaveFileName(self, "Save PDF File", filter='PDF '
                                                                'Files (*.pdf)'))
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
        for i in reversed(range(self.gridLayout_13.count())):
            self.gridLayout_13.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_14.count())):
            self.gridLayout_14.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_15.count())):
            self.gridLayout_15.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.gridLayout_25.count())):
            self.gridLayout_25.itemAt(i).widget().deleteLater()
        self.operatorList.setCurrentIndex(0)
        if hasattr(self, "tmpOperatorLine"):
            if self.horizontalLayout_77.count() > 0:
                self.label_38.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arrow_e"
                                                                "mpty.png")))
                self.label_39.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arrow_e"
                                                                "mpty.png")))
                self.tmpOperatorLine.deleteLater()
                self.tmpAircraftLine.deleteLater()
        self.aircraftList.clear()
        self.aircraftList.setEnabled(False)    
        self.locationList.setCurrentIndex(0)
        self.detailList.clear()
        self.detailList.setEnabled(False)
        for i in reversed(range(0, len(self.images_pdf_path))):
            delete_image(self, i)
        objectsInit(self)
        self.make_window_title()


    def make_onsave_msg_box(self, string, iconName):
        self.presaveWindow = MyWarning(string, iconName)
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
        (out_file_name, filter) = QFileDialog.getOpenFileNameAndFilter(self, "Open XML File", filter  # @ReservedAssignment
                                                                       ="XML Files (*.xml)")
        out_file_name = unicode(out_file_name)
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
        self.siteWindow.setMinimumSize(QtCore.QSize(300, self.siteWindow.sizeHint().height()))
        self.siteWindow.setMaximumSize(QtCore.QSize(300, self.siteWindow.sizeHint().height()))
        self.siteWindow.setGeometry(x, y, 300, self.siteWindow.sizeHint().height())
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
            item_list.remove(unicode(selected_item.text()))
            listWidget.takeItem(selected_line)
            self.modified = True
            self.make_window_title()


    def infoButton_clicked(self):
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
        
        
    def addButton_clicked(self):
        if "addButton" in self.sender().objectName():
            if len(self.ck_list_dict.get(str(self.sender().objectName()[:2]))) < 12:
                add_clicked(self)
            else:
                alertBox = QMessageBox()
                alertBox.about(self, "Warning", "You can't add more than 12 checkboxes.")
                return


    def location_changed(self):
        if self.locationList.currentText() == "Make a choice...":
            self.detailList.clear()
            self.detailList.setEnabled(False)
        elif self.locationList.currentText() == "Continents":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.continents) 
        elif self.locationList.currentText() == "Countries":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.countries)
        elif self.locationList.currentText() == "Oceans":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.oceans)
        elif self.locationList.currentText() == "Regions":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.regions)


    def operator_changed(self):
        if self.operatorList.currentText() == "Make a choice...":
            if hasattr(self, "tmpOperatorLine"):
                if self.horizontalLayout_77.count() > 0:
                    self.label_38.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arr"
                                                                    "ow_empty.png")))
                    self.label_39.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arr"
                                                                    "ow_empty.png")))
                    self.tmpOperatorLine.deleteLater()
                    self.tmpAircraftLine.deleteLater()
            self.aircraftList.clear()
            self.aircraftList.setEnabled(False)
        elif self.operatorList.currentText() == "Other...":
            self.aircraftList.clear()
            self.aircraftList.addItem("Other")
            self.aircraftList.setEnabled(True)
            self.label_38.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arrow.png")))
            self.label_39.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arrow.png")))
            self.tmpOperatorLine = QtGui.QLineEdit(self.flight_information_page)
            self.tmpOperatorLine.setMinimumSize(QtCore.QSize(300, 27))
            self.tmpOperatorLine.setMaximumSize(QtCore.QSize(300, 27))
            self.tmpOperatorLine.setFrame(False)
            self.tmpOperatorLine.setObjectName("tmpOperatorLine")
            self.horizontalLayout_77.addWidget(self.tmpOperatorLine)
            self.tmpAircraftLine = QtGui.QLineEdit(self.flight_information_page)
            self.tmpAircraftLine.setMinimumSize(QtCore.QSize(300, 27))
            self.tmpAircraftLine.setMaximumSize(QtCore.QSize(300, 27))
            self.tmpAircraftLine.setFrame(False)
            self.tmpAircraftLine.setObjectName("tmpAircraftLine")
            self.horizontalLayout_78.addWidget(self.tmpAircraftLine)
        else:
            if hasattr(self, "tmpOperatorLine"):
                if self.horizontalLayout_77.count() > 0:
                    self.label_38.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arr"
                                                                    "ow_empty.png")))
                    self.label_39.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/fwd_arr"
                                                                    "ow_empty.png")))
                    self.tmpOperatorLine.deleteLater()
                    self.tmpAircraftLine.deleteLater()
            self.aircraftList.clear()
            self.aircraftList.addItem("Do your choice...")
            self.aircraftList.setEnabled(True)
            for i in range(len(self.operators_aircraft)):
                if self.operatorList.currentText() == self.operators_aircraft[i][0]:
                    self.aircraftList.addItem(self.operators_aircraft[i][1])
            if self.aircraftList.count() < 3:
                self.aircraftList.removeItem(0)
            self.aircraftList.setCurrentIndex(0)


class MyAbout(QtGui.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS  # @UndefinedVariable
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
            self.progPath = sys._MEIPASS  # @UndefinedVariable
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
            self.progPath = sys._MEIPASS  # @UndefinedVariable
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close() 
 
 
class MyWarning(QtGui.QDialog, Ui_presaveWindow):
    def __init__(self, string, iconName):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS  # @UndefinedVariable
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QPushButton)
        for widget in all_buttons:
            QObject.connect(widget, SIGNAL("clicked()"), self.closeWindow) 
        self.iw_nosaveButton.setText(string + " without saving")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/" + iconName)), QtGui.QIcon.
                       Normal, QtGui.QIcon.Off)
        self.iw_nosaveButton.setIcon(icon)

    def closeWindow(self):
        self.buttonName = self.sender().objectName()
        self.close()
 
     
class MySite(QtGui.QDialog, Ui_Addsite):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS  # @UndefinedVariable
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.ck_cancelButton.clicked.connect(self.closeWindow)
        self.ck_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()
        

class MyURL(QtGui.QDialog, Ui_AddURL):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        if getattr(sys, 'frozen', False):
            self.progPath = sys._MEIPASS  # @UndefinedVariable
        else:
            self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.ck_cancelButton.clicked.connect(self.closeWindow)
        self.ck_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()   