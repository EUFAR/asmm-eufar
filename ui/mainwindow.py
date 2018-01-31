import webbrowser
import tempfile
import shutil
import requests
import logging
import platform
import os
import configparser
from collections import Counter
from PyQt5 import QtCore, QtWidgets, Qt, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from ui.Ui_aboutwindow import Ui_aboutWindow
from ui.Ui_aboutstandard import Ui_aboutStandard
from ui.Ui_logwindow import Ui_Changelog
from ui.Ui_presavewindow import Ui_presaveWindow
from ui.Ui_addsite import Ui_Addsite
from ui.Ui_addUrl import Ui_AddURL
from ui.Ui_apiwindow import Ui_apiWindow
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


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, parent=None):
        self.asmm_path = path
        QtWidgets.QMainWindow.__init__(self, parent)
        logging.info('mainwindow.py - UI initialization ...')
        self.setupUi(self)
        objectsInit(self)
        self.aircraft_db = {}
        self.operator_db = {}
        self.fill_operator_rolebox()
        self.dirpath = tempfile.mkdtemp()
        all_check_boxes = self.findChildren(QtWidgets.QCheckBox)
        for check_box in all_check_boxes:
            check_box.stateChanged.connect(lambda: self.set_modified())
        all_text_edits = self.findChildren(QtWidgets.QTextEdit)
        for widget in all_text_edits:
            widget.textChanged.connect(lambda: self.set_modified())
        all_line_edits = self.findChildren(QtWidgets.QLineEdit)
        for widget in all_line_edits:
            widget.textChanged.connect(lambda: self.set_modified())
        self.date_dt.dateChanged.connect(lambda: self.set_modified()) 
        all_tool_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_tool_buttons:
            widget.clicked.connect(lambda: self.toolButton_clicked())
        all_rolbox_edits = self.findChildren(QtWidgets.QComboBox)
        for widget in all_rolbox_edits:
            widget.activated.connect(lambda: self.set_modified())
        self.operator_cb.activated.connect(lambda: self.operator_changed())
        self.location_cb.addItems(self.locations)
        self.location_cb.activated.connect(lambda: self.location_changed())
        self.newOperator_ln.hide()
        self.newAircraft_ln.hide()
        self.label_38.hide()
        self.label_39.hide()
        self.newCountry_lb.hide()
        self.newCountry_cb.hide()
        self.newRegistration_lb.hide()
        self.newRegistration_ln.hide()
        self.newManufacturer_lb.hide()
        self.newManufacturer_ln.hide() 
        "patch for combobox stylesheet"
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.location_cb.setItemDelegate(itemDelegate)
        self.detailList.setItemDelegate(itemDelegate)
        self.operator_cb.setItemDelegate(itemDelegate)
        self.aircraft_cb.setItemDelegate(itemDelegate)
        self.newCountry_cb.setItemDelegate(itemDelegate)
        self.contact_cb.setItemDelegate(itemDelegate)
        "-----------------------------"
        self.menubar.setStyleSheet("QMenuBar {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
            "                      stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
            "}\n"
            "\n"
            "QMenuBar::item {\n"
            "    spacing: 3px;\n"
            "    padding: 5px 5px 5px 5px;\n"
            "    background: transparent;\n"
            "}\n"
            "\n"
            "QMenuBar::item:selected {\n"
            "    border: 0px solid #7eb4ea;\n"
            "    border-radius: 1px;\n"
            "    background-color: rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QMenu {\n"
            "    background-color: #f0f0f0;\n"
            "    border: 0px solid #f0f0f0;\n"
            "}\n"
            "\n"
            "QMenu::item:selected {\n"
            "    background-color: rgb(200,200,200);\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QMenu::icon {\n"
            "    margin-left: 20px;\n"
            "    background-color: red;\n"
            "    border: none;\n"
            "}")
        self.make_window_title()
        self.api_eufar_acronym_completer()
        self.api_eufar_database_parsing()
        config_dict = configparser.ConfigParser()
        config_dict.read(os.path.join(path, 'asmm_creator.ini'))
        show_api_info = config_dict.get('OPTIONS', 'api_info')
        result = False
        if show_api_info == 'True':
            result = self.api_eufar_information()
            if show_api_info != str(result):
                config_dict.set('OPTIONS', 'api_info', str(result))
                with open(os.path.join(path, 'asmm_creator.ini'), 'w') as configfile:
                    config_dict.write(configfile)
        logging.info('mainwindow.py - UI initialized !')
        logging.info('**************************************************')
        

    @QtCore.pyqtSlot()
    def on_actionNew_triggered(self):
        logging.debug('mainwindow.py - on_actionNew_triggered - self.modified ' + str(self.modified))
        if self.modified:
            result = self.make_onsave_msg_box("Clear")
            if result == "iw_saveButton":
                self.save_document()
                self.reset_all_fields()
            elif result == "iw_nosaveButton":
                self.reset_all_fields()
        else:
            self.reset_all_fields()
        

    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        logging.debug('mainwindow.py - on_actionSave_triggered')
        self.save_document()


    @QtCore.pyqtSlot()
    def on_actionSave_As_triggered(self):
        logging.debug('mainwindow.py - on_actionSave_As_triggered')
        self.save_document(save_as=True)


    @QtCore.pyqtSlot()
    def on_actionPrint_triggered(self):
        logging.debug('mainwindow.py - on_actionPrint_triggered')
        self.out_file_name_pdf = self.get_file_name_pdf()
        if not self.out_file_name_pdf:
            return
        if '.pdf' not in self.out_file_name_pdf:
            self.out_file_name_pdf = self.out_file_name_pdf + '.pdf'
        create_asmm_pdf(self, self.out_file_name_pdf)


    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        logging.debug('mainwindow.py - on_actionOpen_triggered - self.modified ' + str(self.modified))
        if self.modified:
            result = self.make_onsave_msg_box("Open")
            if result == "iw_saveButton":
                self.save_document()
                self.open_file()
            elif result == "iw_nosaveButton":
                self.open_file()
        else:
            self.open_file()


    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        logging.debug('mainwindow.py - on_actionExit_triggered')
        self.close()


    @QtCore.pyqtSlot()
    def on_actionEUFAR_N7SP_triggered(self):
        logging.debug('mainwindow.py - on_actionEUFAR_N7SP_triggered')
        webbrowser.open('http://www.eufar.net/cms/standards-and-protocols/')
        
        
    @QtCore.pyqtSlot()
    def on_actionHelp_triggered(self):
        logging.debug('mainwindow.py - on_actionHelp_triggered')
        webbrowser.open('http://www.eufar.net/cms/airborne-science-mission-metadata-help/')


    @QtCore.pyqtSlot()
    def on_actionASMM_CreatorAbout_triggered(self):
        logging.debug('mainwindow.py - on_actionASMM_CreatorAbout_triggered')
        aboutText = ("The Airborne Science Mission Metadata (ASMM) Creator v%s offline version, was "
        + "developed by EUFAR using Eclipse %s, Python %s and PyQt %s. XML files generated by this "
        + "version conform to v%s of the ASMM XML standard. The opensource reporting library (v%s) "
        + "used for PDF report generation is provided and owned by <a href=http://www.reportlab.com"
        + "/opensource><span style=\" text-decoration: underline; color:#0000ff;\">Reportlab</a>.<b"
        + "r><br>For more information, or to report a bug, please contact <a href='mailto:"
        + "bureau.at.eufar.net'><span style=\" text-decoration: underline; color:#0000ff;\">"
        + "bureau.at.eufar.net</a>.<br><br>The latest offline version and source code of the ASMM Creat"
        + "or can be found at <a href=https://github.com/EUFAR/asmm-eufar><span style=\" text-d"
        + "ecoration: underline; color:#0000ff;\">https://github.com/EUFAR/asmm-eufar</a>.") % (_asmm_version, 
                                                                                                   _eclipse_version, 
                                                                                                   _py_version, 
                                                                                                   _qt_version, 
                                                                                                   _xml_version,
                                                                                                   _report_version)
        self.aboutWindow = MyAbout(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.aboutWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(480, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()

    
    @QtCore.pyqtSlot()
    def on_actionASMM_XML_Standard_triggered(self):
        logging.debug('mainwindow.py - on_actionASMM_XML_Standard_triggered')
        aboutText = ("<html><head/><body><p align=justify>The Airborne Science Mission Metadata (ASM"
        + "M) standard aims to harmonise descriptive information of science research flights. This "
        + "common description will allow users of the airborne science data to search past datasets"
        + " for specific meteorological conditions, geographical regions, cloud-types encountered, "
        + "particles sampled, and other parameters not evident from the data itself.<br> <br> For m"
        + "ore information, please read the following document: <a href=https://github.com/EUFAR"
        + "/asmm-eufar/blob/master/Documentation/ASMM%20-%20XML%20Implementation%20Rules.pdf   >AS"
        + "MM - XML Implementation Rules.pdf</a></p></body></html>")
        self.aboutWindow = MyStandard(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.aboutWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(460, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(460, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()
 

    @QtCore.pyqtSlot()
    def on_actionChangelog_triggered(self):
        logging.debug('mainwindow.py - on_actionChangelog_triggered')
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.logWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.logWindow.setGeometry(x2, y2, w2, h2)
        self.logWindow.exec_()


    @QtCore.pyqtSlot()
    def on_readBoundingBoxButton_clicked(self):
        logging.debug('mainwindow.py - on_readBoundingBoxButton_clicked')
        lat_min, lat_max, lon_min, lon_max, alt_min, alt_max = None, None, None, None, None, None
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self,'Open associated NetCDF','',
                                                        'NetCDF files (*.nc *.cdf);;All Files (*.*)')
        if not filename:
            return
        f = NetCdf(str(filename))
        var_list = f.get_variable_list()
        try:
            lat_min = round(f.get_attribute_value("geospatial_lat_min"), 2)
            lat_max = round(f.get_attribute_value("geospatial_lat_max"), 2)
        except KeyError:
            logging.error('mainwindow.py - on_readBoundingBoxButton_clicked - KeyError, lat_min or '
                          + 'lat_max not found.')
            attr_found = False
            for var_name in var_list:
                try:
                    attr_val = f.get_attribute_value('standard_name', var_name)
                    if attr_val == 'latitude':
                        attr_found = True
                        break
                except KeyError:
                    pass
            if attr_found:
                lat_values = f.read_variable(str(var_name))
                lat_min = round(min(lat_values[lat_values != 0]), 2)
                lat_max = round(max(lat_values[lat_values != 0]), 2)
            else:
                [var_name, ok] = QtWidgets.QInputDialog.getItem(self, "Latitude Variable Name", "ERROR: Latitude "
                                                      "values not found. Please select the latitude variable in the"
                                                      " following list.", var_list, current=0, editable=False)
                if var_name and ok:
                    lat_values = f.read_variable(str(var_name))
                    lat_min = round(min(lat_values[lat_values != 0]), 2)
                    lat_max = round(max(lat_values[lat_values != 0]), 2)
        try:
            lon_min = round(f.get_attribute_value("geospatial_lon_min"), 2)
            lon_max = round(f.get_attribute_value("geospatial_lon_max"), 2)
        except KeyError:
            logging.error('mainwindow.py - on_readBoundingBoxButton_clicked - KeyError, lon_min or '
                          + 'lon_max not found.')
            attr_found = False
            for var_name in var_list:
                try:
                    attr_val = f.get_attribute_value('standard_name', var_name)
                    if attr_val == 'longitude':
                        attr_found = True
                        break
                except KeyError:
                    pass
            if attr_found:
                lon_values = f.read_variable(str(var_name))
                lon_min = round(min(lon_values[lon_values != 0]), 2)
                lon_max = round(max(lon_values[lon_values != 0]), 2)
            else:
                [var_name, ok] = QtWidgets.QInputDialog.getItem(self, "Longitude Variable Name", "ERROR: Longitud"
                                                      "e values not found. Please select the longitude vari"
                                                      "able in the following list.", var_list, current=0, editable=False)
                if var_name and ok:
                    lon_values = f.read_variable(str(var_name))
                    lon_min = round(min(lon_values[lon_values != 0]), 2)
                    lon_max = round(max(lon_values[lon_values != 0]), 2)
        try:
            alt_min = round(f.get_attribute_value("geospatial_vertical_min"), 2)
            alt_max = round(f.get_attribute_value("geospatial_vertical_max"), 2)
        except KeyError:
            logging.error('mainwindow.py - on_readBoundingBoxButton_clicked - KeyError, alt_min or '
                          + 'alt_max not found.')
            attr_found = False
            for var_name in var_list:
                try:
                    attr_val = f.get_attribute_value('standard_name', var_name)
                    if attr_val == 'altitude':
                        attr_found = True
                        break
                except KeyError:
                    pass
            if attr_found:
                alt_values = f.read_variable(str(var_name))
                alt_min = round(min(alt_values[alt_values != 0]), 2)
                alt_max = round(max(alt_values[alt_values != 0]), 2)
            else:
                [var_name, ok] = QtWidgets.QInputDialog.getItem(self, "Altitude Variable Name", "ERROR: Altitude "
                                                      "values not found. Please select the altitude variable in"
                                                      " the following list.", var_list, current=0, editable=False)
                if var_name and ok:
                    alt_values = f.read_variable(str(var_name))
                    alt_min = round(min(alt_values[alt_values != 0]), 2)
                    alt_max = round(max(alt_values[alt_values != 0]), 2)
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


    @QtCore.pyqtSlot()
    def on_imageAddButton_clicked(self):
        logging.debug('mainwindow.py - on_imageAddButton_clicked - self.verticalLayout_52.count() ' +
                      str(self.verticalLayout_52.count()))
        if self.verticalLayout_52.count() < 10:
            filename, fileext = QtWidgets.QFileDialog.getOpenFileName(self,'Open an image','','All Files (*.*);;Images'  # @UnusedVariable
                                                   ' (*.jpg *.jpeg *.bmp *.png *.gif *.tiff)')
            if filename:
                add_image(self, filename)
                self.im_del[-1].clicked.connect(lambda: self.del_image())
                self.im_label[-1].clicked.connect(lambda: self.show_image())
        else:    
            alertBox = QtWidgets.QMessageBox()
            alertBox.about(self, "Warning", "You can't add more than 10 images.")

    
    @QtCore.pyqtSlot()
    def on_urlAddButton_clicked(self):
        logging.debug('mainwindow.py - on_urlAddButton_clicked - self.verticalLayout_52.count() ' +
                      str(self.verticalLayout_52.count()))
        if self.verticalLayout_52.count() < 10:
            x = QtGui.QCursor.pos().x()
            y = QtGui.QCursor.pos().y()
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
            alertBox = QtWidgets.QMessageBox()
            alertBox.about(self, "Warning", "You can't add more than 10 images.")
    
    
    def del_image(self):
        delete_image(self)
        
    
    def show_image(self):
        display_image(self)


    def closeEvent(self, event):
        logging.debug('mainwindow.py - closeEvent - self.modified ' + str(self.modified))
        if self.modified:
            result = self.make_onsave_msg_box("Close")
            if result == "iw_saveButton":
                self.save_document()
                shutil.rmtree(self.dirpath)
                logging.info('ASMM ' + _asmm_version + ' is closing ...')
                event.accept()
            elif result == "iw_nosaveButton":
                shutil.rmtree(self.dirpath)
                logging.info('ASMM ' + _asmm_version + ' is closing ...')
                event.accept()
            else:
                event.ignore()
        else:
            shutil.rmtree(self.dirpath)
            logging.info('ASMM ' + _asmm_version + ' is closing ...')
            self.close()


    def make_window_title(self):
        logging.debug('mainwindow.py - make_window_title - self.modified ' + str(self.modified) +
                      ' ; self.saved ' + str(self.saved))
        title_string = 'ASMM Creator v' + _asmm_version
        file_string = ''
        saved_string = ''
        modified_string = ''
        if self.out_file_name:
            file_string = ' - ' + self.out_file_name
        if not self.saved:
            saved_string = ' - unsaved'
        if self.modified:
            modified_string = ' - modified'
        title_string = title_string + file_string + saved_string + modified_string
        self.setWindowTitle(title_string)


    def set_modified(self):
        if not self.modified:
            self.modified = True
            self.saved = False
            self.make_window_title()


    def save_document(self, save_as=False):
        logging.debug('mainwindow.py - save_document - save_as ' + str(save_as))
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
        logging.debug('mainwindow.py - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDefaultSuffix('xml')
        out_file_name, _ = file_dialog.getSaveFileName(self, "Save XML File","!!!Flight identifier!!!_xxxxxxxxxx.xml"
                                                                  , filter='XML Files (*.xml)')
        logging.debug('mainwindow.py - get_file_name - out_file_name ' + out_file_name)
        return out_file_name


    def get_file_name_pdf(self):
        logging.debug('mainwindow.py - get_file_name_pdf')
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDefaultSuffix('pdf')
        out_file_name_pdf, _ = file_dialog.getSaveFileName(self, "Save PDF File", filter='PDF Files (*.pdf)')
        logging.debug('mainwindow.py - get_file_name_pdf - out_file_name_pdf ' + out_file_name_pdf)
        return out_file_name_pdf


    def reset_all_fields(self):
        logging.debug('mainwindow.py - reset_all_fields - starting ...')
        all_check_boxes = self.findChildren(QtWidgets.QCheckBox)
        for check_box in all_check_boxes:
            check_box.setCheckState(False)
        all_text_edits = self.findChildren(QtWidgets.QTextEdit)
        for widget in all_text_edits:
            widget.clear()
        all_line_edits = self.findChildren(QtWidgets.QLineEdit)
        for widget in all_line_edits:
            widget.clear()
        all_list_widgets = self.findChildren(QtWidgets.QListWidget)
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
        self.newAircraft_ln.hide()
        self.newAircraft_ln.setText('')
        self.newOperator_ln.hide()
        self.newOperator_ln.setText('')
        self.label_38.hide()
        self.label_39.hide()
        self.newCountry_lb.hide()
        self.newCountry_cb.hide()
        self.newCountry_cb.clear()
        self.newRegistration_lb.hide()
        self.newRegistration_ln.hide()
        self.newRegistration_ln.setText('')
        self.newManufacturer_lb.hide()
        self.newManufacturer_ln.hide()
        self.newManufacturer_ln.setText('')
        self.aircraft_cb.clear()
        self.aircraft_cb.setEnabled(False)
        self.location_cb.setCurrentIndex(0)
        self.detailList.clear()
        self.detailList.setEnabled(False)
        for i in reversed(range(0, len(self.images_pdf_path))):
            delete_image(self, i)
        objectsInit(self)
        self.make_window_title()
        logging.debug('mainwindow.py - reset_all_fields - finished')


    def make_onsave_msg_box(self, string):
        logging.debug('mainwindow.py - make_onsave_msg_box')
        self.presaveWindow = MyWarning(string)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.presaveWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.presaveWindow.setGeometry(x2, y2, w2, h2)
        self.presaveWindow.setMinimumSize(QtCore.QSize(450, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.setMaximumSize(QtCore.QSize(452, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.exec_()
        return self.presaveWindow.buttonName


    def open_file(self):
        logging.debug('mainwindow.py - open_file')
        out_file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self,'Open XML File','','XML Files (*.xml)')
        if out_file_name:
            read_asmm_xml(self, out_file_name)
            self.saved = True
            self.modified = False
            self.out_file_name = out_file_name
            self.make_window_title()
        logging.debug('mainwindow.py - open_file - self.saved ' + str(self.saved) + ' ; self.modified '
                      + str(self.modified) + ' ; self.out_file_name ' + str(self.out_file_name))


    def addListItem(self, title, label, listWidget, item_list):
        logging.debug('mainwindow.py - addListItem - title ' + str(title) + ' ; label ' + str(label))
        x = QtGui.QCursor.pos().x()
        y = QtGui.QCursor.pos().y()
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
            logging.debug('mainwindow.py - addListItem - text ' + self.siteWindow.ck_inputLine.text())


    def removeListItem(self, listWidget, item_list):
        logging.debug('mainwindow.py - removeListItem - item_list ' + str(item_list))
        selected_line = listWidget.currentRow()
        if selected_line >= 0:
            selected_item = listWidget.currentItem()
            item_list.remove(selected_item.text())
            listWidget.takeItem(selected_line)
            self.modified = True
            self.make_window_title()

    
    def toolButton_clicked(self):
        if self.sender().objectName() != '':
            logging.debug('mainwindow.py - toolButton_clicked - self.sender().objectName() ' + self.sender().objectName())
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
                    alertBox = QtWidgets.QMessageBox()
                    alertBox.about(self, "Warning", "You can't add more than 12 checkboxes.")
                    return
    
    
    def location_changed(self):
        logging.debug('mainwindow.py - location_changed - self.location_cb.currentText() ' + self.location_cb.currentText())
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
            self.detailList.addItem('Make a choice...')
            country_list = []
            for key, _ in self.new_country_code.items():
                country_list.append(key)
            self.detailList.addItems(sorted(country_list))
        elif self.location_cb.currentText() == "Oceans":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.oceans)
        elif self.location_cb.currentText() == "Regions":
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.regions)


    def fill_operator_rolebox(self):
        logging.debug('mainwindow.py - fill_operator_rolebox')
        unique_list = []
        for item in self.new_operators_aircraft:
            if item[0] not in unique_list:
                unique_list.append(item[0]) 
        self.operator_cb.clear()
        self.operator_cb.addItem('Make a choice...')
        self.operator_cb.addItem('Other...')
        self.operator_cb.addItems(sorted(unique_list, key=str.lower))


    def operator_changed(self):
        logging.debug('mainwindow.py - operator_changed - self.operator_cb.currentText() ' + self.operator_cb.currentText())
        if self.operator_cb.currentText() == "Make a choice...":
            self.newAircraft_ln.hide()
            self.newAircraft_ln.setText('')
            self.newOperator_ln.hide()
            self.newOperator_ln.setText('')
            self.label_38.hide()
            self.label_39.hide()
            self.newCountry_lb.hide()
            self.newCountry_cb.hide()
            self.newCountry_cb.clear()
            self.newRegistration_lb.hide()
            self.newRegistration_ln.hide()
            self.newRegistration_ln.setText('')
            self.newManufacturer_lb.hide()
            self.newManufacturer_ln.hide()
            self.newManufacturer_ln.setText('')
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
            self.newCountry_lb.show()
            self.newCountry_cb.show()
            self.newRegistration_lb.show()
            self.newRegistration_ln.show()
            self.newManufacturer_lb.show()
            self.newManufacturer_ln.show()
            self.newCountry_cb.addItem('Make a choice...')
            country_list = []
            for key, _ in self.new_country_code.items():
                country_list.append(key)
            self.newCountry_cb.addItems(sorted(country_list))
        else:
            self.newAircraft_ln.hide()
            self.newAircraft_ln.setText('')
            self.newOperator_ln.hide()
            self.newOperator_ln.setText('')
            self.label_38.hide()
            self.label_39.hide()
            self.newCountry_lb.hide()
            self.newCountry_cb.hide()
            self.newCountry_cb.clear()
            self.newRegistration_lb.hide()
            self.newRegistration_ln.hide()
            self.newRegistration_ln.setText('')
            self.newManufacturer_lb.hide()
            self.newManufacturer_ln.hide()
            self.newManufacturer_ln.setText('')
            self.aircraft_cb.clear()
            self.aircraft_cb.setEnabled(True)
            aircraft_list = []
            type_list =  []
            for i in range(len(self.new_operators_aircraft)):
                if self.operator_cb.currentText() == self.new_operators_aircraft[i][0]:
                    aircraft_list.append(self.new_operators_aircraft[i])
                    index = self.new_operators_aircraft[i][1].find(', ')
                    type_list.append(self.new_operators_aircraft[i][1][index + 2:])
            if len(aircraft_list) > 1:
                self.aircraft_cb.addItem("Make a choice...")
                counter_result = dict(Counter(type_list))
                for key, value in counter_result.items():
                    if value > 1:
                        for i in range(len(aircraft_list)):
                            if type_list[i] == key:
                                type_list[i] = type_list[i] + ' - ' + aircraft_list[i][2]
            self.aircraft_cb.addItems(sorted(type_list))


    def api_eufar_database_parsing(self):
        logging.debug('mainwindow.py - api_eufar_database_parsing')
        self.download_and_parse_objects = DownloadAndParseJSON()
        self.download_and_parse_objects.start()
        self.download_and_parse_objects.finished.connect(self.api_eufar_asmm_db_updating)
        
        
    def api_eufar_asmm_db_updating(self, val):
        logging.debug('mainwindow.py - api_eufar_asmm_db_updating')
        self.aircraft_db = val[0]
        self.project_db = val[1]     
        self.new_operators_aircraft = []
        for _, value in self.aircraft_db.items():
            self.new_operators_aircraft.append([value['operator'], value['manufacturer_and_aircraft_type'], 
                                                value['registration_number'], value['country']])
        current_operator = self.operator_cb.currentText()
        current_aircraft = self.aircraft_cb.currentText()
        operator_list = []
        for item in self.new_operators_aircraft:
            if item[0] not in operator_list:
                operator_list.append(item[0])
        self.operator_cb.clear()
        self.operator_cb.addItem('Make a choice...')
        self.operator_cb.addItem('Other...')
        self.operator_cb.addItems(sorted(operator_list))
        if current_operator != 'Make a choice...':
            operator_index = self.operator_cb.findText(current_operator)
            if operator_index == -1:
                self.operator_cb.setCurrentIndex(1)
                self.operator_changed()
                self.newOperator_ln.setText(current_operator)
                self.newAircraft_ln.setText(current_aircraft)
            else:
                self.operator_cb.setCurrentIndex(operator_index)
                self.operator_changed()
                aircraft_index = self.aircraft_cb.findText(current_aircraft)
                if aircraft_index == -1:
                    self.operator_cb.setCurrentIndex(1)
                    self.operator_changed()
                    self.newOperator_ln.setText(current_operator)
                    self.newAircraft_ln.setText(current_aircraft)
                else:
                    self.aircraft_cb.setCurrentIndex(aircraft_index)
        completer_list = []
        for key, value in self.project_db.items():
            completer_list.append(key)
        self.completer_model.setStringList(completer_list)
    
    
    def api_eufar_acronym_completer(self):
        logging.debug('mainwindow.py - api_eufar_acronym_completer')
        self.completer = QtWidgets.QCompleter()
        self.completer.popup().setStyleSheet("QListView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background-color: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QScrollBar:vertical {\n"
        "    border: 1px solid white;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "    width: 20px;\n"
        "    margin: 21px 0px 21px 0px;\n"
        "}\n"
        "\n"
        "QScrollBar::handle:vertical {\n"
        "    background-color: rgb(205, 205, 205);\n"
        "    min-height: 25px;\n"
        "}\n"
        "\n"
        "QScrollBar:handle:vertical:hover {\n"
        "    background-color: rgb(167, 167, 167);\n"
        "}\n"
        "\n"
        "QScrollBar::add-line:vertical {\n"
        "    border-top: 1px solid rgb(240,240,240);\n"
        "    border-left: 1px solid white;\n"
        "    border-right: 1px solid white;\n"
        "    border-bottom: 1px solid white;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "    height: 20px;\n"
        "    subcontrol-position: bottom;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::add-line:vertical:hover {\n"
        "    background-color: rgb(219, 219, 219);\n"
        "}\n"
        "\n"
        "QScrollBar::sub-line:vertical {\n"
        "    border-top: 1px solid white;\n"
        "    border-left: 1px solid white;\n"
        "    border-right: 1px solid white;\n"
        "    border-bottom: 1px solid rgb(240,240,240);\n"
        "    background-color: rgb(240, 240, 240);\n"
        "    height: 20px;\n"
        "    subcontrol-position: top;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::sub-line:vertical:hover {\n"
        "    background-color: rgb(219, 219, 219);\n"
        "}\n"
        "\n"
        "QScrollBar::up-arrow:vertical {\n"
        "    image: url(icons/up_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "}\n"
        "\n"
        "QScrollBar::up-arrow:vertical:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}\n"
        "\n"
        "QScrollBar::down-arrow:vertical {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "}\n"
        "\n"
        "QScrollBar::down-arrow:vertical:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}\n")
        self.projectAcronym_ln.setCompleter(self.completer)
        self.completer_model = QtCore.QStringListModel()
        self.completer.setModel(self.completer_model)
        self.completer.activated.connect(self.api_eufar_completer_function)
        
        
    def api_eufar_completer_function(self,val):
        logging.debug('mainwindow.py - api_eufar_completer_function - val ' + str(val))
        project = self.project_db[val]
        self.missionSci_ln.setText(project['leader'])
        try:
            platform = self.aircraft_db[project['aircraft']]
        except KeyError:
            platform = {}
        try:
            operator = platform['operator']
        except KeyError:
            operator = ''
        try:    
            aircraft = platform['manufacturer_and_aircraft_type']
            index = aircraft.find(', ')
            manufacturer = aircraft[: index]
            aircraft = aircraft[index + 2:]
        except KeyError:
            aircraft = ''
            manufacturer = ''
        try:
            registration = platform['registration_number']
        except KeyError:
            registration = ''
        try:
            country = platform['country']
            for key, value in self.new_country_code.items():
                if value == country:
                    country = key
                    break
        except KeyError:
            country = ''
        if operator or aircraft or manufacturer or registration or country:
            index = self.operator_cb.findText(operator)
            if index != -1:
                self.operator_cb.setCurrentIndex(index)
                self.operator_changed()
                index = self.aircraft_cb.findText(aircraft)
                if index != -1:
                    self.aircraft_cb.setCurrentIndex(index)
                else:
                    self.operator_cb.setCurrentIndex(1)
                    self.operator_changed()
                    self.newOperator_ln.setText(operator)
                    self.newAircraft_ln.setText(aircraft)
                    self.newRegistration_ln.setText(registration)
                    self.newManufacturer_ln.setText(manufacturer)
                    index = self.newCountry_cb.findText(country)
                    if index!= -1:
                        self.newCountry_cb.setCurrentIndex(index)
            else:
                self.operator_cb.setCurrentIndex(1)
                self.operator_changed()
                self.newOperator_ln.setText(operator)
                self.newAircraft_ln.setText(aircraft)
                self.newRegistration_ln.setText(registration)
                self.newManufacturer_ln.setText(manufacturer)
                index = self.newCountry_cb.findText(country)
                if index!= -1:
                    self.newCountry_cb.setCurrentIndex(index)

    
    def api_eufar_information(self):
        logging.debug('mainwindow.py - api_eufar_information')
        self.apiWindow = MyApi()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.apiWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.apiWindow.setGeometry(x2, y2, w2, h2)
        if platform.system() == 'Linux':
            x = 500
            y = self.apiWindow.sizeHint().height()
        elif platform.system() == 'Windows':
            x = 700
            y = 400
        else:
            x = 500
            y = self.apiWindow.sizeHint().height()
        self.apiWindow.setMinimumSize(QtCore.QSize(x, y))
        self.apiWindow.setMaximumSize(QtCore.QSize(x, y))
        self.apiWindow.exec_()
        return self.apiWindow.checkboxStatus


class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MyAbout')
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()
        
        
class MyLog(QtWidgets.QDialog, Ui_Changelog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MyLog')
        self.setupUi(self)
        self.log_txBrower.setPlainText(open("Documentation/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()
 
 
class MyStandard(QtWidgets.QDialog, Ui_aboutStandard):
    def __init__(self, aboutText):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MyStandard')
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close() 
 
 
class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, string):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MyWarning - string ' + string)
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            widget.clicked.connect(self.closeWindow)
        self.iw_nosaveButton.setText(string + " without saving")

    def closeWindow(self):
        self.buttonName = self.sender().objectName()
        self.close()
 
     
class MySite(QtWidgets.QDialog, Ui_Addsite):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MySite')
        self.setupUi(self)
        self.ck_cancelButton.clicked.connect(self.closeWindow)
        self.ck_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        if self.ck_inputLine.text():
            self.accept()
        

class MyURL(QtWidgets.QDialog, Ui_AddURL):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('mainwindow.py - MyAbout')
        self.setupUi(self)
        self.ck_cancelButton.clicked.connect(self.closeWindow)
        self.ck_submitButton.clicked.connect(self.submitBox)
        
    def closeWindow(self):
        self.close()

    def submitBox(self):
        self.accept()


class MyApi(QtWidgets.QDialog, Ui_apiWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('button_functions.py - MyInfo')
        self.setupUi(self)
        self.iw_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.checkboxStatus = self.checkBox.isChecked()
        self.close()



class DownloadAndParseJSON(Qt.QThread):
    finished = QtCore.pyqtSignal(list)
    def __init__(self):
        Qt.QThread.__init__(self)
        logging.debug('mainwindow.py - DownloadAndParseJSON - starting ...')
        self.url_list = ['http://eufar.net/api/json/ta/open/aircraft/', 
                         'http://eufar.net/api/sad89712hhdsa89yp1/json/projects/']
        self.db_list = []

    def run(self):   
        for url in self.url_list:
            dict_tmp = {}
            try:
                logging.debug('mainwindow.py - DownloadAndParseJSON - ' + url + ' running ...')
                req = requests.get(url=url)
                json_object = req.json()
                for item in json_object:
                    dict_tmp[item['acronym']] = dict(item)
                self.db_list.append(dict_tmp)
            except Exception:
                self.db_list.append(dict_tmp)
                logging.error('mainwindow.py - DownloadAndParseJSON - ' + url + ' error in connexion or json object')
        self.finished.emit(self.db_list)
        
    def stop(self):
        self.terminate()
