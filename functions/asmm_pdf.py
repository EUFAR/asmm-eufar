# -*- coding: utf-8 -*-

import time
from PyQt5.QtCore import Qt
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib import utils
from functions.signs_and_figures import tick, line, square, semi_square
from PyQt5.QtWidgets import QCheckBox


def create_asmm_pdf(self, out_file_name_pdf):

    ############################
    # Document Preparation
    ############################
    
    # création du document
    template = canvas.Canvas(out_file_name_pdf, pagesize=A4, bottomup=0)
    template.setFillColor('black')
    page_w, page_h = A4  # @UnusedVariable
    deb_page = 0
    
    # polices
    fontname1 = 'font/SourceSansPro-Regular.ttf'
    pdfmetrics.registerFont(TTFont('Times', fontname1))
    pdfmetrics.registerFont(TTFont('Arial', fontname1))
    pdfmetrics.registerFont(TTFont('Ariali', fontname1))

    # styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='asmm_title', fontName='Times', alignment=TA_CENTER, fontSize=16, textColor='red'))
    styles.add(ParagraphStyle(name='asmm_par', fontName='Times', alignment=TA_JUSTIFY, fontSize=10))
    styles.add(ParagraphStyle(name='asmm_par_sl', fontName='Arial', alignment=TA_JUSTIFY, fontSize=10))
    styles.add(ParagraphStyle(name='asmm_par_tl', fontName='Times', alignment=TA_LEFT, fontSize=16))
    styles.add(ParagraphStyle(name='asmm_title2', fontName='Arial', alignment=TA_CENTER, fontSize=22, textColor='black', leading=24))
    styles.add(ParagraphStyle(name='asmm_figure', fontName='Times', alignment=TA_CENTER, fontSize=12))

    # date
    template.setFont("Arial",10)
    pos_x_dt, pos_y_dt = 515, 30
    ptext = time.strftime("%Y-%m-%d")
    template.drawString(pos_x_dt, pos_y_dt, ptext)
    template.setFont("Times",12)

    # titre
    title = 'Airborne Science Mission Metadata Report'
    tl = Paragraph(title, styles["asmm_title2"])
    w, h = tl.wrapOn(template, 400, 200)  # @UnusedVariable
    pos_x_tl = page_w/2 - w/2
    pos_y_tl = 40
    tl.drawOn(template, pos_x_tl, pos_y_tl)
    sq = square(-173, 0, 348, 57, 2, 'black')
    sq.wrapOn(template, 300, 100)
    sq.drawOn(template, page_w/2, pos_y_tl+1)


    ############################
    # Flight Information
    ############################
    title = 'Flight Information'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)  # @UnusedVariable
    pos_x_tl1, pos_y_tl1 = 30, pos_y_tl+125
    tl.drawOn(template, pos_x_tl1, pos_y_tl1)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl1, pos_y_tl1+3)
    template.setFont("Times",10)
    template.drawString(pos_x_tl1+10, pos_y_tl1+25, 'Project acronym:')
    p = Paragraph(str(self.campaignLine.text()), styles["asmm_par_sl"])
    c, h = p.wrapOn(template, 150, 30)  # @UnusedVariable
    p.drawOn(template, pos_x_tl1+100, pos_y_tl1 + 25 - h + 10)
    ptext = 'Date:     %s' % self.dateLine.date().toString(Qt.ISODate)
    template.drawString(pos_x_tl1+10, pos_y_tl1+55, ptext)
    ptext = 'Flight Number:     %s' % self.flightNumberLine.text()
    template.drawString(pos_x_tl1+10, pos_y_tl1+85, ptext)
    ptext = 'Mission Scientist:     %s' % self.missionSciLine.text()
    template.drawString(pos_x_tl1+10, pos_y_tl1+115, ptext)
    ofx = 280
    ptext = 'Flight Manager:     %s' % self.flightManagerLine.text()
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+25, ptext)
    if self.aircraftList.currentText() == "Make a choice...":
        aircraft = ""
    elif self.aircraftList.currentText() == "Other...":
        aircraft = self.tmpAircraftLine.text()
    else:
        aircraft = self.aircraftList.currentText()
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+55, 'Aircraft:')
    p = Paragraph(str(aircraft), styles["asmm_par_sl"])
    c, h = p.wrapOn(template, 150, 30)  # @UnusedVariable
    p.drawOn(template, pos_x_tl1 + ofx + 50, pos_y_tl1 + 55 - h + 10)
    if self.operatorList.currentText() == "Make a choice...":
        operator = ""
    elif self.operatorList.currentText() == "Other...":
        operator = self.tmpOperatorLine.text()
    else:
        operator = self.operatorList.currentText()
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+85, 'Operator:')
    p = Paragraph(str(operator), styles["asmm_par_sl"])
    c, h = p.wrapOn(template, 200, 30)  # @UnusedVariable
    p.drawOn(template, pos_x_tl1 + ofx + 60, pos_y_tl1 + 85 - h + 10)
    if self.locationList.currentText() == "Make a choice..." or self.detailList.currentText() == "Make a choice...":
        country = ""
    else:
        country = self.detailList.currentText()
    ptext = 'Country:     %s' % country
    template.drawString(pos_x_tl1+ofx, pos_y_tl1+115, ptext)

    
    ###########################
    # Metadata Contact Info
    ###########################
    title = 'Contact Information'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)  # @UnusedVariable
    pos_x_tl2, pos_y_tl2 = 30, pos_y_tl1+192
    if pos_y_tl2+60 >= 800:
        template.showPage()
        pos_y_tl2 = 80
    tl.drawOn(template, pos_x_tl2, pos_y_tl2)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl2, pos_y_tl2+2)
    ptext = 'Name:     %s' % self.contactNameLine.text()
    template.drawString(pos_x_tl2+10, pos_y_tl2+25, ptext)
    if self.contactRoleBox.currentText() != "Make a choice...":
        ptext = 'Role:     %s' % self.contactRoleBox.currentText()
    else:
        ptext = 'Role:'
    template.drawString(pos_x_tl2+10, pos_y_tl2+55, ptext)
    ptext = 'E-mail:     %s' % self.contactEmailLine.text()
    template.drawString(pos_x_tl2+10, pos_y_tl2+85, ptext)


    ############################
    # Scientific Aims
    ############################
    title = 'Scientific Aims'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)  # @UnusedVariable
    pos_x_tl3, pos_y_tl3 = 30, pos_y_tl2+162
    if pos_y_tl3+160 >= 800:
        template.showPage()
        pos_y_tl3 = 80
    tl.drawOn(template, pos_x_tl3, pos_y_tl3)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl3, pos_y_tl3+2)
    pos_y = [20,40,60,100,120,140,160,20,40,60,80,120,140,160,20,40,60,80,140,160]
    pos_x = [60,60,60,80,80,80,80,250,270,270,270,250,250,250,430,430,430,430,450,450]
    box_c = ['satelliteCalVal','anthroPollution','mesoscaleImpacts','cloudMicrophysics','cloudDynam'
             'ics','cloudRadiative','cloudConvection','gasChem','gasChemOxidants','gasChemOrganics',
             'gasChemOther','aerosol','aerosolMicrophysical','aerosolRadiative','radiation','radiat'
             'ionAtmosSpectroscopy','radiationSurfProperties','radiationOther','blCloud','blDynamics']
    name_c = ['Satellite Cal/Val','Anthropogenic pollution','Mesoscale atmospheric impacts','Microp'
              'hysics','Dynamics','Radiation properties','Convection dynamics','Gas chemistry','Oxy'
              'dants','Organics','Other','Aerosol','Cloud microphysical impacts','Radiative propert'
              'ies/impacts','Radiation','Atmospheric spectroscopy','Surf. properties/retrievals','O'
              'ther','Cloud','Dynamics']
    check_boxes_loop(pos_x,pos_y,pos_y_tl3,box_c,name_c,self.scientific_aims_check_dict,template)
    ptext = 'Cloud:'
    template.drawString(48, pos_y_tl3+80, ptext)
    ptext = 'Boundary-layer:'
    template.drawString(418, pos_y_tl3+120, ptext)
    pos_y = pos_y_tl3 + 180
    if self.sa_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl3 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl3 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_5.count()):
            if isinstance(self.gridLayout_5.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_5.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_5.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.SAOtherTextBox.toPlainText():
        p = Paragraph(self.SAOtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h1 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h1 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    if pos_y + h1 >= 800:
        template.showPage()
        pos_y = 80
        deb_page = 0
    pos_y_tl3 = pos_y
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl3 + 18, pos_y_tl3, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl3 + 18, pos_y_tl3 + 3)
    pos_y = pos_y_tl3 - h1 + 30
    p.drawOn(template, 60, pos_y)


    ############################
    # Geographical Region
    ############################
    title = 'Geographical Region'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 200, 100)
    if pos_y_tl3 == 80 and deb_page == 0:
        pos_x_tl4, pos_y_tl4 = 30, pos_y_tl3 + h + 70 +  h1
    else:
        pos_x_tl4, pos_y_tl4 = 30, pos_y_tl3 + h + 220 + h1
    if pos_y_tl4+90 >= 800:
        template.showPage()
        pos_y_tl4 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl4, pos_y_tl4)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl4, pos_y_tl4+3)
    template.setFont("Times",12)
    ptext = 'Geographic Bounding Box:'
    template.drawString(pos_x_tl4+18, pos_y_tl4+25, ptext)
    ln = line(0,0,143,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl4+18, pos_y_tl4+25+3)
    template.setFont("Times",10)
    ptext = 'North/South latitudes:     %s / %s' % (self.northBoundLatitudeLine.text(), self.
                                                    southBoundLatitudeLine.text())
    template.drawString(pos_x_tl4+40, pos_y_tl4+45, ptext)
    ptext = 'West/East longitudes:     %s / %s' % (self.westBoundLongitudeLine.text(), self.
                                                   eastBoundLongitudeLine.text())
    template.drawString(pos_x_tl4+40, pos_y_tl4+65, ptext)
    ptext = 'Min/Max altitudes (m):     %s / %s' % (self.minAltitudeLine.text(), self.
                                                    maxAltitudeLine.text())
    template.drawString(pos_x_tl4+300, pos_y_tl4+45, ptext)
    template.setFont("Times",12)
    ptext = 'Geographic Situation:'
    template.drawString(pos_x_tl4+18, pos_y_tl4+95, ptext)
    template.setFont("Times",10)
    ln = line(0,0,116,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl4+18, pos_y_tl4+95+3)
    pos_y = [115,115,115,115,135,135,135,135]
    pos_x = [80,210,340,470,80,210,340,470]
    box_c = ['polar','midLatitudes','subTropical','tropical','maritime','continental','oceanicIslan'
             'ds','other']
    name_c = ['Polar','Mid-latitudes','Sub-tropical','Tropical','Maritime','Continental','Oceanic I'
              'slands','Other']
    check_boxes_loop(pos_x,pos_y,pos_y_tl4,box_c,name_c,self.geographical_region_check_dict,template)
    pos_y = pos_y_tl4 + 160
    if self.gr_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl4 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl4 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_8.count()):
            if isinstance(self.gridLayout_8.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_8.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_8.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.GROtherTextBox.toPlainText():
        p = Paragraph(self.GROtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h2 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h2 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl4 = pos_y
    if pos_y_tl4 + h2 >= 800:
        template.showPage()
        pos_y_tl4 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl4 + 18, pos_y_tl4, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl4 + 18, pos_y_tl4 + 3)
    pos_y = pos_y_tl4 - h2 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Atmospheric Features
    ############################
    title = 'Atmospheric Synoptic Features'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 300, 100)
    if pos_y_tl4 == 80 and deb_page == 0:
        pos_x_tl5, pos_y_tl5 = 30, pos_y_tl4 + h + 70 + h2
    else:
        pos_x_tl5, pos_y_tl5 = 30, pos_y_tl4 + h + 70 + h2
    if pos_y_tl5 + 120 >= 800:
        template.showPage()
        pos_y_tl5 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl5, pos_y_tl5)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl5, pos_y_tl5+3)
    pos_y = [20,40,60,80,100,120,20,40,60,80,100,120,20,40,60,80,100,120]
    pos_x = [60,80,80,60,60,60,240,240,240,240,240,240,420,420,420,420,420,420]
    box_c = ['stationary','stationaryAnticyclonic','stationaryCyclonic','warmFront','warmConveyorBe'
             'lt','coldFront','occludedFront','warmSector','postColdFrontalAirMass','arcticColdAirO'
             'utbreak','orographicInfluence','seaBreezeFront','stratosphericFold','extendedConverge'
             'nceLine','easterlyWave','equatorialWave','tropycalCyclone','mesoscaleOrganizedConvect'
             'ion']
    name_c = ['Stationary','Anticyclonic','Cyclonic','Warm front','Warm conveyor belt','Cold front',
              'Occluded front','Warm sector','Post-cold-frontal air mass','Arctic cold-air outbreak',
              'Orographic influence','Sea-breeze front','Stratospheric fold / intrusion','Extended '
              'convergence line','Easterly wave','Equatorial wave','Tropical cyclone','Mesoscale or'
              'ganized convection']
    check_boxes_loop(pos_x,pos_y,pos_y_tl5,box_c,name_c,self.atmospheric_features_check_dict,template)
    pos_y = pos_y_tl5 + 145
    if self.af_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl5 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl5 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_9.count()):
            if isinstance(self.gridLayout_9.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_9.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_9.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.AFOtherTextBox.toPlainText():
        p = Paragraph(self.AFOtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h3 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h3 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl5 = pos_y
    if pos_y_tl5 + h3 >= 800:
        template.showPage()
        pos_y_tl5 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl5 + 18, pos_y_tl5, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl5 + 18, pos_y_tl5 + 3)
    pos_y = pos_y_tl5 - h3 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Cloud Types
    ############################
    title = 'Cloud Types and Forms Sampled During Flight'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl5 == 80 and deb_page == 0:
        pos_x_tl6, pos_y_tl6 = 30, pos_y_tl5 + h + 70 +  h3
    else:
        pos_x_tl6, pos_y_tl6 = 30, pos_y_tl5 + h + 70 + h3
    if pos_y_tl6 + 120 >= 800:
        template.showPage()
        pos_y_tl6 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl6, pos_y_tl6)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl6, pos_y_tl6+3)
    pos_y = [20,40,60,80,100,20,40,60,80,100,20,40,60,80]
    pos_x = [60,60,60,60,60,220,220,220,220,220,420,420,420,420]
    box_c = ['waterClouds','mixedPhaseClouds','iceClouds','cirrus','contrails','stratocumulus','sha'
             'llowCumulus','cumulusCongestus','cumulonimbusToweringCumulus','altostratusAltocumulus',
             'waveClouds','deepFrontalStratiformClouds','cloudFreeAboveAircraft','cloudFreeBelowAir'
             'craft']
    name_c = ['Water clouds','Mixed-phase clouds','Ice clouds','Cirrus','Contrails','Stratocumulus',
              'Shallow cumulus','Cumulus congestus','Cumulonimbus / towering cumulus','Altostratus '
              '/ altocumulus','Wave clouds','Deep frontal statiform clounds','Cloud-free above airc'
              'raft','Cloud-free below aircraft']
    check_boxes_loop(pos_x,pos_y,pos_y_tl6,box_c,name_c,self.cloud_types_check_dict,template)
    pos_y = pos_y_tl6 + 125
    if self.ct_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl6 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl6 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_10.count()):
            if isinstance(self.gridLayout_10.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_10.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_10.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.CTOtherTextBox.toPlainText():
        p = Paragraph(self.CTOtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h4 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h4 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl6 = pos_y
    if pos_y_tl6 + h4 >= 800:
        template.showPage()
        pos_y_tl6 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl6 + 18, pos_y_tl6, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl6 + 18, pos_y_tl6 + 3)
    pos_y = pos_y_tl6 - h4 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Particles Sampled
    ############################
    title = 'Cloud, Precipitation and Aerosol Particles Sampled'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl6 == 80 and deb_page == 0:
        pos_x_tl7, pos_y_tl7 = 30, pos_y_tl6 + h + 70 + h4
    else:
        pos_x_tl7, pos_y_tl7 = 30, pos_y_tl6 + h + 70 + h4
    if pos_y_tl7 + 100 >= 800:
        template.showPage()
        pos_y_tl7 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl7, pos_y_tl7)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl7, pos_y_tl7+3)
    pos_y = [20,40,60,80,20,40,60,80,20,40,60,80]
    pos_x = [60,60,60,60,240,240,240,240,420,420,420,420]
    box_c = ['rain','drizzle','droplets','pristineIceCrystals','snowOrAggregates','graupelOrHail',
             'seaSaltAerosol','continentalAerosol','urbanPlume','biomassBurning','desertOrMineralDu'
             'st','volcanicAsh']
    name_c = ['Rain','Drizzle','Droplets (liquid)','Pristine ice crystals','Snow / aggregates','Gra'
              'upel / hail','Sea-salt aerosol','Continental aerosol','Urban plume','Biomass burning',
              'Desert / mineral dust','Volcanic ashes']
    check_boxes_loop(pos_x,pos_y,pos_y_tl7,box_c,name_c,self.particles_sampled_check_dict,template)
    pos_y = pos_y_tl7 + 105
    if self.ps_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl7 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl7 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_11.count()):
            if isinstance(self.gridLayout_11.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_11.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_11.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.PSOtherTextBox.toPlainText():
        p = Paragraph(self.PSOtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h5 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h5 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl7 = pos_y
    if pos_y_tl7 + h5 >= 800:
        template.showPage()
        pos_y_tl7 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl7 + 18, pos_y_tl7, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl7 + 18, pos_y_tl7 + 3)
    pos_y = pos_y_tl7 - h5 + 30
    p.drawOn(template, 60, pos_y)
 

    ############################
    # Surfaces Overflown
    ############################
    title = 'Land or Ocean Surfaces Overflown'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl7 == 80 and deb_page == 0:
        pos_x_tl8, pos_y_tl8 = 30, pos_y_tl7 + h + 70 + h5
    else:
        pos_x_tl8, pos_y_tl8 = 30, pos_y_tl7 + h + 70 + h5
    if pos_y_tl8 + 100 >= 800:
        pos_y_tl8 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl8, pos_y_tl8)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl8, pos_y_tl8+3)
    pos_y = [20,40,60,20,40,60,20,40,60,20,40,60]
    pos_x = [60,60,60,200,200,200,340,340,340,480,480,480]    
    box_c = ['ocean','semiArid','seaIce','desert','snow','urban','lakeIce','forest','vegetation',
             'mountainous','hilly','flat']
    name_c = ['Ocean','Semi-arid','Sea-ice','Desert','Snow','Urban','Lake-ice','Forest','Vegetation',
              'Mountainous','Hilly','Flat']
    check_boxes_loop(pos_x,pos_y,pos_y_tl8,box_c,name_c,self.surfaces_overflown_check_dict,template)
    pos_y = pos_y_tl8 + 85
    if self.so_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl8 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl8 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_13.count()):
            if isinstance(self.gridLayout_13.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_13.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_13.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.SOOtherTextBox.toPlainText():
        p = Paragraph(self.SOOtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h6 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h6 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl8 = pos_y
    if pos_y_tl8 + h6 >= 800:
        template.showPage()
        pos_y_tl8 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl8 + 18, pos_y_tl8, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl8 + 18, pos_y_tl8 + 3)
    pos_y = pos_y_tl8 - h6 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Altitude Ranges
    ############################
    title = 'Altitude Ranges of Measurement'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl8 == 80 and deb_page == 0:
        pos_x_tl9, pos_y_tl9 = 30, pos_y_tl8 + h + 70 + h6
    else:
        pos_x_tl9, pos_y_tl9 = 30, pos_y_tl8 + h + 70 + h6
    if pos_y_tl9 + 100 >= 800:
        template.showPage()
        pos_y_tl9 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl9, pos_y_tl9)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl9, pos_y_tl9+3)
    pos_y = [20,40,60,80,20,40,20,40]
    pos_x = [60,80,80,80,240,240,420,420]    
    box_c = ['boundaryLayer','blNearSurface','blSubCloud','blInCloud','lowerTroposphere','midTropos'
             'phere','upperTroposphere','lowerStratosphere']
    name_c = ['Boundary-layer','near-surface','sub-cloud','in-cloud','Lower troposphere','Mid tropo'
              'sphere','Upper troposphere','Lower stratosphere']
    check_boxes_loop(pos_x,pos_y,pos_y_tl9,box_c,name_c,self.altitude_ranges_check_dict,template)
    pos_y = pos_y_tl9 + 105
    if self.ar_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl9 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl9 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_14.count()):
            if isinstance(self.gridLayout_14.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_14.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_14.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.AROtherTextBox.toPlainText():
        p = Paragraph(self.AROtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h7 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h7 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl9 = pos_y
    if pos_y_tl9 + h7 >= 800:
        template.showPage()
        pos_y_tl9 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl9 + 18, pos_y_tl9, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl9 + 18, pos_y_tl9 + 3)
    pos_y = pos_y_tl9 - h7 + 30
    p.drawOn(template, 60, pos_y)
    
    
    ############################
    # Flight Types
    ############################
    title = 'Types of Flight Manoeuvre'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl9 == 80 and deb_page == 0:
        pos_x_tl10, pos_y_tl10 = 30, pos_y_tl9 + h + 70 +  h7
    else:
        pos_x_tl10, pos_y_tl10 = 30, pos_y_tl9 + h + 70 + h7
    if pos_y_tl10 + 80 >= 800:
        template.showPage()
        template.setFont("Arial",10)
        template.setFont("Arial",12)
        pos_y_tl10 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl10, pos_y_tl10)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl10, pos_y_tl10+3)
    pos_y = [20,40,60,20,40,60,20,40,60]
    pos_x = [60,80,80,240,240,240,420,420,420]      
    box_c = ['straightLevelRuns','stackedStraightLevelRuns','separatedStraightLevelRuns','racetracks',
             'orbits','lagrangianDescents','deepProfileAscentDescents','dropsondeDeployed','selfCal'
             'ibration']
    name_c = ['Straight / level runs','stacked','separated','Racetracks','Orbits','Lagrangian desce'
              'nts','Deep profile ascents / descents','Dropsonde deployed','Self-calibration']
    check_boxes_loop(pos_x,pos_y,pos_y_tl10,box_c,name_c,self.flight_types_check_dict,template)
    pos_y = pos_y_tl10 + 85
    if self.fm_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl10 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl10 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_15.count()):
            if isinstance(self.gridLayout_15.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_15.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_15.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.FTOtherTextBox.toPlainText():
        p = Paragraph(self.FTOtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h8 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h8 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl10 = pos_y
    if pos_y_tl10 + h8 >= 800:
        template.showPage()
        pos_y_tl10 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl10 + 18, pos_y_tl10, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl10 + 18, pos_y_tl10 + 3)
    pos_y = pos_y_tl10 - h8 + 30
    p.drawOn(template, 60, pos_y)
    

    ############################
    # Satellite coordination
    ############################
    title = 'Satellite Coordination'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl10 == 80 and deb_page == 0:
        pos_x_tl11, pos_y_tl11 = 30, pos_y_tl10 + h + 70 +  h8
    else:
        pos_x_tl11, pos_y_tl11 = 30, pos_y_tl10 + h + 70 + h8
    if pos_y_tl11+100 >= 800:
        template.showPage()
        pos_y_tl11 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl11, pos_y_tl11)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl11, pos_y_tl11+3)
    pos_y = [40,60,80,100,40,60,20,40,60,80,20,40,60]
    pos_x = [80,80,80,80,200,200,320,320,320,320,440,440,440]      
    box_c = ['polarMetop','polarNpoess','polarAtrain','polarOther','geosynchMsg','geosynchOther',
             'modis','cloudsat','caliop','iasi','airs','cris','amsuMhs']
    name_c = ['METOP','NPOESS','A-train','Other','MSG','Other','MODIS','Cloudsat','CALIOP','IASI',
              'AIRS','CriS','AMSU / MHS']
    check_boxes_loop(pos_x,pos_y,pos_y_tl11,box_c,name_c,self.satellite_coordination_check_dict,template)
    ptext = 'Polar:'
    template.drawString(48, pos_y_tl11+20, ptext)
    ptext = 'Geosynch:'
    template.drawString(168, pos_y_tl11+20, ptext)
    pos_y = pos_y_tl11 + 125
    if self.sc_ck_list:
        if pos_y + 40 >= 800:
            template.showPage()
            pos_y = 80
        template.setFont("Times",12)
        ptext = 'User-defined:'
        template.drawString(pos_x_tl11 + 18, pos_y, ptext)
        ln = line(0,0,72,0, 'black')
        ln.wrapOn(template, 200, 100)
        ln.drawOn(template, pos_x_tl11 + 18, pos_y + 3)
        template.setFont("Times",10)
        pos_x = 80
        pos_y += 20
        off_pos_y = 0
        for i in range(self.gridLayout_25.count()):
            if isinstance(self.gridLayout_25.itemAt(i).widget(), QCheckBox):
                if self.gridLayout_25.itemAt(i).widget().isChecked():
                    template.setFont("Times",10)
                    p = Paragraph(str(self.gridLayout_25.itemAt(i).widget().text()), styles["asmm_par"])
                    c, h = p.wrapOn(template, 110, 30)  # @UnusedVariable
                    if pos_y + h >= 800:
                        template.showPage()
                        pos_y = 80
                    p.drawOn(template, pos_x, pos_y - h + 10)
                    t = tick(0,0,8,1,1.5,'red')
                    t.wrapOn(template, 50, 50)
                    t.drawOn(template, pos_x-12, pos_y)
                    pos_x += 130
                    if off_pos_y < h:
                        off_pos_y = h
                    if i == 4 or i == 8:
                        pos_x = 80
                        pos_y += off_pos_y + 10
                        off_pos_y = 0
        pos_y += 20
    if self.SCOtherTextBox.toPlainText():
        p = Paragraph(self.SCOtherTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h9 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h9 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    pos_y_tl11 = pos_y
    if pos_y_tl11 + h9 >= 800:
        template.showPage()
        pos_y_tl11 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Comments:'
    template.drawString(pos_x_tl11 + 18, pos_y_tl11, ptext)
    template.setFont("Times",10)
    ln = line(0,0,62,0, 'black')
    ln.wrapOn(template, 200, 100)
    ln.drawOn(template, pos_x_tl11 + 18, pos_y_tl11 + 3)
    pos_y = pos_y_tl11 - h9 + 30
    p.drawOn(template, 60, pos_y)
 
    
    ############################
    # Surface Observations
    ############################
    title = 'Supporting Surface-Based Observations'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    if pos_y_tl11 == 80 and deb_page == 0:
        pos_x_tl12, pos_y_tl12 = 30, pos_y_tl11 + h + 70 + h9
    else:
        pos_x_tl12, pos_y_tl12 = 30, pos_y_tl11 + h + 70 + h9
    if (len(self.ground_site_list) * 20 + 40 + pos_y_tl12) >= 800:
        template.showPage()
        pos_y_tl12 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl12, pos_y_tl12)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl12, pos_y_tl12+3)
    template.setFont("Times",12)
    ptext = 'Ground Sites:'
    template.drawString(60, pos_y_tl12+20, ptext)
    template.setFont("Times",10)
    offset_tmp1 = pos_y_tl12 + 40
    i1 = 0
    for item in self.ground_site_list:
        template.drawString(80, offset_tmp1, item)
        offset_tmp1 = offset_tmp1 + 20
        i1 = i1 + 1
    if not self.ground_site_list:
        template.drawString(80, offset_tmp1, '')
        offset_tmp1 = offset_tmp1 + 20
        i1 = i1 + 1
    t = square(0, 0, 200, 20*i1+3, 1, 'black')
    t.wrapOn(template, 300, 300)
    t.drawOn(template, 60, pos_y_tl12 + 25)
    template.setFont("Times",12)
    ptext = 'ARM Sites:'
    template.drawString(320, pos_y_tl12 + 20, ptext)
    template.setFont("Times",10)
    offset_tmp2 = pos_y_tl12 + 40
    i2 = 0
    for item in self.arm_site_list:
        template.drawString(340, offset_tmp2, item)
        offset_tmp2 = offset_tmp2 + 20
        i2 = i2 + 1
    if not self.arm_site_list:
        template.drawString(340, offset_tmp2, '')
        offset_tmp2 = offset_tmp2 + 20
        i2 = i2 + 1
    t = square(0, 0, 200, 20*i2+3, 1, 'black')
    t.wrapOn(template, 300, 300)
    t.drawOn(template, 320, pos_y_tl12 + 25)
    if offset_tmp1 < offset_tmp2:
        offset_tmp1 = offset_tmp2
        i1 = i2
    offset_tmp1 += 20 
    if (len(self.research_vessel_list) * 20 + offset_tmp1 + 20) >= 800 or (len(self.arm_mobile_list)
            * 20 + offset_tmp1 + 20) >= 800:
        template.showPage()
        offset_tmp1 = 80
        deb_page = 0
    template.setFont("Times",12)
    ptext = 'Research Vessels:'
    template.drawString(60, offset_tmp1, ptext)
    offset_tmp3 = offset_tmp1 + 20
    template.setFont("Times",10)
    i3 = 0
    for item in self.research_vessel_list:
        template.drawString(80, offset_tmp3, item)
        offset_tmp3 = offset_tmp3 + 20
        i3 = i3 + 1
    if not self.research_vessel_list:
        template.drawString(80, offset_tmp3, '')
        i3 = i3 + 1
    t = square(0, 0, 200, 20 * i3 + 3, 1, 'black')
    t.wrapOn(template, 300, 300)
    t.drawOn(template, 60, offset_tmp1 + 5)
    template.setFont("Times",12)
    ptext = 'ARM Mobile sites:'
    template.drawString(320, offset_tmp1, ptext)
    offset_tmp4 = offset_tmp1 + 20
    template.setFont("Times",10)
    i4 = 0
    for item in self.arm_mobile_list:
        template.drawString(340, offset_tmp4, item)
        offset_tmp4 = offset_tmp4 + 20
        i4 = i4 + 1
    if not self.arm_mobile_list:
        template.drawString(340, offset_tmp4, '')
        i4 = i4 + 1
    t = square(0, 0, 200, 20 * i4 + 3, 1, 'black')
    t.wrapOn(template, 300, 300)
    t.drawOn(template, 320, offset_tmp1 + 5)

    
    #############################
    # Other Comments
    ############################
    if offset_tmp3 < offset_tmp4:
        offset_tmp3 = offset_tmp4
        i3 = i4
    title = 'Additional Notes on the Flight'
    tl = Paragraph(title, styles["asmm_par_tl"])
    w, h = tl.wrapOn(template, 500, 100)
    pos_y_tl13 = offset_tmp3 + 70
    pos_x_tl13 = 25
    if self.OtherCommentsTextBox.toPlainText():
        p = Paragraph(self.OtherCommentsTextBox.toPlainText(), styles["asmm_par_sl"])
        c, h10 = p.wrapOn(template, 500, 500)  # @UnusedVariable
    else:
        ptext = 'No comment'
        p = Paragraph(ptext, styles["asmm_par_sl"])
        c, h10 = p.wrapOn(template, 100, 100)  # @UnusedVariable
    if pos_y_tl13 + h10 + 20 >= 800:
        template.showPage()
        pos_y_tl13 = 80
        deb_page = 1
    tl.drawOn(template, pos_x_tl13, pos_y_tl13)
    sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
    sq.wrapOn(template, 600, 100)
    sq.drawOn(template, pos_x_tl13, pos_y_tl13 + 3)
    pos_y = pos_y_tl13 - h10 + 40
    p.drawOn(template, 48, pos_y)


    #############################
    # Uploaded images
    #############################
    if self.images_pdf_path:
        pos_x_tl14 = 25
        pos_y_tl14 = pos_y_tl13 + h10 + 100
        title = 'Images Included in the PDF Report'
        tl = Paragraph(title, styles["asmm_par_tl"])
        w, h = tl.wrapOn(template, 500, 100)
        if pos_y_tl14 + h > 800:
            pos_y_tl14 = 80
            template.showPage()
            deb_page = 1
        tl.drawOn(template, pos_x_tl14, pos_y_tl14)
        sq = semi_square(-10, 0, -10, -28, page_w-50, 0, 2, 'black')
        sq.wrapOn(template, 600, 100)   
        sq.drawOn(template, pos_x_tl14, pos_y_tl14 + 3)
        i = 0
        for path in self.images_pdf_path:
            img = utils.ImageReader(path)
            width, height = img.getSize()
            ratio = float(width) / float(height)
            if ratio > 1:
                width = 450
                height = 450 / float(ratio)
                pos_x = pos_x_tl14 + 45
            elif ratio < 0.5:
                height = 400
                width = 400 * float(ratio)
                pos_x = pos_x_tl14 + 70
            else:
                height = 450
                width = 450 * float(ratio)
                pos_x = pos_x_tl14 + 45
            if pos_y_tl14 + h + height > 800:
                pos_y_tl14 = 60
                template.showPage()
                deb_page = 1
            template.drawImage(img, pos_x, pos_y_tl14 + 20, width, height)
            #title = 'Figure %s: %s' % str(i + 1), self.im_textbox[i].text()
            title = "Figure " + str(i + 1) + ": " + self.im_textbox[i].text()
            tl = Paragraph(str(title), styles["asmm_figure"])
            w, h = tl.wrapOn(template, width + 50, 100)
            pos_y_tl14 = pos_y_tl14 + height + 40
            tl.drawOn(template, pos_x - 25, pos_y_tl14)
            pos_y_tl14 = pos_y_tl14 + 20
            i +=1


    #############################
    # Document generation
    #############################
    template.save()
    
    
def check_boxes_loop(xc,yc,ofc,bc,nc,itemc,tc):
    tc.setFont("Times",10)
    for key, value in iter(itemc.items()):
        idx = bc.index(value)
        tc.drawString(int(xc[idx]), (int(yc[idx])+ofc), nc[idx])
        if key.isChecked():
            t = tick(0,0,8,1,1.5,'red')
        else:
            t = tick(0,0,8,0,1.5,'red')
        t.wrapOn(tc, 50, 50)
        t.drawOn(tc, int(xc[idx])-12, (int(yc[idx])+ofc))
    tc.setFont("Times",12)
    