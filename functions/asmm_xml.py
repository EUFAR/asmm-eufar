# -*- coding: utf-8 -*-

import datetime
import xml.dom.minidom
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QCheckBox
from functions.button_functions import add_read


NAMESPACE_URI = 'http://www.eufar.net/ASMM'

def create_asmm_xml(self, out_file_name):
  
    doc = xml.dom.minidom.Document()
    doc_root = add_element(doc, "MissionMetadata", doc)
    doc_root.setAttribute("xmlns:asmm", NAMESPACE_URI)
    current_date = datetime.date.isoformat(datetime.date.today())
    if not self.create_date:
        self.create_date = current_date
    add_element(doc, "CreationDate", doc_root, self.create_date)
    add_element(doc, "RevisionDate", doc_root, current_date)


    ############################
    # Flight Information
    ############################
    flightInformation = add_element(doc, "FlightInformation", doc_root)
    add_element(doc, "FlightNumber", flightInformation, self.flightNumber_ln.text())
    add_element(doc, "Date", flightInformation, self.date_dt.date().toString(Qt.ISODate))
    add_element(doc, "ProjectAcronym", flightInformation, self.projectAcronym_ln.text())
    add_element(doc, "MissionScientist", flightInformation, self.missionSci_ln.text())
    add_element(doc, "FlightManager", flightInformation, self.flightManager_ln.text())
    operator = ""
    aircraft = ""
    if self.operator_cb.currentText() == "Other...":
        operator = self.newAircraft_ln.text()
        aircraft = self.newOperator_ln.text()
    elif self.operator_cb.currentText() != "Make a choice...":
        for i in range(len(self.operators_aircraft)):
            if self.operator_cb.currentText() == self.operators_aircraft[i][0]:
                operator = self.operators_aircraft[i][2]
                break
        for i in range(len(self.operators_aircraft)):
            if self.aircraft_cb.currentText() == self.operators_aircraft[i][1]:
                aircraft = self.operators_aircraft[i][3]
                break
    add_element(doc, "Platform", flightInformation, aircraft)
    add_element(doc, "Operator", flightInformation, operator)
    if self.location_cb.currentText() == "Make a choice...":
        add_element(doc, "Localisation", flightInformation, "")
    elif self.detailList.currentText() == "Make a choice...":
        add_element(doc, "Localisation", flightInformation, "")
    else:
        add_element(doc, "Localisation", flightInformation, self.detailList.currentText())


    ###########################
    # Metadata Contact Info
    ###########################
    contactInfo = add_element(doc, "ContactInfo", doc_root)
    add_element(doc, "ContactName", contactInfo, self.contactName_ln.text())
    if self.contact_cb.currentText() == 'Make a choice...':
        add_element(doc, "ContactRole", contactInfo, '')
    else:
        add_element(doc, "ContactRole", contactInfo, self.contact_cb.currentText())
    add_element(doc, "ContactEmail", contactInfo, self.contactEmail_ln.text())


    ############################
    # Scientific Aims
    ############################
    scientificAims = add_element(doc, "ScientificAims", doc_root)
    add_check_elements(doc, self.scientific_aims_check_dict, "SA_Code", scientificAims)
    if self.sa_ck_list:
        for i in range(self.gridLayout_5.count()):
            if isinstance(self.gridLayout_5.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_5.itemAt(i).widget().isChecked():
                    add_element(doc,"SA_User", scientificAims, self.gridLayout_5.itemAt(i).widget().
                                text())
    add_comment_element(doc, "SA_Other", scientificAims, self.SAOtherTextBox.toPlainText())


    ############################
    # Geographical Region
    ############################
    geographicalRegion = add_element(doc, "GeographicalRegion", doc_root)
    geographicBoundingBox = add_element(doc, "GeographicBoundingBox", geographicalRegion)
    add_element(doc, "westBoundLongitude", geographicBoundingBox, self.westBoundLongitudeLine.text())
    add_element(doc, "eastBoundLongitude", geographicBoundingBox, self.eastBoundLongitudeLine.text())
    add_element(doc, "northBoundLatitude", geographicBoundingBox, self.northBoundLatitudeLine.text())
    add_element(doc, "southBoundLatitude", geographicBoundingBox, self.southBoundLatitudeLine.text())
    add_element(doc, "minAltitude", geographicBoundingBox, self.minAltitudeLine.text())
    add_element(doc, "maxAltitude", geographicBoundingBox, self.maxAltitudeLine.text())
    add_check_elements(doc, self.geographical_region_check_dict, "GR_Code", geographicalRegion)
    if self.gr_ck_list:
        for i in range(self.gridLayout_8.count()):
            if isinstance(self.gridLayout_8.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_8.itemAt(i).widget().isChecked():
                    add_element(doc,"GR_User", geographicalRegion, self.gridLayout_8.itemAt(i).
                                widget().text())
    add_comment_element(doc, "GR_Other", geographicalRegion, self.GROtherTextBox.toPlainText())


    ############################
    # Atmospheric Features
    ############################
    atmosphericFeatures = add_element(doc, "AtmosFeatures", doc_root)
    add_check_elements(doc, self.atmospheric_features_check_dict, "AF_Code", atmosphericFeatures)
    if self.af_ck_list:
        for i in range(self.gridLayout_9.count()):
            if isinstance(self.gridLayout_9.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_9.itemAt(i).widget().isChecked():
                    add_element(doc,"AF_User", atmosphericFeatures, self.gridLayout_9.itemAt(i).
                                widget().text())
    add_comment_element(doc, "AF_Other", atmosphericFeatures, self.AFOtherTextBox.toPlainText())


    ############################
    # Cloud Types
    ############################
    cloudTypes = add_element(doc, "CloudTypes", doc_root)
    add_check_elements(doc, self.cloud_types_check_dict, "CT_Code", cloudTypes)
    if self.ct_ck_list:
        for i in range(self.gridLayout_10.count()):
            if isinstance(self.gridLayout_10.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_10.itemAt(i).widget().isChecked():
                    add_element(doc,"CT_User", cloudTypes, self.gridLayout_10.itemAt(i).widget().
                                text())
    add_comment_element(doc, "CT_Other", cloudTypes, self.CTOtherTextBox.toPlainText())


    ############################
    # Particles Sampled
    ############################
    particlesSampled = add_element(doc, "ParticlesSampled", doc_root)
    add_check_elements(doc, self.particles_sampled_check_dict, "PS_Code", particlesSampled)
    if self.ps_ck_list:
        for i in range(self.gridLayout_11.count()):
            if isinstance(self.gridLayout_11.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_11.itemAt(i).widget().isChecked():
                    add_element(doc,"PS_User", particlesSampled, self.gridLayout_11.itemAt(i).
                                widget().text())
    add_comment_element(doc, "PS_Other", particlesSampled, self.PSOtherTextBox.toPlainText())


    ############################
    # Surfaces Overflown
    ############################
    surfacesOverflown = add_element(doc, "SurfacesOverflown", doc_root)
    add_check_elements(doc, self.surfaces_overflown_check_dict, "SO_Code", surfacesOverflown)
    if self.so_ck_list:
        for i in range(self.gridLayout_13.count()):
            if isinstance(self.gridLayout_13.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_13.itemAt(i).widget().isChecked():
                    add_element(doc,"SO_User", surfacesOverflown, self.gridLayout_13.itemAt(i).
                                widget().text())
    add_comment_element(doc, "SO_Other", surfacesOverflown, self.SOOtherTextBox.toPlainText())


    ############################
    # Altitude Ranges
    ############################
    altitudeRanges = add_element(doc, "AltitudeRanges", doc_root)
    add_check_elements(doc, self.altitude_ranges_check_dict, "AR_Code", altitudeRanges)
    if self.ar_ck_list:
        for i in range(self.gridLayout_14.count()):
            if isinstance(self.gridLayout_14.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_14.itemAt(i).widget().isChecked():
                    add_element(doc,"AR_User", altitudeRanges, self.gridLayout_14.itemAt(i).
                                widget().text())
    add_comment_element(doc, "AR_Other", altitudeRanges, self.AROtherTextBox.toPlainText())


    ############################
    # Flight Types
    ############################
    flightTypes = add_element(doc, "FlightTypes", doc_root)
    add_check_elements(doc, self.flight_types_check_dict, "FT_Code", flightTypes)
    if self.fm_ck_list:
        for i in range(self.gridLayout_15.count()):
            if isinstance(self.gridLayout_15.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_15.itemAt(i).widget().isChecked():
                    add_element(doc,"FT_User", flightTypes, self.gridLayout_15.itemAt(i).widget().
                                text())
    add_comment_element(doc, "FT_Other", flightTypes, self.FTOtherTextBox.toPlainText())


    ############################
    # Satellite coordination
    ############################
    satelliteCoordination = add_element(doc, "SatelliteCoordination", doc_root)
    add_check_elements(doc, self.satellite_coordination_check_dict, "SC_Code", satelliteCoordination)
    if self.sc_ck_list:
        for i in range(self.gridLayout_25.count()):
            if isinstance(self.gridLayout_25.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_25.itemAt(i).widget().isChecked():
                    add_element(doc,"SC_User", satelliteCoordination, self.gridLayout_25.itemAt(i).
                                widget().text())
    add_comment_element(doc, "SC_Other", satelliteCoordination, self.SCOtherTextBox.toPlainText())


    ############################
    # Surface Observations
    ############################
    surfaceObs = add_element(doc, "SurfaceObs", doc_root)
    for item in self.ground_site_list:
        add_element(doc, "GroundSite", surfaceObs, item)
    for item in self.research_vessel_list:
        add_element(doc, "ResearchVessel", surfaceObs, item)
    for item in self.arm_site_list:
        add_element(doc, "ArmSite", surfaceObs, item)
    for item in self.arm_mobile_list:
        add_element(doc, "ArmMobile", surfaceObs, item)
        
    ############################
    # Other Comments
    ############################
    if self.OtherCommentsTextBox.toPlainText():
        add_element(doc, "OtherComments", doc_root, self.OtherCommentsTextBox.toPlainText())
   
   
    ############################
    # File Creation
    ############################
    f = open(out_file_name, 'w')
    f.write(doc.toprettyxml())
    f.close()
    self.saved = True
    self.modified = False


def read_asmm_xml(self, in_file_name):

    self.reset_all_fields()
    f = open(in_file_name, 'r')
    doc = xml.dom.minidom.parse(f)


    ############################
    # Flight Information
    ############################
    self.create_date = get_element_value(doc, "CreationDate")
    flightInformation = get_element(doc, "FlightInformation")
    set_text_value(self.flightNumber_ln, flightInformation, "FlightNumber")
    date = get_element_value(flightInformation, "Date")
    self.date_dt.setDate(QDate.fromString(date, Qt.ISODate))
    set_text_value(self.projectAcronym_ln, flightInformation, "ProjectAcronym")
    set_text_value(self.missionSci_ln, flightInformation, "MissionScientist")
    set_text_value(self.flightManager_ln, flightInformation, "FlightManager")
    operator = get_element_value(flightInformation, "Operator")
    aircraft = get_element_value(flightInformation, "Platform")
    operator_combo = None
    aircraft_combo = None
    for i in range(len(self.operators_aircraft)):
        if operator == self.operators_aircraft[i][2]:
            operator_combo = self.operators_aircraft[i][0]
    for i in range(len(self.operators_aircraft)):
        if aircraft == self.operators_aircraft[i][3]:
            aircraft_combo = self.operators_aircraft[i][1]
            break
    if operator_combo == None:
        self.operator_cb.setCurrentIndex(self.operator_cb.findText("Other..."))
        operator_read(self)
        self.newOperator_ln.setText(operator)
        self.newAircraft_ln.setText(aircraft)
    else:
        if aircraft_combo == None and aircraft != None:
            self.operator_cb.setCurrentIndex(self.operator_cb.findText("Other..."))
            operator_read(self)
            self.newOperator_ln.setText(operator)
            self.newAircraft_ln.setText(aircraft)
        else:
            self.operator_cb.setCurrentIndex(self.operator_cb.findText(operator_combo))
            self.aircraft_cb.clear()
            self.aircraft_cb.addItem("Make a choice...")
            self.aircraft_cb.setEnabled(True)
            for i in range(len(self.operators_aircraft)):
                if self.operator_cb.currentText() == self.operators_aircraft[i][0]:
                    self.aircraft_cb.addItem(self.operators_aircraft[i][1])
            if self.aircraft_cb.count() < 3:
                self.aircraft_cb.removeItem(0)
            if aircraft == None:
                self.aircraft_cb.setCurrentIndex(0)
            else:
                self.aircraft_cb.setCurrentIndex(self.aircraft_cb.findText(aircraft_combo))

    combo_text = get_element_value(flightInformation, "Localisation")
    if combo_text != None:
        if combo_text in self.countries:
            self.location_cb.setCurrentIndex(self.location_cb.findText("Countries"))
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.countries)
            self.detailList.setCurrentIndex(self.detailList.findText(combo_text))
        elif combo_text in self.continents:
            self.location_cb.setCurrentIndex(self.location_cb.findText("Continents"))
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.continents)
            self.detailList.setCurrentIndex(self.detailList.findText(combo_text))
        elif combo_text in self.oceans:
            self.location_cb.setCurrentIndex(self.location_cb.findText("Oceans"))
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.oceans)
            self.detailList.setCurrentIndex(self.detailList.findText(combo_text))
        elif combo_text in self.regions:
            self.location_cb.setCurrentIndex(self.location_cb.findText("Regions"))
            self.detailList.clear()
            self.detailList.setEnabled(True)
            self.detailList.addItems(self.regions)
            self.detailList.setCurrentIndex(self.detailList.findText(combo_text))


    #############################
    # Metadata Contact Info
    #############################
    contactInfo = get_element(doc, "ContactInfo")
    set_text_value(self.contactName_ln, contactInfo, "ContactName")
    set_text_value(self.contactEmail_ln, contactInfo, "ContactEmail")
    combo_text = get_element_value(contactInfo, "ContactRole")
    if combo_text != None:
        self.contact_cb.setCurrentIndex(self.contact_cb.findText(combo_text))


    #############################
    # Scientific Aims
    #############################
    scientificAims = get_element(doc, "ScientificAims")
    try:
        set_check_values(self.scientific_aims_check_dict, scientificAims, "SA_Code")
    except IndexError:
        set_check_values(self.old_scientific_aims_check_dict, scientificAims, "SA_Code")
    set_text_value(self.SAOtherTextBox, scientificAims, "SA_Other")
    values = get_element_values(scientificAims, "SA_User")
    for item in values:
        add_read(self, "SA", item)
    

    #############################
    # Geographical Region
    #############################
    geographicalRegion = get_element(doc, "GeographicalRegion")
    geographicBoundingBox = get_element(geographicalRegion, "GeographicBoundingBox")
    set_text_value_coord(self, self.westBoundLongitudeLine, geographicBoundingBox, "westBoundLongitude")
    set_text_value_coord(self, self.eastBoundLongitudeLine, geographicBoundingBox, "eastBoundLongitude")
    set_text_value_coord(self, self.northBoundLatitudeLine, geographicBoundingBox, "northBoundLatitude")
    set_text_value_coord(self, self.southBoundLatitudeLine, geographicBoundingBox, "southBoundLatitude")
    set_text_value_coord(self, self.minAltitudeLine, geographicBoundingBox, "minAltitude")
    set_text_value_coord(self, self.maxAltitudeLine, geographicBoundingBox, "maxAltitude")
    try:
        set_check_values(self.geographical_region_check_dict, geographicalRegion, "GR_Code")
    except IndexError:
        set_check_values(self.old_geographical_region_check_dict, geographicalRegion, "GR_Code")
    set_text_value(self.GROtherTextBox, geographicalRegion, "GR_Other")
    values = get_element_values(geographicalRegion, "GR_User")
    for item in values:
        add_read(self, "GR", item)
    

    #############################
    # Atmospheric Features
    #############################
    atmosphericFeatures = get_element(doc, "AtmosFeatures")
    try:
        set_check_values(self.atmospheric_features_check_dict, atmosphericFeatures, "AF_Code")
    except IndexError:
        set_check_values(self.old_atmospheric_features_check_dict, atmosphericFeatures, "AF_Code")
    set_text_value(self.AFOtherTextBox, atmosphericFeatures, "AF_Other")
    values = get_element_values(atmosphericFeatures, "AF_User")
    for item in values:
        add_read(self, "AF", item)


    #############################
    # Cloud Types
    #############################
    cloudTypes = get_element(doc, "CloudTypes")
    try:
        set_check_values(self.cloud_types_check_dict, cloudTypes, "CT_Code")
    except IndexError:
        set_check_values(self.old_cloud_types_check_dict, cloudTypes, "CT_Code")
    set_text_value(self.CTOtherTextBox, cloudTypes, "CT_Other")
    values = get_element_values(cloudTypes, "CT_User")
    for item in values:
        add_read(self, "CT", item)
    

    #############################
    # Particles Sampled
    #############################
    particlesSampled = get_element(doc, "ParticlesSampled")
    try:
        set_check_values(self.particles_sampled_check_dict, particlesSampled, "PS_Code")
    except IndexError:
        set_check_values(self.old_particles_sampled_check_dict, particlesSampled, "PS_Code")
    set_text_value(self.PSOtherTextBox, particlesSampled, "PS_Other")
    values = get_element_values(particlesSampled, "PS_User")
    for item in values:
        add_read(self, "PS", item)
    

    #############################
    # Surfaces Overflown
    #############################
    surfacesOverflown = get_element(doc, "SurfacesOverflown")
    try:
        set_check_values(self.surfaces_overflown_check_dict, surfacesOverflown, "SO_Code")
    except IndexError:
        set_check_values(self.old_surfaces_overflown_check_dict, surfacesOverflown, "SO_Code")
    set_text_value(self.SOOtherTextBox, surfacesOverflown, "SO_Other")
    values = get_element_values(surfacesOverflown, "SO_User")
    for item in values:
        add_read(self, "SO", item)
    

    #############################
    # Altitude Ranges
    #############################
    altitudeRanges = get_element(doc, "AltitudeRanges")
    try:
        set_check_values(self.altitude_ranges_check_dict, altitudeRanges, "AR_Code")
    except IndexError:
        set_check_values(self.old_altitude_ranges_check_dict, altitudeRanges, "AR_Code")
    set_text_value(self.AROtherTextBox, altitudeRanges, "AR_Other")
    values = get_element_values(altitudeRanges, "AR_User")
    for item in values:
        add_read(self, "AR", item)
        
    
    #############################
    # Flight Types
    #############################
    flightTypes = get_element(doc, "FlightTypes")
    try:
        set_check_values(self.flight_types_check_dict, flightTypes, "FT_Code")
    except IndexError:
        set_check_values(self.old_flight_types_check_dict, flightTypes, "FT_Code")
    set_text_value(self.FTOtherTextBox, flightTypes, "FT_Other")
    values = get_element_values(flightTypes, "FT_User")
    for item in values:
        add_read(self, "FM", item)
    

    #############################
    # Satellite Coordination
    #############################
    satelliteCoordination = get_element(doc, "SatelliteCoordination")
    try:
        set_check_values(self.satellite_coordination_check_dict, satelliteCoordination, "SC_Code")
    except IndexError:
        set_check_values(self.old_satellite_coordination_check_dict, satelliteCoordination, "SC_Code")
    set_text_value(self.SCOtherTextBox, satelliteCoordination, "SC_Other")
    values = get_element_values(satelliteCoordination, "SC_User")
    for item in values:
        add_read(self, "SC", item)


    #############################
    # Surface Observations
    #############################
    surfaceObservations = get_element(doc, "SurfaceObs")
    self.ground_site_list = get_element_values(surfaceObservations, "GroundSite")
    self.groundListWidget.addItems(self.ground_site_list)
    self.research_vessel_list = get_element_values(surfaceObservations, "ResearchVessel")
    self.vesselListWidget.addItems(self.research_vessel_list)
    self.arm_site_list = get_element_values(surfaceObservations, "ArmSite")
    self.armListWidget.addItems(self.arm_site_list)
    self.arm_mobile_list = get_element_values(surfaceObservations, "ArmMobile")
    self.armMobileListWidget.addItems(self.arm_mobile_list)
    
    
    ##############################
    # Other Comments
    ##############################
    set_text_value(self.OtherCommentsTextBox, doc, "OtherComments")


def get_element(parent, element_name):
    return parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)[0]


def get_element_value(parent, element_name):
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    if elements:
        element = elements[0]
        nodes = element.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                return node.data.strip()


def get_element_values(parent, element_name):
    value_list = []
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    for element in elements:
        value_list.append(element.childNodes[0].data.strip())
    return value_list


def set_check_values(check_dict, parent, element_name):
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    for element in elements:
        check_widget = find_key(check_dict, element.childNodes[0].data.strip())
        if check_widget is not None:
            check_widget.setChecked(True)


def set_text_value(text_widget, parent, element_name):
    node_data = get_element_value(parent, element_name)
    if node_data:
        text_widget.setText(node_data)
        
        
def set_text_value_coord(self, text_widget, parent, element_name):
    node_data = get_element_value(parent, element_name)
    if node_data:
        text_widget.setText(clean_coordinate_string(self, node_data))        


def add_element(doc, element_name, parent, value=None):
    new_element = doc.createElementNS(NAMESPACE_URI, "asmm:" + element_name)
    if value:
        new_text = doc.createTextNode(value)
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element


def add_comment_element(doc, element_name, parent, value):
    if value:
        add_element(doc, element_name, parent, value)


def add_check_elements(doc, check_dict, code_name, parent):
    for key, val in iter(check_dict.items()):
        if key.isChecked():
            add_element(doc, code_name, parent, val)


def find_key(dic, val):
    return [k for k, v in iter(dic.items()) if v == val][0]


def operator_read(self):
    self.aircraft_cb.clear()
    self.aircraft_cb.addItem("Other...")
    self.aircraft_cb.setEnabled(True)
    self.newOperator_ln.show()
    self.newAircraft_ln.show()
    self.label_38.show()
    self.label_39.show()
    
    
def clean_coordinate_string(self, string):
    for key, val in self.coordinate_units_list.items():
        try:
            string = string[:string.index(key)]
            if val < 0:
                string = '-' + string
            break
        except ValueError:
            pass
    return string
    
    