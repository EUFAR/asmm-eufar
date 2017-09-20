import datetime
import logging
from PyQt5 import QtCore, QtWidgets
from reportlab.platypus import Paragraph, Image, doctemplate, tables
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib import colors, utils, enums, pagesizes, styles
from functions.signs_and_figures import tick_2, square, semi_square


def create_asmm_pdf(self, out_file_name_pdf):
    logging.debug('asmm_pdf.py - create_asmm_pdf - out_file_name_pdf ' + str(out_file_name_pdf))
    
    # document creation
    docpdf = doctemplate.SimpleDocTemplate(out_file_name_pdf,
                               pagesize = pagesizes.A4,
                               rightMargin=30,
                               leftMargin=30,
                               topMargin=30,
                               bottomMargin=50)
    page_w, _ = pagesizes.A4
    
    
    # polices
    pdfmetrics.registerFont(ttfonts.TTFont('asmm', 'fonts/SourceSansPro-Regular.ttf'))
    pdfmetrics.registerFont(ttfonts.TTFont('asmm_bold', 'fonts/SourceSansPro-Semibold.ttf'))
    pdfmetrics.registerFont(ttfonts.TTFont('asmm_italic', 'fonts/SourceSansPro-Italic.ttf'))


    # styles
    style = styles.getSampleStyleSheet()
    style.add(styles.ParagraphStyle(name='report_title', fontName='asmm', fontSize=22, alignment=enums.TA_CENTER, wordWrap = 'CJK'))
    style.add(styles.ParagraphStyle(name='date', fontName='asmm', fontSize=13, alignment=enums.TA_RIGHT, wordWrap = 'CJK'))
    style.add(styles.ParagraphStyle(name='section_title', fontName='asmm_bold', fontSize=16, alignment=enums.TA_LEFT, wordWrap = 'CJK'))
    style.add(styles.ParagraphStyle(name='asmm', fontName='asmm', fontSize=12, leading=14, wordWrap = 'CJK'))
    style.add(styles.ParagraphStyle(name='asmm_justify', fontName='asmm', fontSize=12, alignment=enums.TA_JUSTIFY, leading=14, wordWrap = 'CJK'))
    style.add(styles.ParagraphStyle(name='checkbox_title', fontName='asmm_bold', fontSize=12, leading=14, wordWrap = 'CJK'))
    style.add(styles.ParagraphStyle(name='figure_number', fontName='asmm_bold', fontSize=12, alignment=enums.TA_RIGHT, leading=14, wordWrap = 'CJK'))
    style.add(styles.ParagraphStyle(name='figure_caption', fontName='asmm_italic', fontSize=12, alignment=enums.TA_LEFT, leading=14, wordWrap = 'CJK'))


    # title and date
    story = []
    story.append(Paragraph(create_date_string(), style["date"]))
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    story.append(Paragraph('Airborne Science Mission Metadata<br/><br/>Report', style["report_title"]))
    sq = square(90, -20, 342, 60, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/><br/><br/>', style["asmm"]))
    
    
    # flight information
    proj_acronyme = Paragraph(self.projectAcronym_ln.text(),style["asmm"])
    date = Paragraph(self.date_dt.date().toString(QtCore.Qt.ISODate),style["asmm"])
    flight_number = Paragraph(self.flightNumber_ln.text(),style["asmm"])
    mission_scientist = Paragraph(self.missionSci_ln.text(),style["asmm"])
    flight_manager = Paragraph(self.flightManager_ln.text(),style["asmm"])
    if self.aircraft_cb.currentText() == "Make a choice...":
        aircraft = Paragraph("",style["asmm"])
    elif self.aircraft_cb.currentText() == "Other...":
        aircraft = Paragraph(self.newAircraft_ln.text(),style["asmm"])
    else:
        aircraft = Paragraph(self.aircraft_cb.currentText(),style["asmm"])
    if self.operator_cb.currentText() == "Make a choice...":
        operator = Paragraph("",style["asmm"])
    elif self.operator_cb.currentText() == "Other...":
        operator = Paragraph(self.newOperator_ln.text(),style["asmm"])
    else:
        operator = Paragraph(self.operator_cb.currentText(),style["asmm"])
    if self.location_cb.currentText() == "Make a choice..." or self.detailList.currentText() == "Make a choice...":
        country = Paragraph("",style["asmm"])
    else:
        country = Paragraph(self.detailList.currentText(),style["asmm"])
    story.append(Paragraph('Flight Information', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data= [[Paragraph('Project acronym:',style["asmm"]), proj_acronyme, Paragraph('Flight manager:',style["asmm"]), flight_manager],
           [Paragraph('Date:',style["asmm"]), date, Paragraph('Aircraft:',style["asmm"]), aircraft],
           [Paragraph('Flight number:',style["asmm"]), flight_number, Paragraph('Operator:',style["asmm"]), operator],
           [Paragraph('Mission scientist:',style["asmm"]), mission_scientist, Paragraph('Location:',style["asmm"]), country]]
    table=tables.Table(data, colWidths=[95, 170, 90, 170], rowHeights=30)
    table.setStyle(tables.TableStyle([('ALIGN',(0,0),(3,3),'LEFT'),
                               ('VALIGN',(0,0),(3,3),'TOP'),
                               ('LEFTPADDING',(0,0),(0,3),5)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    
    # contact information
    story.append(Paragraph('Contact Information', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    contact_name = Paragraph(self.contactName_ln.text(), style["asmm"])
    if self.contact_cb.currentText() != "Make a choice...":
        contact_role = Paragraph(self.contact_cb.currentText(), style["asmm"])
    else:
        contact_role = Paragraph('', style["asmm"])
    contact_email = Paragraph(self.contactEmail_ln.text(), style["asmm"])
    data = [[Paragraph('Name:', style["asmm"]), contact_name, Paragraph('Email:', style["asmm"]), contact_email], 
            [Paragraph('Role:', style["asmm"]), contact_role]]
    table=tables.Table(data, colWidths=[43, 219, 43, 220], rowHeights=30) # 525
    table.setStyle(tables.TableStyle([('ALIGN',(0,0),(3,1),'LEFT'),
                               ('VALIGN',(0,0),(3,1),'TOP'),
                               ('LEFTPADDING',(0,0),(0,1),5)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    
    # scientific aims
    story.append(Paragraph('Scientific Aims', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[check_boxes(self.satelliteCalValCheck),Paragraph('Satellite Cal/Var',style["asmm"]),
             check_boxes(self.gasChemCheck),Paragraph('Gas Chemistry',style["asmm"]),
             check_boxes(self.radiationCheck),Paragraph('Radiation',style["asmm"])],
            [check_boxes(self.anthroPollutionCheck),Paragraph('Anthropogenic poullution',style["asmm"]),
             check_boxes(self.gasChemOxidantsCheck),Paragraph('Oxydants',style["asmm"]),
             check_boxes(self.radiationAtmosSpectroscopyCheck),Paragraph('Atmospheric spectroscopy',style["asmm"])],
            [check_boxes(self.mesoscaleImpactsCheck),Paragraph('Mesoscale atmospheric impacts',style["asmm"]),
             check_boxes(self.gasChemOrganicsCheck),Paragraph('Organics',style["asmm"]),
             check_boxes(self.radiationSurfPropertiesCheck),Paragraph('Surf. properties/retrievals',style["asmm"])],
            [None, Paragraph('<u>Cloud:</u>',style["checkbox_title"]),
             check_boxes(self.gasChemOtherCheck),Paragraph('Other',style["asmm"]),
             check_boxes(self.radiationOtherCheck),Paragraph('Other',style["asmm"])],
            [check_boxes(self.cloudMicrophysicsCheck),Paragraph('Microphysics',style["asmm"]),
             None,None,
             None,None],
            [check_boxes(self.cloudDynamicsCheck),Paragraph('Dynamics',style["asmm"]),
             check_boxes(self.aerosolCheck),Paragraph('Aerosol',style["asmm"]),
             None,Paragraph('<u>Boundary-layer:</u>',style["checkbox_title"])],
            [check_boxes(self.cloudRadiativeCheck),Paragraph('Radiative properties',style["asmm"]),
             check_boxes(self.aerosolMicrophysicalCheck),Paragraph('Cloud microphysical impacts',style["asmm"]),
             check_boxes(self.blCloudCheck),Paragraph('Cloud',style["asmm"])],
            [check_boxes(self.cloudConvectionCheck),Paragraph('Convection dynamics',style["asmm"]),
             check_boxes(self.aerosolRadiativeCheck),Paragraph('Radiative properties/impacts',style["asmm"]),
             check_boxes(self.blDynamicsCheck),Paragraph('Dynamics',style["asmm"])]]
    table=tables.Table(data, colWidths=[14, 175, 14, 175, 14, 160], rowHeights=20) # 525
    table.setStyle(tables.TableStyle([('LEFTPADDING',(2,1),(3,3),20),
                               ('LEFTPADDING',(0,4),(1,7),20),
                               ('LEFTPADDING',(4,1),(5,3),20),
                               ('LEFTPADDING',(2,6),(3,7),20),
                               ('LEFTPADDING',(4,6),(5,7),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.sa_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_5.count()):
            if isinstance(self.gridLayout_5.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_5.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_5.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_5.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.SAOtherTextBox.toPlainText():
        story.append(Paragraph(self.SAOtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # geographical region
    story.append(Paragraph('Geographical Region', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    story.append(Paragraph('<u>Geographic Bounding Box:</u>',style["checkbox_title"]))
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
    data = [[Paragraph('North/South latitudes:',style["asmm"]),
             Paragraph(north + ' / ' + south,style["asmm"]),
             Paragraph('Min/Max altitudes:',style["asmm"]),
             Paragraph(min_alt + ' / ' + max_alt,style["asmm"])],
            [Paragraph('West/East longitudes:',style["asmm"]),
             Paragraph(west + ' / ' + east,style["asmm"]),
             None,
             None]]
    table=tables.Table(data, colWidths=[125, 130, 105, 140], rowHeights=20)
    table.setStyle(tables.TableStyle([('ALIGN',(0,0),(3,1),'LEFT'),
                               ('VALIGN',(0,0),(3,1),'TOP')]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    story.append(Paragraph('<u>Geographic Situation:</u>',style["checkbox_title"]))
    data = [[check_boxes(self.polarCheck),Paragraph('Polar',style["asmm"]),
             check_boxes(self.subTropicalCheck),Paragraph('Sub-tropical',style["asmm"]),
             check_boxes(self.maritimeCheck),Paragraph('Maritime',style["asmm"]),
             check_boxes(self.oceanicIslandsCheck),Paragraph('Oceanic islands',style["asmm"])],
            [check_boxes(self.midLatitudesCheck),Paragraph('Mid-latitudes',style["asmm"]),
             check_boxes(self.tropicalCheck),Paragraph('Tropical',style["asmm"]),
             check_boxes(self.continentalCheck),Paragraph('Continental',style["asmm"]),
             check_boxes(self.geogOtherCheck),Paragraph('Other',style["asmm"])]]
    table=tables.Table(data, colWidths=[14, 120, 14, 120, 14, 120, 14, 120], rowHeights=20) # 525
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.gr_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_8.count()):
            if isinstance(self.gridLayout_8.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_8.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_8.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_8.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.GROtherTextBox.toPlainText():
        story.append(Paragraph(self.GROtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # atmospheric features
    story.append(Paragraph('Atmospheric Synoptic Features', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[check_boxes(self.stationaryCheck),Paragraph('Stationary',style["asmm"]),
             check_boxes(self.coldFrontCheck),Paragraph('Cold front',style["asmm"]),
             check_boxes(self.orographicInfluenceCheck),Paragraph('Orographic influence',style["asmm"])],
            [check_boxes(self.stationaryAnticyclonicCheck),Paragraph('Anticyclonic',style["asmm"]),
             check_boxes(self.occludedFrontCheck),Paragraph('Occluded front',style["asmm"]),
             check_boxes(self.seaBreezeFrontCheck),Paragraph('Sea-breeze front',style["asmm"])],
            [check_boxes(self.stationaryCyclonicCheck),Paragraph('Cyclonic',style["asmm"]),
             check_boxes(self.warmSectorCheck),Paragraph('Warm sector',style["asmm"]),
             check_boxes(self.stratosphericFoldCheck),Paragraph('Stratospheric fold/intrusion',style["asmm"])],
            [check_boxes(self.warmFrontCheck),Paragraph('Warm front',style["asmm"]),
             check_boxes(self.postColdFrontalAirMassCheck),Paragraph('Post-cold-frontal air-mass',style["asmm"]),
             check_boxes(self.extendedConvergenceLineCheck),Paragraph('Extended convergence line',style["asmm"])],
            [check_boxes(self.warmConveyorBeltCheck),Paragraph('Warm conveyor belt',style["asmm"]),
             check_boxes(self.arcticColdAirOutbreakCheck),Paragraph('Arctic cold-air outbreak',style["asmm"]),
             check_boxes(self.easterlyWaveCheck),Paragraph('Easterly wave',style["asmm"])],
            [check_boxes(self.equatorialWaveCheck),Paragraph('Equatorial wave',style["asmm"]),
             check_boxes(self.tropicalCycloneCheck),Paragraph('Tropical cyclone',style["asmm"]),
             check_boxes(self.mesoscaleOrganizedConvectionCheck),Paragraph('Mesoscale organized convection',style["asmm"])]]
    table=tables.Table(data, colWidths=[14, 160, 14, 160, 14, 180], rowHeights=20)
    table.setStyle(tables.TableStyle([('LEFTPADDING',(0,1),(1,2),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.af_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_9.count()):
            if isinstance(self.gridLayout_9.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_9.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_9.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_9.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.AFOtherTextBox.toPlainText():
        story.append(Paragraph(self.AFOtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # cloud types
    story.append(Paragraph('Cloud Types and Forms sampled during flight', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[check_boxes(self.waterCloudsCheck),Paragraph('Water clouds',style["asmm"]),
             check_boxes(self.contrailsCheck),Paragraph('Contrails',style["asmm"]),
             check_boxes(self.altostratusAltocumulusCheck),Paragraph('Altostratus/Altocumulus',style["asmm"])],
            [check_boxes(self.cloudFreeAboveAircraftCheck),Paragraph('Cloud-free above aircraft',style["asmm"]),
             check_boxes(self.mixedPhaseCloudsCheck),Paragraph('Mixed-phase clouds',style["asmm"]),
             check_boxes(self.stratocumulusCheck),Paragraph('Stratocumulus',style["asmm"])],
            [check_boxes(self.waveCloudsCheck),Paragraph('Wave clouds',style["asmm"]),
             check_boxes(self.cloudFreeBelowAircraftCheck),Paragraph('Cloud-free below aircraft',style["asmm"]),
             check_boxes(self.iceCloudsCheck),Paragraph('Ice clouds',style["asmm"])],
            [check_boxes(self.shallowCumulusCheck),Paragraph('Shallow cumulus',style["asmm"]),
             check_boxes(self.cumulonimbusToweringCumulusCheck),Paragraph('Cumulonimbus/towering cumulus',style["asmm"]),
             check_boxes(self.deepFrontalStratiformCloudsCheck),Paragraph('Deep frontal statiform clouds',style["asmm"])],
            [check_boxes(self.cirrusCheck),Paragraph('Cirrus',style["asmm"]),
             check_boxes(self.cumulusCongestusCheck),Paragraph('Cumulus congestus',style["asmm"]),
             None,None]]
    table=tables.Table(data, colWidths=[14, 150, 14, 190, 14, 160], rowHeights=20)
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.ct_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_10.count()):
            if isinstance(self.gridLayout_10.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_10.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_10.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_10.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.CTOtherTextBox.toPlainText():
        story.append(Paragraph(self.CTOtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # particles sampled
    story.append(Paragraph('Cloud, Precipitation and Aerosoft Particles Sampled', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[check_boxes(self.rainCheck),Paragraph('Rain',style["asmm"]),
             check_boxes(self.pristineIceCrystalsCheck),Paragraph('Pristine ice crystals',style["asmm"]),
             check_boxes(self.seaSaltAerosolCheck),Paragraph('Sea-salt aerosol',style["asmm"])],
            [check_boxes(self.biomassBurningCheck),Paragraph('Biomass burning',style["asmm"]),
             check_boxes(self.drizzleCheck),Paragraph('Drizzle',style["asmm"]),
             check_boxes(self.snowOrAggregatesCheck),Paragraph('Snow/aggregates',style["asmm"])],
            [check_boxes(self.continentalAerosolCheck),Paragraph('Continental aerosol',style["asmm"]),
             check_boxes(self.desertOrMineralDustCheck),Paragraph('Desert/mineral dust',style["asmm"]),
             check_boxes(self.dropletsCheck),Paragraph('Droplets (Liquid)',style["asmm"])],
            [check_boxes(self.graupelOrHailCheck),Paragraph('Graupel/Hail',style["asmm"]),
             check_boxes(self.urbanPlumeCheck),Paragraph('Urban plume',style["asmm"]),
             check_boxes(self.volcanicAshCheck),Paragraph('Volcanic ash',style["asmm"])]]
    table=tables.Table(data, colWidths=[14, 165, 14, 165, 14, 165], rowHeights=20)
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.ps_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_11.count()):
            if isinstance(self.gridLayout_11.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_11.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_11.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_11.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.PSOtherTextBox.toPlainText():
        story.append(Paragraph(self.PSOtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # surfaces overflown
    story.append(Paragraph('Land or Oceans Surfaces Overflown', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[check_boxes(self.oceanCheck),Paragraph('Ocean',style["asmm"]),
             check_boxes(self.desertCheck),Paragraph('Desert',style["asmm"]),
             check_boxes(self.lakeIceCheck),Paragraph('Lake-ice',style["asmm"]),
             check_boxes(self.hillyCheck),Paragraph('Hilly',style["asmm"])],
            [check_boxes(self.semiAridCheck),Paragraph('Semi-arid',style["asmm"]),
             check_boxes(self.snowCheck),Paragraph('Snow',style["asmm"]),
             check_boxes(self.mountainousCheck),Paragraph('Mountainous',style["asmm"]),
             check_boxes(self.forestCheck),Paragraph('Forest',style["asmm"])],
            [check_boxes(self.seaIceCheck),Paragraph('Sea-ice',style["asmm"]),
             check_boxes(self.urbanCheck),Paragraph('Urban',style["asmm"]),
             check_boxes(self.vegetationCheck),Paragraph('Vegetation',style["asmm"]),
             check_boxes(self.flatCheck),Paragraph('Flat',style["asmm"])]]
    table=tables.Table(data, colWidths=[14, 120, 14, 120, 14, 120, 14, 120], rowHeights=20)
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.so_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_16.count()):
            if isinstance(self.gridLayout_16.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_16.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_16.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_16.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.SOOtherTextBox.toPlainText():
        story.append(Paragraph(self.SOOtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # surfaces overflown
    story.append(Paragraph('Altitude Range of Measurement', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[check_boxes(self.boundaryLayerCheck),Paragraph('Boundary-layer',style["asmm"]),
             check_boxes(self.lowerTroposphereCheck),Paragraph('Lower troposphere',style["asmm"]),
             check_boxes(self.upperTroposphereCheck),Paragraph('Upper troposphere',style["asmm"])],
            [check_boxes(self.blNearSurfaceCheck),Paragraph('near-surface',style["asmm"]),
             check_boxes(self.midTroposphereCheck),Paragraph('Mid troposphere',style["asmm"]),
             check_boxes(self.lowerStratosphereCheck),Paragraph('Lower stratosphere',style["asmm"])],
            [check_boxes(self.blSubCloudCheck),Paragraph('sub-cloud',style["asmm"]),
             None,None],
            [check_boxes(self.blInCloudCheck),Paragraph('in-cloud',style["asmm"]),
             None,None]]
    table=tables.Table(data, colWidths=[14, 165, 14, 165, 14, 165], rowHeights=20)
    table.setStyle(tables.TableStyle([('LEFTPADDING',(0,1),(1,3),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.ar_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_14.count()):
            if isinstance(self.gridLayout_14.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_14.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_14.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_14.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.AROtherTextBox.toPlainText():
        story.append(Paragraph(self.AROtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # flight manoeuvre
    story.append(Paragraph('Types of Flight Manoeuvre', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[check_boxes(self.straightLevelRunsCheck),Paragraph('Straight/level runs',style["asmm"]),
             check_boxes(self.racetracksCheck),Paragraph('Racetracks',style["asmm"]),
             check_boxes(self.lagrangianDescentsCheck),Paragraph('Lagrangian descents',style["asmm"]),
             check_boxes(self.dropsondeDeployedCheck),Paragraph('Dropsonde deployed',style["asmm"])],
            [check_boxes(self.stackedStraightLevelRunsCheck),Paragraph('stacked',style["asmm"]),
             check_boxes(self.orbitsCheck),Paragraph('Orbits',style["asmm"]),
             check_boxes(self.deepProfileAscentDescentsCheck),Paragraph('Deep profile ascents/descents',style["asmm"]),
             check_boxes(self.selfCalibrationCheck),Paragraph('Self-calibration',style["asmm"])],
            [check_boxes(self.separatedStraightLevelRuns),Paragraph('separated',style["asmm"]),
             None,None,None,None,None,None,]]
    table=tables.Table(data, colWidths=[14, 110, 14, 80, 14, 165, 14, 130], rowHeights=20)
    table.setStyle(tables.TableStyle([('LEFTPADDING',(0,1),(1,2),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.fm_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_15.count()):
            if isinstance(self.gridLayout_15.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_15.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_15.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_15.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.FTOtherTextBox.toPlainText():
        story.append(Paragraph(self.FTOtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # satellite coordination
    story.append(Paragraph('Satellite Coordination', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[None,Paragraph('<u>Polar:</u>',style["checkbox_title"]),
             None,Paragraph('<u>Geosynch:</u>',style["checkbox_title"]),
             check_boxes(self.modisCheck),Paragraph('MODIS',style["asmm"]),
             check_boxes(self.airsCheck),Paragraph('AIRS',style["asmm"])],
            [check_boxes(self.polarMetopCheck),Paragraph('METOP',style["asmm"]),
             check_boxes(self.geosynchMsgCheck),Paragraph('MSG',style["asmm"]),
             check_boxes(self.cloudsatCheck),Paragraph('Cloudsat',style["asmm"]),
             check_boxes(self.crisCheck),Paragraph('CriS',style["asmm"])],
            [check_boxes(self.polarNpoessCheck),Paragraph('NPOESS',style["asmm"]),
             check_boxes(self.geosynchOtherCheck),Paragraph('Other',style["asmm"]),
             check_boxes(self.caliopCheck),Paragraph('CALIOP',style["asmm"]),
             check_boxes(self.amsuMhsCheck),Paragraph('AMSU/MHS',style["asmm"])],
            [check_boxes(self.polarAtrainCheck),Paragraph('A-train',style["asmm"]),
             None,None,
             check_boxes(self.iasiCheck),Paragraph('IASI',style["asmm"]),
             None, None],
            [check_boxes(self.polarOtherCheck),Paragraph('Other',style["asmm"]),
             None, None,None, None,None, None]]
    table=tables.Table(data, colWidths=[14, 125, 14, 125, 14, 125, 14, 125], rowHeights=20)
    table.setStyle(tables.TableStyle([('LEFTPADDING',(0,1),(1,4),20),
                               ('LEFTPADDING',(2,1),(3,2),20)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    if self.sc_ck_list:
        story.append(Paragraph('<u>User-defined:</u>', style["checkbox_title"]))
        data = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        col = 0
        row = 0
        for i in range(self.gridLayout_25.count()):
            if isinstance(self.gridLayout_25.itemAt(i).widget(), QtWidgets.QCheckBox):
                if self.gridLayout_25.itemAt(i).widget().isChecked():
                    data[row][col] = check_boxes(self.gridLayout_25.itemAt(i).widget())
                    data[row][col + 1] = Paragraph(str(self.gridLayout_25.itemAt(i).widget().text()), style["asmm"])
                    col += 2
                    if col > 5:
                        row +=1
                        col = 0
        table=tables.Table(data, colWidths=[14, 170, 14, 170, 14, 170], rowHeights=20)
        table.setStyle(tables.TableStyle([('VALIGN',(1,0),(1,3),'TOP'),
                                   ('VALIGN',(3,0),(3,3),'TOP'),
                                   ('VALIGN',(5,0),(5,3),'TOP')]))
        story.append(table)
    story.append(Paragraph('<u>Comments:</u>',style["checkbox_title"]))
    if self.SCOtherTextBox.toPlainText():
        story.append(Paragraph(self.SCOtherTextBox.toPlainText(),style["asmm_justify"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    else:
        story.append(Paragraph('No comment',style["asmm"]))
        story.append(Paragraph('<br/><br/><br/>', style["asmm"]))
    
    
    # supporting observations
    story.append(Paragraph('Supporting Surface-based Observations', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    data = [[Paragraph('<u>Ground sites:</u>',style["checkbox_title"]), None, Paragraph('<u>ARM sites:</u>',style["checkbox_title"])]]
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
                left_cell = Paragraph(self.ground_site_list[i], style["asmm"])
            except IndexError:
                left_cell = None
            try:
                right_cell = Paragraph(self.arm_site_list[i], style["asmm"])
            except IndexError:
                right_cell = None
            data.append([left_cell, None, right_cell])
    data.append([None, None, None])
    data.append([Paragraph('<u>Research vessels:</u>',style["checkbox_title"]), None, Paragraph('<u>ARM mobile sites:</u>',style["checkbox_title"])])
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
                left_cell = Paragraph(self.research_vessel_list[i], style["asmm"])
            except IndexError:
                left_cell = None
            try:
                right_cell = Paragraph(self.arm_mobile_list[i], style["asmm"])
            except IndexError:
                right_cell = None
            data.append([left_cell, None, right_cell])
    table=tables.Table(data, colWidths=[240, 20, 240], rowHeights=20)
    if first_rows_num == 0:
        first_rows_num = 1  
    if second_rows_num == 0:
        second_rows_num = 1
    table.setStyle(tables.TableStyle([('BOX',(0,1),(0,first_rows_num), 1, colors.black)]))
    table.setStyle(tables.TableStyle([('BOX',(2,1),(2,first_rows_num), 1, colors.black)]))
    table.setStyle(tables.TableStyle([('BOX',(0,first_rows_num + 3),(0,first_rows_num + 2 + second_rows_num), 1, colors.black)]))
    table.setStyle(tables.TableStyle([('BOX',(2,first_rows_num + 3),(2,first_rows_num + 2 + second_rows_num), 1, colors.black)]))
    story.append(table)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    
    # additional notes
    story.append(Paragraph('Additional Notes on the Flight', style["section_title"]))
    sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
    story.append(sq)
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    story.append(Paragraph(self.OtherCommentsTextBox.toPlainText(), style["asmm"]))
    story.append(Paragraph('<br/><br/>', style["asmm"]))
    
    
    # images
    if self.images_pdf_path:
        story.append(Paragraph('Images Included in the PDF Report', style["section_title"]))
        sq = semi_square(-10, -13, -10, 15, page_w-70, -13, 2, 'black')
        story.append(sq)
        story.append(Paragraph('<br/><br/>', style["asmm"]))
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
            story.append(Paragraph('<br/>', style["asmm"]))
            data = [[Paragraph('<u>Figure ' + str(i + 1) + ':</u>', style['figure_number']),
                     Paragraph(self.im_textbox[i].text(), style['figure_caption'])]]
            table=tables.Table(data, colWidths=[100, 400], rowHeights=40)
            table.setStyle(tables.TableStyle([('VALIGN',(0,0),(1,0),'TOP')]))
            story.append(table)
            story.append(Paragraph('<br/><br/>', style["asmm"]))
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

    