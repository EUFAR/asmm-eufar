import datetime
import xml.dom.minidom
import logging
from PyQt5 import QtCore, QtWidgets
from functions.button_functions import add_read


NAMESPACE_URI = 'http://www.eufar.net/ASMM'

def create_asmm_xml(self, out_file_name):
    logging.debug('asmm_xml.py - create_asmm_xml - out_file_name ' + out_file_name)
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
    add_element(doc, "Date", flightInformation, self.date_dt.date().toString(QtCore.Qt.ISODate))
    add_element(doc, "ProjectAcronym", flightInformation, self.projectAcronym_ln.text())
    add_element(doc, "MissionScientist", flightInformation, self.missionSci_ln.text())
    add_element(doc, "FlightManager", flightInformation, self.flightManager_ln.text())
    operator = self.operator_cb.currentText()
    aircraft = self.aircraft_cb.currentText()
    country = ''
    manufacturer = ''
    registration = ''
    if operator == 'Other...':
        operator = self.newOperator_ln.text()
        aircraft = self.newAircraft_ln.text()
        registration = self.newRegistration_ln.text()
        manufacturer = self.newManufacturer_ln.text()
        if self.newCountry_cb.currentText() != 'Make a choice...':
            country = self.newCountry_cb.currentText()
    elif operator != 'Make a choice...':
        if aircraft != 'Make a choice...':
            index = -1
            index = aircraft.find(' - ')
            if (index != -1):
                registration = aircraft[index + 3:]
                if len(registration) > 3:
                    aircraft = aircraft[0:index]
            for i in range(len(self.new_operators_aircraft)):
                if registration != '' and len(registration) > 3:
                    if registration == self.new_operators_aircraft[i][2]:
                        index = self.new_operators_aircraft[i][1].find(', ');
                        manufacturer = self.new_operators_aircraft[i][1][: index]
                        country = self.new_operators_aircraft[i][3]
                        break
                else:
                    index = self.new_operators_aircraft[i][1].find(', ');
                    aircraft_from_table = self.new_operators_aircraft[i][1][index + 2:]
                    if aircraft == aircraft_from_table:
                        manufacturer = self.new_operators_aircraft[i][1][: index]
                        country = self.new_operators_aircraft[i][3]
                        registration = self.new_operators_aircraft[i][2]
                        break
        else:
            aircraft = ''
    else:
        operator = ''
        aircraft = ''
    for key, value in self.new_country_code.items():
        if value == country:
            country = key
            break
    add_element(doc, "Platform", flightInformation, aircraft)
    add_element(doc, "Operator", flightInformation, operator)
    add_element(doc, "OperatorCountry", flightInformation, country)
    add_element(doc, "Manufacturer", flightInformation, manufacturer)
    add_element(doc, "RegistrationNumber", flightInformation, registration)
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
            if isinstance(self.gridLayout_5.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_5.itemAt(i).widget().isChecked():
                    add_element(doc,"SA_User", scientificAims, self.gridLayout_5.itemAt(i).widget().
                                text())
    add_element(doc, "SA_Other", scientificAims, self.SAOtherTextBox.toPlainText())


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
            if isinstance(self.gridLayout_8.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_8.itemAt(i).widget().isChecked():
                    add_element(doc,"GR_User", geographicalRegion, self.gridLayout_8.itemAt(i).
                                widget().text())
    add_element(doc, "GR_Other", geographicalRegion, self.GROtherTextBox.toPlainText())


    ############################
    # Atmospheric Features
    ############################
    atmosphericFeatures = add_element(doc, "AtmosFeatures", doc_root)
    add_check_elements(doc, self.atmospheric_features_check_dict, "AF_Code", atmosphericFeatures)
    if self.af_ck_list:
        for i in range(self.gridLayout_9.count()):
            if isinstance(self.gridLayout_9.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_9.itemAt(i).widget().isChecked():
                    add_element(doc,"AF_User", atmosphericFeatures, self.gridLayout_9.itemAt(i).
                                widget().text())
    add_element(doc, "AF_Other", atmosphericFeatures, self.AFOtherTextBox.toPlainText())


    ############################
    # Cloud Types
    ############################
    cloudTypes = add_element(doc, "CloudTypes", doc_root)
    add_check_elements(doc, self.cloud_types_check_dict, "CT_Code", cloudTypes)
    if self.ct_ck_list:
        for i in range(self.gridLayout_10.count()):
            if isinstance(self.gridLayout_10.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_10.itemAt(i).widget().isChecked():
                    add_element(doc,"CT_User", cloudTypes, self.gridLayout_10.itemAt(i).widget().
                                text())
    add_element(doc, "CT_Other", cloudTypes, self.CTOtherTextBox.toPlainText())


    ############################
    # Particles Sampled
    ############################
    particlesSampled = add_element(doc, "ParticlesSampled", doc_root)
    add_check_elements(doc, self.particles_sampled_check_dict, "PS_Code", particlesSampled)
    if self.ps_ck_list:
        for i in range(self.gridLayout_11.count()):
            if isinstance(self.gridLayout_11.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_11.itemAt(i).widget().isChecked():
                    add_element(doc,"PS_User", particlesSampled, self.gridLayout_11.itemAt(i).
                                widget().text())
    add_element(doc, "PS_Other", particlesSampled, self.PSOtherTextBox.toPlainText())


    ############################
    # Surfaces Overflown
    ############################
    surfacesOverflown = add_element(doc, "SurfacesOverflown", doc_root)
    add_check_elements(doc, self.surfaces_overflown_check_dict, "SO_Code", surfacesOverflown)
    if self.so_ck_list:
        for i in range(self.gridLayout_13.count()):
            if isinstance(self.gridLayout_13.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_13.itemAt(i).widget().isChecked():
                    add_element(doc,"SO_User", surfacesOverflown, self.gridLayout_13.itemAt(i).
                                widget().text())
    add_element(doc, "SO_Other", surfacesOverflown, self.SOOtherTextBox.toPlainText())


    ############################
    # Altitude Ranges
    ############################
    altitudeRanges = add_element(doc, "AltitudeRanges", doc_root)
    add_check_elements(doc, self.altitude_ranges_check_dict, "AR_Code", altitudeRanges)
    if self.ar_ck_list:
        for i in range(self.gridLayout_14.count()):
            if isinstance(self.gridLayout_14.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_14.itemAt(i).widget().isChecked():
                    add_element(doc,"AR_User", altitudeRanges, self.gridLayout_14.itemAt(i).
                                widget().text())
    add_element(doc, "AR_Other", altitudeRanges, self.AROtherTextBox.toPlainText())


    ############################
    # Flight Types
    ############################
    flightTypes = add_element(doc, "FlightTypes", doc_root)
    add_check_elements(doc, self.flight_types_check_dict, "FT_Code", flightTypes)
    if self.fm_ck_list:
        for i in range(self.gridLayout_15.count()):
            if isinstance(self.gridLayout_15.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_15.itemAt(i).widget().isChecked():
                    add_element(doc,"FT_User", flightTypes, self.gridLayout_15.itemAt(i).widget().
                                text())
    add_element(doc, "FT_Other", flightTypes, self.FTOtherTextBox.toPlainText())


    ############################
    # Satellite coordination
    ############################
    satelliteCoordination = add_element(doc, "SatelliteCoordination", doc_root)
    add_check_elements(doc, self.satellite_coordination_check_dict, "SC_Code", satelliteCoordination)
    if self.sc_ck_list:
        for i in range(self.gridLayout_25.count()):
            if isinstance(self.gridLayout_25.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_25.itemAt(i).widget().isChecked():
                    add_element(doc,"SC_User", satelliteCoordination, self.gridLayout_25.itemAt(i).
                                widget().text())
    add_element(doc, "SC_Other", satelliteCoordination, self.SCOtherTextBox.toPlainText())


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
    logging.debug('asmm_xml.py - create_asmm_xml - file created successfully')


def read_asmm_xml(self, in_file_name):
    logging.debug('asmm_xml.py - read_asmm_xml - out_file_name ' + in_file_name)
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
    self.date_dt.setDate(QtCore.QDate.fromString(date, QtCore.Qt.ISODate))
    set_text_value(self.projectAcronym_ln, flightInformation, "ProjectAcronym")
    set_text_value(self.missionSci_ln, flightInformation, "MissionScientist")
    set_text_value(self.flightManager_ln, flightInformation, "FlightManager")
    operator = get_element_value(flightInformation, "Operator")
    aircraft = get_element_value(flightInformation, "Platform")
    registration = get_element_value(flightInformation, "RegistrationNumber")
    aircraft_found = False
    if registration:
        for i in range(len(self.new_operators_aircraft)):
            if registration == self.new_operators_aircraft[i][2]:
                aircraft_found = True
                self.operator_cb.setCurrentIndex(self.operator_cb.findText(operator))
                self.operator_changed()
                index = self.aircraft_cb.findText(aircraft)
                if index != -1:
                    self.aircraft_cb.setCurrentIndex(index)
                else:
                    index = self.aircraft_cb.findText(aircraft + ' - ' + registration)
                    self.aircraft_cb.setCurrentIndex(index)
                break
        if not aircraft_found:
            self.operator_cb.setCurrentIndex(1)
            self.operator_changed()
            self.newOperator_ln.setText(operator)
            self.newAircraft_ln.setText(aircraft)
            self.newRegistration_ln.setText(registration)
            self.newManufacturer_ln.setText(get_element_value(flightInformation, "Manufacturer"))
            if get_element_value(flightInformation, "OperatorCountry"):
                self.newCountry_cb.setCurrentIndex(self.newCountry_cb.findText(get_element_value(flightInformation, "OperatorCountry"))) 
    else:
        self.operator_cb.setCurrentIndex(1)
        self.operator_changed()
        self.newOperator_ln.setText(operator)
        self.newAircraft_ln.setText(aircraft)
        self.newRegistration_ln.setText(registration)
        self.newManufacturer_ln.setText(get_element_value(flightInformation, "Manufacturer"))
        if get_element_value(flightInformation, "OperatorCountry"):
            index = self.newCountry_cb.findText(get_element_value(flightInformation, "OperatorCountry"))
            if index != -1:
                self.newCountry_cb.setCurrentIndex(index) 
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
    
    logging.debug('asmm_xml.py - create_asmm_xml - file read successfully')


def get_element(parent, element_name):
    logging.debug('asmm_xml.py - get_element - parent ' + str(parent) + ' ; element_name ' + str(element_name))
    return parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)[0]


def get_element_value(parent, element_name):
    logging.debug('asmm_xml.py - get_element_value - parent ' + str(parent) + ' ; element_name ' + str(element_name))
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    if elements:
        element = elements[0]
        nodes = element.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                return node.data.strip()


def get_element_values(parent, element_name):
    logging.debug('asmm_xml.py - get_element_values - parent ' + str(parent) + ' ; element_name ' + str(element_name))
    value_list = []
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    for element in elements:
        value_list.append(element.childNodes[0].data.strip())
    return value_list


def set_check_values(check_dict, parent, element_name):
    logging.debug('asmm_xml.py - set_check_values - parent ' + str(parent) + ' ; element_name ' + str(element_name))
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    for element in elements:
        check_widget = find_key(check_dict, element.childNodes[0].data.strip())
        if check_widget is not None:
            check_widget.setChecked(True)


def set_text_value(text_widget, parent, element_name):
    logging.debug('asmm_xml.py - set_text_value - parent ' + str(parent) + ' ; element_name ' + str(element_name))
    node_data = get_element_value(parent, element_name)
    if node_data:
        text_widget.setText(node_data)
        
        
def set_text_value_coord(self, text_widget, parent, element_name):
    logging.debug('asmm_xml.py - set_text_value_coord - parent ' + str(parent) + ' ; element_name ' + str(element_name))
    node_data = get_element_value(parent, element_name)
    if node_data:
        text_widget.setText(clean_coordinate_string(self, node_data))        


def add_element(doc, element_name, parent, value=None):
    logging.debug('asmm_xml.py - add_element - parent ' + str(parent) + ' ; element_name ' + str(element_name) + ' ; value ' + str(value))
    new_element = doc.createElementNS(NAMESPACE_URI, "asmm:" + element_name)
    if value:
        new_text = doc.createTextNode(value)
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element


def add_check_elements(doc, check_dict, code_name, parent):
    logging.debug('asmm_xml.py - add_check_elements - parent ' + str(parent) + ' ; element_name ' + str(code_name))
    for key, val in iter(check_dict.items()):
        if key.isChecked():
            add_element(doc, code_name, parent, val)


def find_key(dic, val):
    return [k for k, v in iter(dic.items()) if v == val][0]
    
    
def clean_coordinate_string(self, string):
    logging.debug('asmm_xml.py - clean_coordinate_string - string ' + string)
    for key, val in self.coordinate_units_list.items():
        try:
            string = string[:string.index(key)]
            if val < 0:
                string = '-' + string
            break
        except ValueError:
            pass
    return string
    
    