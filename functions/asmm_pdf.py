# -*- coding: utf-8 -*-

import datetime
from PyQt5.QtCore import Qt
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors, utils
from functions.signs_and_figures import tick_2, square, semi_square
from PyQt5.QtWidgets import QCheckBox
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle


def create_asmm_pdf(self, out_file_name_pdf):
    
    # document creation
    docpdf = SimpleDocTemplate(out_file_name_pdf,
                               pagesize = A4,
                               rightMargin=30,
                               leftMargin=30,
                               topMargin=30,
                               bottomMargin=50)
    page_w, _ = A4
    
    # polices
    pdfmetrics.registerFont(TTFont('asmm', 'fonts/SourceSansPro-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('asmm_bold', 'fonts/SourceSansPro-Semibold.ttf'))
    pdfmetrics.registerFont(TTFont('asmm_italic', 'fonts/SourceSansPro-Italic.ttf'))


    # styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='report_title', fontName='asmm', fontSize=22, alignment=TA_CENTER, wordWrap = 'CJK'))
    styles.add(ParagraphStyle(name='date', fontName='asmm', fontSize=13, alignment=TA_RIGHT, wordWrap = 'CJK'))
    styles.add(ParagraphStyle(name='section_title', fontName='asmm_bold', fontSize=16, alignment=TA_LEFT, wordWrap = 'CJK'))
    styles.add(ParagraphStyle(name='asmm', fontName='asmm', fontSize=12, leading=14, wordWrap = 'CJK'))
    styles.add(ParagraphStyle(name='asmm_justify', fontName='asmm', fontSize=12, alignment=TA_JUSTIFY, leading=14, wordWrap = 'CJK'))
    styles.add(ParagraphStyle(name='checkbox_title', fontName='asmm_bold', fontSize=12, leading=14, wordWrap = 'CJK'))
    styles.add(ParagraphStyle(name='figure_number', fontName='asmm_bold', fontSize=12, alignment=TA_RIGHT, leading=14, wordWrap = 'CJK'))
    styles.add(ParagraphStyle(name='figure_caption', fontName='asmm_italic', fontSize=12, alignment=TA_LEFT, leading=14, wordWrap = 'CJK'))


    # title and date
    story = []
    story.append(Paragraph(create_date_string(), styles["date"]))
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('Airborne Science Mission Metadata<br/><br/>Report', styles["report_title"]))
    sq = square(90, -20, 342, 60, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/><br/><br/>', styles["asmm"]))
    
    
    # flight information
    proj_acronyme = Paragraph(self.projectAcronym_ln.text(),styles["asmm"])
    date = Paragraph(self.date_dt.date().toString(Qt.ISODate),styles["asmm"])
    flight_number = Paragraph(self.flightNumber_ln.text(),styles["asmm"])
    mission_scientist = Paragraph(self.missionSci_ln.text(),styles["asmm"])
    flight_manager = Paragraph(self.flightManager_ln.text(),styles["asmm"])
    if self.aircraft_cb.currentText() == "Make a choice...":
        aircraft = Paragraph("",styles["asmm"])
    elif self.aircraft_cb.currentText() == "Other...":
        aircraft = Paragraph(self.newAircraft_ln.text(),styles["asmm"])
    else:
        aircraft = Paragraph(self.aircraft_cb.currentText(),styles["asmm"])
    if self.operator_cb.currentText() == "Make a choice...":
        operator = Paragraph("",styles["asmm"])
    elif self.operator_cb.currentText() == "Other...":
        operator = Paragraph(self.newOperator_ln.text(),styles["asmm"])
    else:
        operator = Paragraph(self.operator_cb.currentText(),styles["asmm"])
    if self.location_cb.currentText() == "Make a choice..." or self.detailList.currentText() == "Make a choice...":
        country = Paragraph("",styles["asmm"])
    else:
        country = Paragraph(self.detailList.currentText(),styles["asmm"])
    story.append(Paragraph('Flight Information', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data= [[Paragraph('Project acronym:',styles["asmm"]), proj_acronyme, Paragraph('Flight manager:',styles["asmm"]), flight_manager],
           [Paragraph('Date:',styles["asmm"]), date, Paragraph('Aircraft:',styles["asmm"]), aircraft],
           [Paragraph('Flight number:',styles["asmm"]), flight_number, Paragraph('Operator:',styles["asmm"]), operator],
           [Paragraph('Mission scientist:',styles["asmm"]), mission_scientist, Paragraph('Location:',styles["asmm"]), country]]
    table=Table(data, colWidths=[95, 170, 90, 170], rowHeights=30)
    table.setStyle(TableStyle([('ALIGN',(0,0),(3,3),'LEFT'),
                               ('VALIGN',(0,0),(3,3),'TOP'),
                               ('LEFTPADDING',(0,0),(0,3),5)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    
    # contact information
    story.append(Paragraph('Contact Information', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    contact_name = Paragraph(self.contactName_ln.text(), styles["asmm"])
    if self.contact_cb.currentText() != "Make a choice...":
        contact_role = Paragraph(self.contact_cb.currentText(), styles["asmm"])
    else:
        contact_role = Paragraph('', styles["asmm"])
    contact_email = Paragraph(self.contactEmail_ln.text(), styles["asmm"])
    data = [[Paragraph('Name:', styles["asmm"]), contact_name, Paragraph('Email:', styles["asmm"]), contact_email], 
            [Paragraph('Role:', styles["asmm"]), contact_role]]
    table=Table(data, colWidths=[43, 219, 43, 220], rowHeights=30) # 525
    table.setStyle(TableStyle([('ALIGN',(0,0),(3,1),'LEFT'),
                               ('VALIGN',(0,0),(3,1),'TOP'),
                               ('LEFTPADDING',(0,0),(0,1),5)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    # scientific aims
    story.append(Paragraph('Scientific Aims', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[check_boxes(self.satelliteCalValCheck),Paragraph('Satellite Cal/Var',styles["asmm"]),
             check_boxes(self.gasChemCheck),Paragraph('Gas Chemistry',styles["asmm"]),
             check_boxes(self.radiationCheck),Paragraph('Radiation',styles["asmm"])],
            [check_boxes(self.anthroPollutionCheck),Paragraph('Anthropogenic poullution',styles["asmm"]),
             check_boxes(self.gasChemOxidantsCheck),Paragraph('Oxydants',styles["asmm"]),
             check_boxes(self.radiationAtmosSpectroscopyCheck),Paragraph('Atmospheric spectroscopy',styles["asmm"])],
            [check_boxes(self.mesoscaleImpactsCheck),Paragraph('Mesoscale atmospheric impacts',styles["asmm"]),
             check_boxes(self.gasChemOrganicsCheck),Paragraph('Organics',styles["asmm"]),
             check_boxes(self.radiationSurfPropertiesCheck),Paragraph('Surf. properties/retrievals',styles["asmm"])],
            [None, Paragraph('<u>Cloud:</u>',styles["checkbox_title"]),
             check_boxes(self.gasChemOtherCheck),Paragraph('Other',styles["asmm"]),
             check_boxes(self.radiationOtherCheck),Paragraph('Other',styles["asmm"])],
            [check_boxes(self.cloudMicrophysicsCheck),Paragraph('Microphysics',styles["asmm"]),
             None,None,
             None,None],
            [check_boxes(self.cloudDynamicsCheck),Paragraph('Dynamics',styles["asmm"]),
             check_boxes(self.aerosolCheck),Paragraph('Aerosol',styles["asmm"]),
             None,Paragraph('<u>Boundary-layer:</u>',styles["checkbox_title"])],
            [check_boxes(self.cloudRadiativeCheck),Paragraph('Radiative properties',styles["asmm"]),
             check_boxes(self.aerosolMicrophysicalCheck),Paragraph('Cloud microphysical impacts',styles["asmm"]),
             check_boxes(self.blCloudCheck),Paragraph('Cloud',styles["asmm"])],
            [check_boxes(self.cloudConvectionCheck),Paragraph('Convection dynamics',styles["asmm"]),
             check_boxes(self.aerosolRadiativeCheck),Paragraph('Radiative properties/impacts',styles["asmm"]),
             check_boxes(self.blDynamicsCheck),Paragraph('Dynamics',styles["asmm"])]]
    table=Table(data, colWidths=[14, 175, 14, 175, 14, 160], rowHeights=20) # 525
    table.setStyle(TableStyle([('LEFTPADDING',(2,1),(3,3),20),
                               ('LEFTPADDING',(0,4),(1,7),20),
                               ('LEFTPADDING',(4,1),(5,3),20),
                               ('LEFTPADDING',(2,6),(3,7),20),
                               ('LEFTPADDING',(4,6),(5,7),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.sa_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_5.count()):
            if isinstance(self.gridLayout_5.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_5.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_5.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_5.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.SAOtherTextBox.toPlainText():
        story.append(Paragraph(self.SAOtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # geographical region
    story.append(Paragraph('Geographical Region', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Geographic Bounding Box:</u>',styles["checkbox_title"]))
    try:
        if float(self.northBoundLatitudeLine.text()) < 0:
            north = self.northBoundLatitudeLine.text()[1:] + '°S'
        else:
            north = self.northBoundLatitudeLine.text() + '°N'
    except ValueError:
        north = '' 
    try:
        if float(self.southBoundLatitudeLine.text()) < 0:
            south = self.southBoundLatitudeLine.text()[1:] + '°S'
        else:
            south = self.southBoundLatitudeLine.text() + '°N'
    except ValueError:
        south = '' 
    try:
            if float(self.eastBoundLongitudeLine.text()) < 0:
                east = self.eastBoundLongitudeLine.text()[1:] + '°W'
            else:
                east = self.eastBoundLongitudeLine.text() + '°E'
    except ValueError:
        east = '' 
    try:
        if float(self.westBoundLongitudeLine.text()) < 0:
            west = self.westBoundLongitudeLine.text()[1:] + '°W'
        else:
            west = self.westBoundLongitudeLine.text() + '°E'
    except ValueError:
        west = '' 
    if self.minAltitudeLine.text():
        min_alt = self.minAltitudeLine.text() + 'm'
    else:
        min_alt = ''
    if self.maxAltitudeLine.text():
        max_alt = self.maxAltitudeLine.text() + 'm'
    else:
        max_alt = ''
    data = [[Paragraph('North/South latitudes:',styles["asmm"]),
             Paragraph(north + ' / ' + south,styles["asmm"]),
             Paragraph('Min/Max altitudes:',styles["asmm"]),
             Paragraph(min_alt + ' / ' + max_alt,styles["asmm"])],
            [Paragraph('West/East longitudes:',styles["asmm"]),
             Paragraph(west + ' / ' + east,styles["asmm"]),
             None,
             None]]
    table=Table(data, colWidths=[125, 130, 105, 140], rowHeights=20)
    table.setStyle(TableStyle([('ALIGN',(0,0),(3,1),'LEFT'),
                               ('VALIGN',(0,0),(3,1),'TOP')]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Geographic Situation:</u>',styles["checkbox_title"]))
    data = [[check_boxes(self.polarCheck),Paragraph('Polar',styles["asmm"]),
             check_boxes(self.subTropicalCheck),Paragraph('Sub-tropical',styles["asmm"]),
             check_boxes(self.maritimeCheck),Paragraph('Maritime',styles["asmm"]),
             check_boxes(self.oceanicIslandsCheck),Paragraph('Oceanic islands',styles["asmm"])],
            [check_boxes(self.midLatitudesCheck),Paragraph('Mid-latitudes',styles["asmm"]),
             check_boxes(self.tropicalCheck),Paragraph('Tropical',styles["asmm"]),
             check_boxes(self.continentalCheck),Paragraph('Continental',styles["asmm"]),
             check_boxes(self.geogOtherCheck),Paragraph('Other',styles["asmm"])]]
    table=Table(data, colWidths=[14, 120, 14, 120, 14, 120, 14, 120], rowHeights=20) # 525
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.gr_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_8.count()):
            if isinstance(self.gridLayout_8.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_8.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_8.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_8.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.GROtherTextBox.toPlainText():
        story.append(Paragraph(self.GROtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # atmospheric features
    story.append(Paragraph('Atmospheric Synoptic Features', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[check_boxes(self.stationaryCheck),Paragraph('Stationary',styles["asmm"]),
             check_boxes(self.coldFrontCheck),Paragraph('Cold front',styles["asmm"]),
             check_boxes(self.orographicInfluenceCheck),Paragraph('Orographic influence',styles["asmm"])],
            [check_boxes(self.stationaryAnticyclonicCheck),Paragraph('Anticyclonic',styles["asmm"]),
             check_boxes(self.occludedFrontCheck),Paragraph('Occluded front',styles["asmm"]),
             check_boxes(self.seaBreezeFrontCheck),Paragraph('Sea-breeze front',styles["asmm"])],
            [check_boxes(self.stationaryCyclonicCheck),Paragraph('Cyclonic',styles["asmm"]),
             check_boxes(self.warmSectorCheck),Paragraph('Warm sector',styles["asmm"]),
             check_boxes(self.stratosphericFoldCheck),Paragraph('Stratospheric fold/intrusion',styles["asmm"])],
            [check_boxes(self.warmFrontCheck),Paragraph('Warm front',styles["asmm"]),
             check_boxes(self.postColdFrontalAirMassCheck),Paragraph('Post-cold-frontal air-mass',styles["asmm"]),
             check_boxes(self.extendedConvergenceLineCheck),Paragraph('Extended convergence line',styles["asmm"])],
            [check_boxes(self.warmConveyorBeltCheck),Paragraph('Warm conveyor belt',styles["asmm"]),
             check_boxes(self.arcticColdAirOutbreakCheck),Paragraph('Arctic cold-air outbreak',styles["asmm"]),
             check_boxes(self.easterlyWaveCheck),Paragraph('Easterly wave',styles["asmm"])],
            [check_boxes(self.equatorialWaveCheck),Paragraph('Equatorial wave',styles["asmm"]),
             check_boxes(self.tropicalCycloneCheck),Paragraph('Tropical cyclone',styles["asmm"]),
             check_boxes(self.mesoscaleOrganizedConvectionCheck),Paragraph('Mesoscale organized convection',styles["asmm"])]]
    table=Table(data, colWidths=[14, 160, 14, 160, 14, 180], rowHeights=20)
    table.setStyle(TableStyle([('LEFTPADDING',(0,1),(1,2),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.af_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_9.count()):
            if isinstance(self.gridLayout_9.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_9.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_9.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_9.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.AFOtherTextBox.toPlainText():
        story.append(Paragraph(self.AFOtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # cloud types
    story.append(Paragraph('Cloud Types and Forms sampled during flight', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[check_boxes(self.waterCloudsCheck),Paragraph('Water clouds',styles["asmm"]),
             check_boxes(self.contrailsCheck),Paragraph('Contrails',styles["asmm"]),
             check_boxes(self.altostratusAltocumulusCheck),Paragraph('Altostratus/Altocumulus',styles["asmm"])],
            [check_boxes(self.cloudFreeAboveAircraftCheck),Paragraph('Cloud-free above aircraft',styles["asmm"]),
             check_boxes(self.mixedPhaseCloudsCheck),Paragraph('Mixed-phase clouds',styles["asmm"]),
             check_boxes(self.stratocumulusCheck),Paragraph('Stratocumulus',styles["asmm"])],
            [check_boxes(self.waveCloudsCheck),Paragraph('Wave clouds',styles["asmm"]),
             check_boxes(self.cloudFreeBelowAircraftCheck),Paragraph('Cloud-free below aircraft',styles["asmm"]),
             check_boxes(self.iceCloudsCheck),Paragraph('Ice clouds',styles["asmm"])],
            [check_boxes(self.shallowCumulusCheck),Paragraph('Shallow cumulus',styles["asmm"]),
             check_boxes(self.cumulonimbusToweringCumulusCheck),Paragraph('Cumulonimbus/towering cumulus',styles["asmm"]),
             check_boxes(self.deepFrontalStratiformCloudsCheck),Paragraph('Deep frontal statiform clouds',styles["asmm"])],
            [check_boxes(self.cirrusCheck),Paragraph('Cirrus',styles["asmm"]),
             check_boxes(self.cumulusCongestusCheck),Paragraph('Cumulus congestus',styles["asmm"]),
             None,None]]
    table=Table(data, colWidths=[14, 150, 14, 190, 14, 160], rowHeights=20)
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.ct_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_10.count()):
            if isinstance(self.gridLayout_10.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_10.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_10.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_10.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.CTOtherTextBox.toPlainText():
        story.append(Paragraph(self.CTOtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # particles sampled
    story.append(Paragraph('Cloud, Precipitation and Aerosoft Particles Sampled', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[check_boxes(self.rainCheck),Paragraph('Rain',styles["asmm"]),
             check_boxes(self.pristineIceCrystalsCheck),Paragraph('Pristine ice crystals',styles["asmm"]),
             check_boxes(self.seaSaltAerosolCheck),Paragraph('Sea-salt aerosol',styles["asmm"])],
            [check_boxes(self.biomassBurningCheck),Paragraph('Biomass burning',styles["asmm"]),
             check_boxes(self.drizzleCheck),Paragraph('Drizzle',styles["asmm"]),
             check_boxes(self.snowOrAggregatesCheck),Paragraph('Snow/aggregates',styles["asmm"])],
            [check_boxes(self.continentalAerosolCheck),Paragraph('Continental aerosol',styles["asmm"]),
             check_boxes(self.desertOrMineralDustCheck),Paragraph('Desert/mineral dust',styles["asmm"]),
             check_boxes(self.dropletsCheck),Paragraph('Droplets (Liquid)',styles["asmm"])],
            [check_boxes(self.graupelOrHailCheck),Paragraph('Graupel/Hail',styles["asmm"]),
             check_boxes(self.urbanPlumeCheck),Paragraph('Urban plume',styles["asmm"]),
             check_boxes(self.volcanicAshCheck),Paragraph('Volcanic ash',styles["asmm"])]]
    table=Table(data, colWidths=[14, 165, 14, 165, 14, 165], rowHeights=20)
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.ps_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_11.count()):
            if isinstance(self.gridLayout_11.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_11.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_11.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_11.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.PSOtherTextBox.toPlainText():
        story.append(Paragraph(self.PSOtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # surfaces overflown
    story.append(Paragraph('Land or Oceans Surfaces Overflown', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[check_boxes(self.oceanCheck),Paragraph('Ocean',styles["asmm"]),
             check_boxes(self.desertCheck),Paragraph('Desert',styles["asmm"]),
             check_boxes(self.lakeIceCheck),Paragraph('Lake-ice',styles["asmm"]),
             check_boxes(self.hillyCheck),Paragraph('Hilly',styles["asmm"])],
            [check_boxes(self.semiAridCheck),Paragraph('Semi-arid',styles["asmm"]),
             check_boxes(self.snowCheck),Paragraph('Snow',styles["asmm"]),
             check_boxes(self.mountainousCheck),Paragraph('Mountainous',styles["asmm"]),
             check_boxes(self.forestCheck),Paragraph('Forest',styles["asmm"])],
            [check_boxes(self.seaIceCheck),Paragraph('Sea-ice',styles["asmm"]),
             check_boxes(self.urbanCheck),Paragraph('Urban',styles["asmm"]),
             check_boxes(self.vegetationCheck),Paragraph('Vegetation',styles["asmm"]),
             check_boxes(self.flatCheck),Paragraph('Flat',styles["asmm"])]]
    table=Table(data, colWidths=[14, 120, 14, 120, 14, 120, 14, 120], rowHeights=20)
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.so_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_16.count()):
            if isinstance(self.gridLayout_16.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_16.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_16.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_16.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.SOOtherTextBox.toPlainText():
        story.append(Paragraph(self.SOOtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # surfaces overflown
    story.append(Paragraph('Altitude Range of Measurement', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[check_boxes(self.boundaryLayerCheck),Paragraph('Boundary-layer',styles["asmm"]),
             check_boxes(self.lowerTroposphereCheck),Paragraph('Lower troposphere',styles["asmm"]),
             check_boxes(self.upperTroposphereCheck),Paragraph('Upper troposphere',styles["asmm"])],
            [check_boxes(self.blNearSurfaceCheck),Paragraph('near-surface',styles["asmm"]),
             check_boxes(self.midTroposphereCheck),Paragraph('Mid troposphere',styles["asmm"]),
             check_boxes(self.lowerStratosphereCheck),Paragraph('Lower stratosphere',styles["asmm"])],
            [check_boxes(self.blSubCloudCheck),Paragraph('sub-cloud',styles["asmm"]),
             None,None],
            [check_boxes(self.blInCloudCheck),Paragraph('in-cloud',styles["asmm"]),
             None,None]]
    table=Table(data, colWidths=[14, 165, 14, 165, 14, 165], rowHeights=20)
    table.setStyle(TableStyle([('LEFTPADDING',(0,1),(1,3),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.ar_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_14.count()):
            if isinstance(self.gridLayout_14.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_14.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_14.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_14.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.AROtherTextBox.toPlainText():
        story.append(Paragraph(self.AROtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # flight manoeuvre
    story.append(Paragraph('Types of Flight Manoeuvre', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[check_boxes(self.straightLevelRunsCheck),Paragraph('Straight/level runs',styles["asmm"]),
             check_boxes(self.racetracksCheck),Paragraph('Racetracks',styles["asmm"]),
             check_boxes(self.lagrangianDescentsCheck),Paragraph('Lagrangian descents',styles["asmm"]),
             check_boxes(self.dropsondeDeployedCheck),Paragraph('Dropsonde deployed',styles["asmm"])],
            [check_boxes(self.stackedStraightLevelRunsCheck),Paragraph('stacked',styles["asmm"]),
             check_boxes(self.orbitsCheck),Paragraph('Orbits',styles["asmm"]),
             check_boxes(self.deepProfileAscentDescentsCheck),Paragraph('Deep profile ascents/descents',styles["asmm"]),
             check_boxes(self.selfCalibrationCheck),Paragraph('Self-calibration',styles["asmm"])],
            [check_boxes(self.separatedStraightLevelRuns),Paragraph('separated',styles["asmm"]),
             None,None,None,None,None,None,]]
    table=Table(data, colWidths=[14, 110, 14, 80, 14, 165, 14, 130], rowHeights=20)
    table.setStyle(TableStyle([('LEFTPADDING',(0,1),(1,2),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.fm_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_15.count()):
            if isinstance(self.gridLayout_15.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_15.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_15.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_15.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.FTOtherTextBox.toPlainText():
        story.append(Paragraph(self.FTOtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # satellite coordination
    story.append(Paragraph('Satellite Coordination', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[None,Paragraph('<u>Polar:</u>',styles["checkbox_title"]),
             None,Paragraph('<u>Geosynch:</u>',styles["checkbox_title"]),
             check_boxes(self.modisCheck),Paragraph('MODIS',styles["asmm"]),
             check_boxes(self.airsCheck),Paragraph('AIRS',styles["asmm"])],
            [check_boxes(self.polarMetopCheck),Paragraph('METOP',styles["asmm"]),
             check_boxes(self.geosynchMsgCheck),Paragraph('MSG',styles["asmm"]),
             check_boxes(self.cloudsatCheck),Paragraph('Cloudsat',styles["asmm"]),
             check_boxes(self.crisCheck),Paragraph('CriS',styles["asmm"])],
            [check_boxes(self.polarNpoessCheck),Paragraph('NPOESS',styles["asmm"]),
             check_boxes(self.geosynchOtherCheck),Paragraph('Other',styles["asmm"]),
             check_boxes(self.caliopCheck),Paragraph('CALIOP',styles["asmm"]),
             check_boxes(self.amsuMhsCheck),Paragraph('AMSU/MHS',styles["asmm"])],
            [check_boxes(self.polarAtrainCheck),Paragraph('A-train',styles["asmm"]),
             None,None,
             check_boxes(self.iasiCheck),Paragraph('IASI',styles["asmm"]),
             None, None],
            [check_boxes(self.polarOtherCheck),Paragraph('Other',styles["asmm"]),
             None, None,None, None,None, None]]
    table=Table(data, colWidths=[14, 125, 14, 125, 14, 125, 14, 125], rowHeights=20)
    table.setStyle(TableStyle([('LEFTPADDING',(0,1),(1,4),20),
                               ('LEFTPADDING',(2,1),(3,2),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    if self.sc_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', styles["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_25.count()):
            if isinstance(self.gridLayout_25.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_25.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_25.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_25.itemAt(i).widget().text()), styles["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph('<u>Comments:</u>',styles["checkbox_title"]))
    if self.SCOtherTextBox.toPlainText():
        story.append(Paragraph(self.SCOtherTextBox.toPlainText(),styles["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    else:
        story.append(Paragraph('No comment',styles["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', styles["asmm"]))
    
    
    # supporting observations
    story.append(Paragraph('Supporting Surface-based Observations', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    data = [[Paragraph('<u>Ground sites:</u>',styles["checkbox_title"]), None, Paragraph('<u>ARM sites:</u>',styles["checkbox_title"])]]
    first_rows_num = 0
    if len(self.arm_site_list) >= len(self.ground_site_list):
        first_rows_num = len(self.arm_site_list)
    else:
        first_rows_num = len(self.ground_site_list)
    if first_rows_num == 0:
        data.append([None, None, None])
    else:
        for i in range(first_rows_num):
            try:
                left_cell = Paragraph(self.ground_site_list[i], styles["asmm"])
            except IndexError:
                left_cell = None
            try:
                right_cell = Paragraph(self.arm_site_list[i], styles["asmm"])
            except IndexError:
                right_cell = None
            data.append([left_cell, None, right_cell])
    data.append([None, None, None])
    data.append([Paragraph('<u>Research vessels:</u>',styles["checkbox_title"]), None, Paragraph('<u>ARM mobile sites:</u>',styles["checkbox_title"])])
    second_rows_num = 0
    if len(self.arm_mobile_list) >= len(self.research_vessel_list):
        second_rows_num = len(self.arm_mobile_list)
    else:
        second_rows_num = len(self.research_vesse_list)
    if second_rows_num == 0:
        data.append([None, None, None])
    else:
        for i in range(second_rows_num):
            try:
                left_cell = Paragraph(self.research_vessel_list[i], styles["asmm"])
            except IndexError:
                left_cell = None
            try:
                right_cell = Paragraph(self.arm_mobile_list[i], styles["asmm"])
            except IndexError:
                right_cell = None
            data.append([left_cell, None, right_cell])
    table=Table(data, colWidths=[240, 20, 240], rowHeights=20)
    if first_rows_num == 0:
        first_rows_num = 1  
    if second_rows_num == 0:
        second_rows_num = 1
    table.setStyle(TableStyle([('BOX',(0,1),(0,first_rows_num), 1, colors.black)]))
    table.setStyle(TableStyle([('BOX',(2,1),(2,first_rows_num), 1, colors.black)]))
    table.setStyle(TableStyle([('BOX',(0,first_rows_num + 3),(0,first_rows_num + 2 + second_rows_num), 1, colors.black)]))
    table.setStyle(TableStyle([('BOX',(2,first_rows_num + 3),(2,first_rows_num + 2 + second_rows_num), 1, colors.black)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    
    # additional notes
    story.append(Paragraph('Additional Notes on the Flight', styles["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    story.append(Paragraph(self.OtherCommentsTextBox.toPlainText(), styles["asmm"]))
    story.append(Paragraph('<br/><br/>', styles["asmm"]))
    
    
    # images
    if self.images_pdf_path:
        story.append(Paragraph('Images Included in the PDF Report', styles["section_title"]))
        sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
        story.append(sq)
        story.append(Paragraph('<br/><br/>', styles["asmm"]))
        i = 0
        for path in self.images_pdf_path:
            image_info = utils.ImageReader(path)
            width, height = image_info.getSize()
            ratio = float(width) / float(height)
            if ratio > 1:
                width = 450
                height = 450 / float(ratio)
            elif ratio < 0.5:
                height = 400
                width = 400 * float(ratio)
            else:
                height = 450
                width = 450 * float(ratio)
            image = Image(path, width=width, height=height)
            image.hAlign = 'CENTER'
            story.append(image)
            story.append(Paragraph('<br/>', styles["asmm"]))
            data = [[Paragraph('<u>Figure ' + str(i + 1) + ':</u>', styles['figure_number']),
                     Paragraph(self.im_textbox[i].text(), styles['figure_caption'])]]
            table=Table(data, colWidths=[100, 400], rowHeights=40)
            table.setStyle(TableStyle([('VALIGN',(0,0),(1,0),'TOP')]))
            story.append(table)
            story.append(Paragraph('<br/><br/>', styles["asmm"]))
            i += 1
        story.pop(-1) 
    docpdf.build(story)
    

def create_date_string():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    if len(month) < 2:
        month = "0" + month
    if len(day) < 2:
        day = "0" + day
    string = year + '-' + month + '-'+ day
    return string

    
def check_boxes(itemc):
    if itemc.isChecked():
        t = tick_2(0,2,8,8,1,1.5,'red')
    else:
        t = tick_2(0,2,8,8,0,1.5,'red')
    return t

    