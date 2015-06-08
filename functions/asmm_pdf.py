# -*- coding: utf-8 -*-

'''
Created on Sep 1, 2014

@author: henry
'''

import datetime
import time
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QDate
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from functions.signs_and_figures import tick, line, square


def create_asmm_pdf(self, out_file_name_pdf):

    ############################
    # Document Preparation
    ############################
    
	# création du document
    formatted_time = time.ctime()
    template = canvas.Canvas(out_file_name_pdf, pagesize=A4, bottomup=0)
    template.setFillColor('black')
    page_w, page_h = A4
    deb_page = 0
    
	# polices
    fontname1 = '../fonts/LiberationSerif-Regular.ttf'
    fontname2 = '../fonts/LiberationSans-Regular.ttf'
    fontname3 = '../fonts/LiberationSans-Italic.ttf'
    pdfmetrics.registerFont(TTFont('Times', fontname1))
    pdfmetrics.registerFont(TTFont('Arial', fontname2))
    pdfmetrics.registerFont(TTFont('Ariali', fontname3))

	# styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='asmm_title', fontName='Times', alignment=TA_CENTER, fontSize=16, textColor='red'))
    styles.add(ParagraphStyle(name='asmm_par', fontName='Arial', alignment=TA_JUSTIFY, fontSize=12))
    styles.add(ParagraphStyle(name='asmm_par_sl', fontName='Arial', alignment=TA_JUSTIFY, fontSize=10))
    styles.add(ParagraphStyle(name='asmm_par_tl', fontName='Arial', alignment=TA_LEFT, fontSize=14))

	# date
    template.setFont("Arial",10)
    pos_x_dt, pos_y_dt = 500, 40
    ptext = time.strftime("%Y/%m/%d")
    template.drawString(pos_x_dt, pos_y_dt, ptext)
    template.setFont("Arial",12)

	# titre
    title = 'ASMM Creator'
    tl = Paragraph(title, styles["asmm_title"])
    w, h = tl.wrapOn(template, 200, 100)
    pos_x_tl = page_w/2 - w/2
    pos_y_tl = 50
    tl.drawOn(template, pos_x_tl, pos_y_tl)
    sq = square(-100, 0, 200, -22, 1.5, 'red')
    sq.wrapOn(template, 300, 100)
    sq.drawOn(template, page_w/2, pos_y_tl+1)


    ############################
    # Flight Information
    ############################
    template.setFont("Arial",10)
    num_page='Page #%s' % template.getPageNumber()
    template.drawString(25, 40, num_page)
    template.setFont("Arial",12)
    title = 'Flight Information'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)
    pos_x_tl1, pos_y_tl1 = 25, pos_y_tl+50
    tl.drawOn(template, pos_x_tl1, pos_y_tl1)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl1, pos_y_tl1+3)
    ptext = 'Flight Number: %s' % self.flightNumberLine.text()
    template.drawString(pos_x_tl1+20, pos_y_tl1+20, ptext)
    ptext = 'Date: %s' % self.dateLine.date().toString(Qt.ISODate)
    template.drawString(pos_x_tl1+20, pos_y_tl1+40, ptext)
    ptext = 'Campaign: %s' % self.campaignLine.text()
    template.drawString(pos_x_tl1+20, pos_y_tl1+60, ptext)
    ptext = 'Mission Scientist: %s' % self.missionSciLine.text()
    template.drawString(pos_x_tl1+20, pos_y_tl1+80, ptext)
    ofx = 280
    ptext = 'Flight Manager: %s' % self.flightManagerLine.text()
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+20, ptext)
    ptext = 'Platform/Aircraft: %s' % self.platformLine.text()
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+40, ptext)
    ptext = 'Operator: %s' % self.operatorLine.text()
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+60, ptext)
    ptext = 'Country: %s' % self.countryLine.text()
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+80, ptext)

    
    ###########################
    # Metadata Contact Info
    ###########################
    title = 'Contact Information'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)
    pos_x_tl2, pos_y_tl2 = 25, pos_y_tl1+120
    if pos_y_tl2+60 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl2 = 80
    tl.drawOn(template, pos_x_tl2, pos_y_tl2)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl2, pos_y_tl2+3)
    ptext = 'Name: %s' % self.contactNameLine.text()
    template.drawString(pos_x_tl2+20, pos_y_tl2+20, ptext)
    ptext = 'Role: %s' % self.contactRoleBox.currentText()
    template.drawString(pos_x_tl2+20, pos_y_tl2+40, ptext)
    ptext = 'E-mail: %s' % self.contactEmailLine.text()
    template.drawString(pos_x_tl2+20, pos_y_tl2+60, ptext)


    ############################
    # Scientific Aims
    ############################
    title = 'Scientific Aims'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)
    pos_x_tl3, pos_y_tl3 = 25, pos_y_tl2+100
    if pos_y_tl3+160 >= 800:
	template.setFont("Arial",10)
	template.showPage()
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl3 = 80
    tl.drawOn(template, pos_x_tl3, pos_y_tl3)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl3, pos_y_tl3+3)
    pos_y = [20,40,60,100,120,140,160,20,40,60,80,120,140,160,20,40,60,80,140,160]
    pos_x = [60,60,60,80,80,80,80,250,270,270,270,250,250,250,430,430,430,430,450,450]
    box_c = ['satelliteCalVal','anthroPollution','mesoscaleImpacts','cloudMicrophysics','cloudDynamics','cloudRadiative','cloudConvection','gasChem','gasChemOxidants','gasChemOrganics','gasChemOther','aerosol','aerosolMicrophysical','aerosolRadiative','radiation','radiationAtmosSpectroscopy','radiationSurfProperties','radiationOther','blCloud','blDynamics']
    name_c = ['Satellite Cal/Val','Anthropogenic pollution','Mesoscale atmospheric impacts','Microphysics','Dynamics','Radiation properties','Convection dynamics','Gas chemistry','Oxydants','Organics','Other','Aerosol','Cloud microphysical impacts','Radiative properties/impacts','Radiation','Atmospheric spectroscopy','Surf. properties/retrievals','Other','Cloud','Dynamics']
    check_boxes_loop(pos_x,pos_y,pos_y_tl3,box_c,name_c,self.scientific_aims_check_dict,template)
    ptext = 'Cloud:'
    template.drawString(48, pos_y_tl3+80, ptext)
    ptext = 'Boundary-layer:'
    template.drawString(418, pos_y_tl3+120, ptext)
    if self.SAOtherTextBox.toPlainText():
	p = Paragraph(unicode(self.SAOtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h1 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h1 = p.wrapOn(template, 100, 100)
    offset1 = 180
    if pos_y_tl3+offset1+h1 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl3 = 80
	offset1 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl3+offset1, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl3+offset1+3)
    pos_y = pos_y_tl3 - h1 + offset1 + 30
    p.drawOn(template, 60, pos_y)


    ############################
    # Geographical Region
    ############################
    title = 'Geographical Region'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)
    if pos_y_tl3 == 80 and deb_page == 0:
	pos_x_tl4, pos_y_tl4 = 25, pos_y_tl3 + h + 40 +  h1
    else:
	pos_x_tl4, pos_y_tl4 = 25, pos_y_tl3 + h + 220 + h1
    if pos_y_tl4+90 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl4 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl4, pos_y_tl4)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl4, pos_y_tl4+3)
    ptext = 'North / South Latitudes (N/S): %s / %s' % (self.northBoundLatitudeLine.text(), self.southBoundLatitudeLine.text())
    template.drawString(pos_x_tl4+20, pos_y_tl4+20, ptext)
    ptext = 'West / East Latitudes (W/E): %s / %s' % (self.westBoundLongitudeLine.text(), self.eastBoundLongitudeLine.text())
    template.drawString(pos_x_tl4+300, pos_y_tl4+20, ptext)
    ptext = 'Min / Max Altitudes (m): %s / %s' % (self.minAltitudeLine.text(), self.maxAltitudeLine.text())
    template.drawString(pos_x_tl4+20, pos_y_tl4+40, ptext)
    pos_y = [70,70,70,70,90,90,90,90]
    pos_x = [80,210,340,470,80,210,340,470]
    box_c = ['polar','midLatitudes','subTropical','tropical','maritime','continental','oceanicIslands','other']
    name_c = ['Polar','Mid-latitudes','Sub-tropical','Tropical','Maritime','Continental','Oceanic Islands','Other']
    check_boxes_loop(pos_x,pos_y,pos_y_tl4,box_c,name_c,self.geographical_region_check_dict,template)
    if self.GROtherTextBox.toPlainText():
	p = Paragraph(unicode(self.GROtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h2 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h2 = p.wrapOn(template, 100, 100)
    offset2 = 110
    if pos_y_tl4+offset2+h2 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl4 = 80
	offset2 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl4+offset2, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl4+offset2+3)
    pos_y = pos_y_tl4 - h2 + offset2 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Atmospheric Features
    ############################
    title = 'Atmospheric Synoptic Features'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 300, 100)
    if pos_y_tl4 == 80 and deb_page == 0:
	pos_x_tl5, pos_y_tl5 = 25, pos_y_tl4 + h + 40 +  h2
    else:
	pos_x_tl5, pos_y_tl5 = 25, pos_y_tl4 + h + 160 + h2
    if pos_y_tl5+120 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl5 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl5, pos_y_tl5)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl5, pos_y_tl5+3)
    pos_y = [20,40,60,80,100,120,20,40,60,80,100,120,20,40,60,80,100,120]
    pos_x = [60,80,80,60,60,60,240,240,240,240,240,240,420,420,420,420,420,420]
    box_c = ['stationary','stationaryAnticyclonic','stationaryCyclonic','warmFront','warmConveyorBelt','coldFront','occludedFront','warmSector','postColdFrontalAirMass','arcticColdAirOutbreak','orographicInfluence','seaBreezeFront','stratosphericFold','extendedConvergenceLine','easterlyWave','equatorialWave','tropycalCyclone','mesoscaleOrganizedConvection']
    name_c = ['Stationary','Anticyclonic','Cyclonic','Warm front','Warm conveyor belt','Cold front','Occluded front','Warm sector','Post-cold-frontal air mass','Arctic cold-air outbreak','Orographic influence','Sea-breeze front','Stratospheric fold / intrusion','Extended convergence line','Easterly wave','Equatorial wave','Tropical cyclone','Mesoscale organized convection']
    check_boxes_loop(pos_x,pos_y,pos_y_tl5,box_c,name_c,self.atmospheric_features_check_dict,template)
    if self.AFOtherTextBox.toPlainText():
	p = Paragraph(unicode(self.AFOtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h3 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h3 = p.wrapOn(template, 100, 100)
    offset3 = 140
    if pos_y_tl5+offset3+h3 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl5 = 80
	offset3 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl5+offset3, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl5+offset3+3)
    pos_y = pos_y_tl5 - h3 + offset3 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Cloud Types
    ############################
    title = 'Cloud Types and Forms Sampled During Flight'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl5 == 80 and deb_page == 0:
	pos_x_tl6, pos_y_tl6 = 25, pos_y_tl5 + h + 40 +  h3
    else:
	pos_x_tl6, pos_y_tl6 = 25, pos_y_tl5 + h + 180 + h3
    if pos_y_tl6+120 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl6 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl6, pos_y_tl6)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl6, pos_y_tl6+3)
    pos_y = [20,40,60,80,100,20,40,60,80,100,20,40,60,80]
    pos_x = [60,60,60,60,60,220,220,220,220,220,420,420,420,420]
    box_c = ['waterClouds','mixedPhaseClouds','iceClouds','cirrus','contrails','stratocumulus','shallowCumulus','cumulusCongestus','cumulonimbusToweringCumulus','altostratusAltocumulus','waveClouds','deepFrontalStratiformClouds','cloudFreeAboveAircraft','cloudFreeBelowAircraft']
    name_c = ['Water clouds','Mixed-phase clouds','Ice clouds','Cirrus','Contrails','Stratocumulus','Shallow cumulus','Cumulus congestus','Cumulonimbus / towering cumulus','Altostratus / altocumulus','Wave clouds','Deep frontal statiform clounds','Cloud-free above aircraft','Cloud-free below aircraft']
    check_boxes_loop(pos_x,pos_y,pos_y_tl6,box_c,name_c,self.cloud_types_check_dict,template)
    if self.CTOtherTextBox.toPlainText():
	p = Paragraph(unicode(self.CTOtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h4 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h4 = p.wrapOn(template, 100, 100)
    offset4 = 120
    if pos_y_tl6+offset4+h4 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl6 = 80
	offset4 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl6+offset4, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl6+offset4+3)
    pos_y = pos_y_tl6 - h4 + offset4 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Particles Sampled
    ############################
    title = 'Cloud, Precipitation and Aerosol Particles Sampled'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl6 == 80 and deb_page == 0:
	pos_x_tl7, pos_y_tl7 = 25, pos_y_tl6 + h + 40 +  h4
    else:
	pos_x_tl7, pos_y_tl7 = 25, pos_y_tl6 + h + 160 + h4
    if pos_y_tl7+100 >= 800:
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	template.showPage()
	pos_y_tl7 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl7, pos_y_tl7)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl7, pos_y_tl7+3)
    pos_y = [20,40,60,80,20,40,60,80,20,40,60,80]
    pos_x = [60,60,60,60,240,240,240,240,420,420,420,420]
    box_c = ['rain','drizzle','droplets','pristineIceCrystals','snowOrAggregates','graupelOrHail','seaSaltAerosol','continentalAerosol','urbanPlume','biomassBurning','desertOrMineralDust','volcanicAsh']
    name_c = ['Rain','Drizzle','Droplets (liquid)','Pristine ice crystals','Snow / aggregates','Graupel / hail','Sea-salt aerosol','Continental aerosol','Urban plume','Biomass burning','Desert / mineral dust','Volcanic ashes']
    check_boxes_loop(pos_x,pos_y,pos_y_tl7,box_c,name_c,self.particles_sampled_check_dict,template)
    if self.PSOtherTextBox.toPlainText():
	p = Paragraph(unicode(self.PSOtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h5 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h5 = p.wrapOn(template, 100, 100)
    offset5 = 100
    if pos_y_tl7+offset5+h5 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl7 = 80
	offset5 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl7+offset5, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl7+offset5+3)
    pos_y = pos_y_tl7 - h5 + offset5 + 30
    p.drawOn(template, 60, pos_y)
 

    ############################
    # Surfaces Overflown
    ############################
    title = 'Land or Ocean Surfaces Overflown'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl7 == 80 and deb_page == 0:
	pos_x_tl8, pos_y_tl8 = 25, pos_y_tl7 + h + 40 +  h5
    else:
	pos_x_tl8, pos_y_tl8 = 25, pos_y_tl7 + h + 140 + h5
    if pos_y_tl8+100 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl8 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl8, pos_y_tl8)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl8, pos_y_tl8+3)
    pos_y = [20,40,60,80,20,40,60,80,20,40,60,80]
    pos_x = [60,60,60,60,240,240,240,240,420,420,420,420]    
    box_c = ['ocean','semiArid','seaIce','desert','snow','urban','lakeIce','mountainous','vegetation','hilly','forest','flat']
    name_c = ['Ocean','Semi-arid','Sea-ice','Desert','Snow','Urban','Lake-ice','Mountainous','Vegetation','Hilly','Forest','Flat']
    check_boxes_loop(pos_x,pos_y,pos_y_tl8,box_c,name_c,self.surfaces_overflown_check_dict,template)
    if self.SOOtherTextBox.toPlainText():
	p = Paragraph(unicode(self.SOOtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h6 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h6 = p.wrapOn(template, 100, 100)
    offset6 = 100
    if pos_y_tl8+offset6+h6 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl8 = 80
	offset6 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl8+offset6, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl8+offset6+3)
    pos_y = pos_y_tl8 - h6 + offset6 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Altitude Ranges
    ############################
    title = 'Altitude Ranges of Measurement'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl8 == 80 and deb_page == 0:
	pos_x_tl9, pos_y_tl9 = 25, pos_y_tl8 + h + 40 +  h6
    else:
	pos_x_tl9, pos_y_tl9 = 25, pos_y_tl8 + h + 140 + h6
    if pos_y_tl9+100 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl9 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl9, pos_y_tl9)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl9, pos_y_tl9+3)
    pos_y = [20,40,60,80,20,40,60,80]
    pos_x = [150,170,170,170,330,330,330,330]    
    box_c = ['boundaryLayer','blNearSurface','blSubCloud','blInCloud','lowerTroposphere','midTroposphere','upperTroposphere','lowerStratosphere']
    name_c = ['Boundary-layer','near-surface','sub-cloud','in-cloud','Lower troposphere','Mid troposphere','Upper troposphere','Lower stratosphere']
    check_boxes_loop(pos_x,pos_y,pos_y_tl9,box_c,name_c,self.altitude_ranges_check_dict,template)
    if self.AROtherTextBox.toPlainText():
	p = Paragraph(unicode(self.AROtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h7 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h7 = p.wrapOn(template, 100, 100)
    offset7 = 100
    if pos_y_tl9+offset7+h7 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl9 = 80
	offset7 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl9+offset7, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl9+offset7+3)
    pos_y = pos_y_tl9 - h7 + offset7 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Flight Types
    ############################
    title = 'Types of Flight Manoeuvre'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl9 == 80 and deb_page == 0:
	pos_x_tl10, pos_y_tl10 = 25, pos_y_tl9 + h + 40 +  h7
    else:
	pos_x_tl10, pos_y_tl10 = 25, pos_y_tl9 + h + 140 + h7
    if pos_y_tl10+80 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl10 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl10, pos_y_tl10)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl10, pos_y_tl10+3)
    pos_y = [20,40,60,20,40,60,20,40,60]
    pos_x = [60,80,80,240,240,240,420,420,420]      
    box_c = ['straightLevelRuns','stackedStraightLevelRuns','separatedStraightLevelRuns','racetracks','orbits','lagrangianDescents','deepProfileAscentDescents','dropsondeDeployed','selfCalibration']
    name_c = ['Straight / level runs','stacked','separated','Racetracks','Orbits','Lagrangian descents','Deep profile ascents / descents','Dropsonde deployed','Self-calibration']
    check_boxes_loop(pos_x,pos_y,pos_y_tl10,box_c,name_c,self.flight_types_check_dict,template)
    if self.FTOtherTextBox.toPlainText():
	p = Paragraph(unicode(self.FTOtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h8 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h8 = p.wrapOn(template, 100, 100)
    offset8 = 80
    if pos_y_tl10+offset8+h8 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl10 = 80
	offset8 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl10+offset8, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl10+offset8+3)
    pos_y = pos_y_tl10 - h8 + offset8 + 30
    p.drawOn(template, 60, pos_y)
    

    ############################
    # Satellite coordination
    ############################
    title = 'Satellite Coordination'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl10 == 80 and deb_page == 0:
	pos_x_tl11, pos_y_tl11 = 25, pos_y_tl10 + h + 40 +  h8
    else:
	pos_x_tl11, pos_y_tl11 = 25, pos_y_tl10 + h + 120 + h8
    if pos_y_tl11+100 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl11 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl11, pos_y_tl11)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl11, pos_y_tl11+3)
    pos_y = [40,60,80,100,40,60,80,100,20,40,60,80,100]
    pos_x = [80,80,80,80,260,260,240,240,420,420,420,420,420]      
    box_c = ['polarMetop','polarNpoess','polarAtrain','polarOther','geosynchMsg','geosynchOther','modis','cloudsat','caliop','iasi','airs','cris','amsuMhs']
    name_c = ['METOP','NPOESS','A-train','Other','MSG','Other','MODIS','Cloudsat','CALIOP','IASI','AIRS','CriS','AMSU / MHS']
    check_boxes_loop(pos_x,pos_y,pos_y_tl11,box_c,name_c,self.satellite_coordination_check_dict,template)
    ptext = 'Polar:'
    template.drawString(48, pos_y_tl11+20, ptext)
    ptext = 'Geosynch:'
    template.drawString(228, pos_y_tl11+20, ptext)
    if self.SCOtherTextBox.toPlainText():
	p = Paragraph(unicode(self.SCOtherTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h9 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h9 = p.wrapOn(template, 100, 100)
    offset9 = 120
    if pos_y_tl11+offset9+h9 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl11 = 80
	offset9 = 0
	deb_page = 0
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl11+offset9, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl11+offset9+3)
    pos_y = pos_y_tl11 - h9 + offset9 + 30
    p.drawOn(template, 60, pos_y)
 
    
    ############################
    # Surface Observations
    ############################
    title = 'Supporting Surface-Based Observations'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl11 == 80 and deb_page == 0:
	pos_x_tl12, pos_y_tl12 = 25, pos_y_tl11 + h + 40 +  h9
    else:
	pos_x_tl12, pos_y_tl12 = 25, pos_y_tl11 + h + 160 + h9
	
    if (len(self.ground_site_list) * 20 + 40 + pos_y_tl12) >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	offset_tmp1 = 0
	pos_y_tl12 = 80
	deb_page = 1
    tl.drawOn(template, pos_x_tl12, pos_y_tl12)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl12, pos_y_tl12+3)
    
    
    ptext = 'Ground Sites:'
    template.drawString(60, pos_y_tl12+20, ptext)
    offset_tmp1 = 40
    i1 = 0
    template.setFont("Arial",10)
    for item in self.ground_site_list:
	template.drawString(80, pos_y_tl12+offset_tmp1, unicode(item))
	offset_tmp1 = offset_tmp1 + 20
	i1 = i1 + 1
    if not self.ground_site_list:
	template.drawString(80, pos_y_tl12+offset_tmp1, 'NoNe')
	i1 = i1 + 1
    t = square(0, 0, 200, 20*i1+3, 1, 'black')
    t.wrapOn(template, 300, 300)
    t.drawOn(template, 60, pos_y_tl12+25)
    template.setFont("Arial",12)
    
    
    ptext = 'ARM Sites:'
    template.drawString(320, pos_y_tl12+20, ptext)
    offset_tmp2 = 40
    i2 = 0
    template.setFont("Arial",10)
    for item in self.arm_site_list:
	template.drawString(340, pos_y_tl12+offset_tmp2, unicode(item))
	offset_tmp2 = offset_tmp2 + 20
	i2 = i2 + 1
    if not self.arm_site_list:
	template.drawString(340, pos_y_tl12+offset_tmp2, 'NoNe')
	i2 = i2 + 1
    t = square(0, 0, 200, 20*i2+3, 1, 'black')
    t.wrapOn(template, 300, 300)
    t.drawOn(template, 320, pos_y_tl12+25)
    template.setFont("Arial",12)
    
      
    if offset_tmp1 < offset_tmp2:
	offset_tmp1 = offset_tmp2
	i1 = i2
    if (len(self.research_vessel_list) * 20 + offset_tmp1 + 40 + pos_y_tl12) >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	offset_tmp1 = 0
	pos_y_tl12 = 80
	deb_page = 0
    
   
    ptext = 'Research Vessels:'
    if deb_page == 1:
	template.drawString(60, pos_y_tl12+60+20*i1, ptext)
	offset_tmp3 = pos_y_tl12+80+20*i1
    elif deb_page == 0 and pos_y_tl12 > 80:
      template.drawString(60, pos_y_tl12+60+20*i1, ptext)
      offset_tmp3 = pos_y_tl12+80+20*i1
    else:
	template.drawString(60, pos_y_tl12, ptext)
	offset_tmp3 = pos_y_tl12+20
    i3 = 0
    template.setFont("Arial",10)
    for item in self.research_vessel_list:
	template.drawString(80, offset_tmp3, unicode(item))
	offset_tmp3 = offset_tmp3 + 20
	i3 = i3 + 1
    if not self.research_vessel_list:
	template.drawString(80, offset_tmp3, 'NoNe')
	i3 = i3 + 1
    t = square(0, 0, 200, 20*i3+3, 1, 'black')
    t.wrapOn(template, 300, 300)
    if deb_page == 0 and pos_y_tl12 > 80:
	t.drawOn(template, 60, pos_y_tl12+65+20*i1)
    elif deb_page == 0 and pos_y_tl12 == 80:
	t.drawOn(template, 60, pos_y_tl12+5)
    else:
	t.drawOn(template, 60, pos_y_tl12+65+20*i1)
    template.setFont("Arial",12)
    

    ptext = 'ARM Mobile sites:'
    if deb_page == 1:
	template.drawString(320, pos_y_tl12+60+20*i1, ptext)
	offset_tmp4 = pos_y_tl12+80+20*i1
    elif deb_page == 0 and pos_y_tl12 > 80:
      template.drawString(320, pos_y_tl12+60+20*i1, ptext)
      offset_tmp4 = pos_y_tl12+80+20*i1
    else:
	template.drawString(320, pos_y_tl12, ptext)
	offset_tmp4 = pos_y_tl12+20
    i4 = 0
    template.setFont("Arial",10)
    for item in self.arm_mobile_list:
	template.drawString(340, offset_tmp4, unicode(item))
	offset_tmp4 = offset_tmp4 + 20
	i4 = i4 + 1
    if not self.arm_mobile_list:
	template.drawString(340, offset_tmp4, 'NoNe')
	i4 = i4 + 1
    t = square(0, 0, 200, 20*i4+3, 1, 'black')
    t.wrapOn(template, 300, 300)
    if deb_page == 0 and pos_y_tl12 > 80:
	t.drawOn(template, 320, pos_y_tl12+65+20*i1)
    elif deb_page == 0 and pos_y_tl12 == 80:
	t.drawOn(template, 320, pos_y_tl12+5)
    else:
	t.drawOn(template, 320, pos_y_tl12+65+20*i1)
    template.setFont("Arial",12)

    
    #############################
    # Other Comments
    ############################
    if offset_tmp3 < offset_tmp4:
	offset_tmp3 = offset_tmp4
	i3 = i4
    title = 'Additional Notes on the Flight'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl12 == 80 and deb_page == 1:
	pos_x_tl13, pos_y_tl13 = 25, pos_y_tl12 + i3*20 + i1*20 + 60 + 60
    elif pos_y_tl12 == 80 and deb_page == 0:
	pos_x_tl13, pos_y_tl13 = 25, pos_y_tl12 + i3*20 + 60
    elif pos_y_tl12 > 80 and deb_page == 0:
	#pos_x_tl13, pos_y_tl13 = 25, offset_tmp3 + i3*20
	pos_x_tl13, pos_y_tl13 = 25, pos_y_tl12 + i3*20 + i1*20 + 60 + 60
    else:
	pos_x_tl13, pos_y_tl13 = 25, offset_tmp3 + i3*20 + 40	
    if self.OtherCommentsTextBox.toPlainText():
	p = Paragraph(unicode(self.OtherCommentsTextBox.toPlainText()), styles["asmm_par_sl"])
	c, h10 = p.wrapOn(template, 500, 500)
    else:
	ptext = 'No Comments'
	p = Paragraph(ptext, styles["asmm_par_sl"])
	c, h10 = p.wrapOn(template, 100, 100)
    offset10 = 20
    if pos_y_tl13+h10+offset10 >= 800:
	template.showPage()
	template.setFont("Arial",10)
	num_page='Page #%s' % template.getPageNumber()
	template.drawString(25, 40, num_page)
	template.setFont("Arial",12)
	pos_y_tl13 = 80
	deb_page = 1
    template.setFont("Arial",12)
    tl.drawOn(template, pos_x_tl13, pos_y_tl13)
    sq = square(-10, 0, page_w-30, -20, 1.5, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl13, pos_y_tl13+3)
    ptext = 'Comments:'
    template.drawString(48, pos_y_tl13+offset10, ptext)
    ln = line(0,0,70,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, 48, pos_y_tl13+offset10+3)
    pos_y = pos_y_tl13 - h10 + offset10 + 30
    p.drawOn(template, 60, pos_y)

    #############################
    # Document generation
    #############################
    template.save()
    
    
def check_boxes_loop(xc,yc,ofc,bc,nc,itemc,tc):
    tc.setFont("Arial",10)
    for key, value in itemc.iteritems():
	idx = bc.index(value)
	tc.drawString(int(xc[idx]), (int(yc[idx])+ofc), nc[idx])
	if key.isChecked():
	    t = tick(0,0,8,1,1.5,'red')
	else:
	    t = tick(0,0,8,0,1.5,'red')
	t.wrapOn(tc, 50, 50)
	t.drawOn(tc, int(xc[idx])-12, (int(yc[idx])+ofc))
    tc.setFont("Arial",12)
    