# -*- coding: utf-8 -*-

import sqlite3 as lite
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDate
#import logging

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def objectsInit(self):
    self.ground_site_list = []
    self.research_vessel_list = []
    self.arm_site_list = []
    self.arm_mobile_list = []
    self.dateLine.setDate(QDate.currentDate())
    self.out_file_name = None
    self.saved = False
    self.modified = False
    self.create_date = None
    self.sa_ck_list = []
    self.sa_ckL = 0
    self.sa_x = 0
    self.sa_y = 0
    self.gr_ck_list = []
    self.gr_ckL = 0
    self.gr_x = 0
    self.gr_y = 0
    self.af_ck_list = []
    self.af_ckL = 0
    self.af_x = 0
    self.af_y = 0
    self.ct_ck_list = []
    self.ct_ckL = 0
    self.ct_x = 0
    self.ct_y = 0
    self.ps_ck_list = []
    self.ps_ckL = 0
    self.ps_x = 0
    self.ps_y = 0
    self.so_ck_list = []
    self.so_ckL = 0
    self.so_x = 0
    self.so_y = 0
    self.ar_ck_list = []
    self.ar_ckL = 0
    self.ar_x = 0
    self.ar_y = 0
    self.fm_ck_list = []
    self.fm_ckL = 0
    self.fm_x = 0
    self.fm_y = 0
    self.sc_ck_list = []
    self.sc_ckL = 0
    self.sc_x = 0
    self.sc_y = 0
    
    
    self.scientific_aims_check_dict = {self.satelliteCalValCheck:'satelliteCalVal',
                                       self.aerosolCheck:'aerosol',
                                       self.aerosolRadiativeCheck:'aerosolRadiative',
                                       self.aerosolMicrophysicalCheck:'aerosolMicrophysical',
                                       self.anthroPollutionCheck:'anthroPollution',
                                       self.mesoscaleImpactsCheck:'mesoscaleImpacts',
                                       self.cloudMicrophysicsCheck:'cloudMicrophysics',
                                       self.cloudDynamicsCheck:'cloudDynamics',
                                       self.cloudRadiativeCheck:'cloudRadiative',
                                       self.cloudConvectionCheck:'cloudConvection',
                                       self.blCloudCheck:'blCloud',
                                       self.blDynamicsCheck:'blDynamics',
                                       self.radiationCheck:'radiation',
                                       self.radiationAtmosSpectroscopyCheck:'radiationAtmosSpectroscopy',
                                       self.radiationSurfPropertiesCheck:'radiationSurfProperties',
                                       self.radiationOtherCheck:'radiationOther',
                                       self.gasChemCheck:'gasChem',
                                       self.gasChemOrganicsCheck:'gasChemOrganics',
                                       self.gasChemOxidantsCheck:'gasChemOxidants',
                                       self.gasChemOtherCheck:'gasChemOther'
                                       }

    self.geographical_region_check_dict = {self.polarCheck:'polar',
                                           self.midLatitudesCheck:'midLatitudes',
                                           self.subTropicalCheck:'subTropical',
                                           self.tropicalCheck:'tropical',
                                           self.maritimeCheck:'maritime',
                                           self.continentalCheck:'continental',
                                           self.oceanicIslandsCheck:'oceanicIslands',
                                           self.geogOtherCheck:'other'
                                           }

    self.atmospheric_features_check_dict = {self.stationaryCheck:'stationary',
                                            self.stationaryAnticyclonicCheck:'stationaryAnticyclonic',
                                            self.stationaryCyclonicCheck:'stationaryCyclonic',
                                            self.warmFrontCheck:'warmFront',
                                            self.warmConveyorBeltCheck:'warmConveyorBelt',
                                            self.coldFrontCheck:'coldFront',
                                            self.occludedFrontCheck:'occludedFront',
                                            self.warmSectorCheck:'warmSector',
                                            self.postColdFrontalAirMassCheck:'postColdFrontalAirMass',
                                            self.arcticColdAirOutbreakCheck:'arcticColdAirOutbreak',
                                            self.orographicInfluenceCheck:'orographicInfluence',
                                            self.seaBreezeFrontCheck:'seaBreezeFront',
                                            self.stratosphericFoldCheck:'stratosphericFold',
                                            self.extendedConvergenceLineCheck:'extendedConvergenceLine',
                                            self.easterlyWaveCheck:'easterlyWave',
                                            self.equatorialWaveCheck:'equatorialWave',
                                            self.tropicalCycloneCheck:'tropycalCyclone',
                                            self.mesoscaleOrganizedConvectionCheck:'mesoscaleOrganizedConvection'
                                            }

    self.cloud_types_check_dict = {self.waterCloudsCheck:'waterClouds',
                                   self.mixedPhaseCloudsCheck:'mixedPhaseClouds',
                                   self.iceCloudsCheck:'iceClouds',
                                   self.cirrusCheck:'cirrus',
                                   self.contrailsCheck:'contrails',
                                   self.stratocumulusCheck:'stratocumulus',
                                   self.shallowCumulusCheck:'shallowCumulus',
                                   self.cumulusCongestusCheck:'cumulusCongestus',
                                   self.cumulonimbusToweringCumulusCheck:'cumulonimbusToweringCumulus',
                                   self.altostratusAltocumulusCheck:'altostratusAltocumulus',
                                   self.waveCloudsCheck:'waveClouds',
                                   self.deepFrontalStratiformCloudsCheck:'deepFrontalStratiformClouds',
                                   self.cloudFreeAboveAircraftCheck:'cloudFreeAboveAircraft',
                                   self.cloudFreeBelowAircraftCheck:'cloudFreeBelowAircraft'
                                   }

    self.particles_sampled_check_dict = {self.rainCheck:'rain',
                                         self.drizzleCheck:'drizzle',
                                         self.dropletsCheck:'droplets',
                                         self.pristineIceCrystalsCheck:'pristineIceCrystals',
                                         self.snowOrAggregatesCheck:'snowOrAggregates',
                                         self.graupelOrHailCheck:'graupelOrHail',
                                         self.seaSaltAerosolCheck:'seaSaltAerosol',
                                         self.continentalAerosolCheck:'continentalAerosol',
                                         self.urbanPlumeCheck:'urbanPlume',
                                         self.biomassBurningCheck:'biomassBurning',
                                         self.desertOrMineralDustCheck:'desertOrMineralDust',
                                         self.volcanicAshCheck:'volcanicAsh'
                                         }

    self.surfaces_overflown_check_dict = {self.oceanCheck:'ocean',
                                          self.semiAridCheck:'semiArid',
                                          self.seaIceCheck:'seaIce',
                                          self.desertCheck:'desert',
                                          self.snowCheck:'snow',
                                          self.urbanCheck:'urban',
                                          self.lakeIceCheck:'lakeIce',
                                          self.mountainousCheck:'mountainous',
                                          self.vegetationCheck:'vegetation',
                                          self.hillyCheck:'hilly',
                                          self.forestCheck:'forest',
                                          self.flatCheck:'flat'
                                          }

    self.altitude_ranges_check_dict = {self.boundaryLayerCheck:'boundaryLayer',
                                       self.blNearSurfaceCheck:'blNearSurface',
                                       self.blSubCloudCheck:'blSubCloud',
                                       self.blInCloudCheck:'blInCloud',
                                       self.lowerTroposphereCheck:'lowerTroposphere',
                                       self.midTroposphereCheck:'midTroposphere',
                                       self.upperTroposphereCheck:'upperTroposphere',
                                       self.lowerStratosphereCheck:'lowerStratosphere'
                                       }

    self.flight_types_check_dict = {self.straightLevelRunsCheck:'straightLevelRuns',
                                    self.stackedStraightLevelRunsCheck:'stackedStraightLevelRuns',
                                    self.separatedStraightLevelRuns:'separatedStraightLevelRuns',
                                    self.racetracksCheck:'racetracks',
                                    self.orbitsCheck:'orbits',
                                    self.lagrangianDescentsCheck:'lagrangianDescents',
                                    self.deepProfileAscentDescentsCheck:'deepProfileAscentDescents',
                                    self.dropsondeDeployedCheck:'dropsondeDeployed',
                                    self.selfCalibrationCheck:'selfCalibration'
                                    }

    self.satellite_coordination_check_dict = {self.polarMetopCheck:'polarMetop',
                                              self.polarNpoessCheck:'polarNpoess',
                                              self.polarAtrainCheck:'polarAtrain',
                                              self.polarOtherCheck:'polarOther',
                                              self.geosynchMsgCheck:'geosynchMsg',
                                              self.geosynchOtherCheck:'geosynchOther',
                                              self.modisCheck:'modis',
                                              self.cloudsatCheck:'cloudsat',
                                              self.caliopCheck:'caliop',
                                              self.iasiCheck:'iasi',
                                              self.airsCheck:'airs',
                                              self.crisCheck:'cris',
                                              self.amsuMhsCheck:'amsuMhs'
                                              }
    
    self.operators_aircraft = [
        ["Alfred Wegener Institute","BT-67 POLAR 5","AWI","BT-67"],
        ["CNR - Istituto per i Sistemi Agricoli e Forestali del Mediterraneo","Sky Arrow 650","CNR-ISAFoM","Sky Arrow 650"],
        ["CNR - Istituto di Metodologie per l'Analisi Ambientale","Partenavia P-68","CNR-IMAA","P-68"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Cessna 208","DLR","Cessna 208"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Dornier DO-228 D-CFFU","DLR","DO-228"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Dornier DO-228 D-CODE","DLR","DO-228"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Mystere/Falcon 20","DLR","Mystere/Falcon 20"],
        ["ENVISCOPE","Learjet 35","Enviscope","Learjet 35"],
        ["ENVISCOPE","Partenavia P-68","Enviscope","P-68"],
        ["NERC - Facility for Airborne Atmospheric Measurements","BAe-146","FAAM","BAe-146"],
        ["FUB - Institut fur Weltraumwissenschaften","Cessna 207","FUB-ISS","Cessna 207"],
        ["Instituto Nacional de Tecnica Aeroespacial","CASA-212 AR","INTA","CASA-212"],
        ["Instituto Nacional de Tecnica Aeroespacial","CASA-212 RS","INTA","CASA-212"],
        ["KIT - Institute of Meteorology and Climate Research","Enduro","KIT-IMK-IFU","Enduro"],
        ["NERC - Airborne Research and Survey Facility","Dornier DO-228","NERC-ARSF","DO-228"],
        ["NERC - British Antarctic Survey","DHC-6 Twin Otter","NERC-BAS","DHC-6"],
        ["SAFIRE","ATR-42","SAFIRE","ATR-42"],
        ["SAFIRE","Mystere/Falcon 20","SAFIRE","Mystere/Falcon 20"],
        ["SAFIRE","Piper PA23","SAFIRE","PA23"],
        ["UEDIN - Airborne GeoSciences","HK36TTC ECO Dimona","UEDIN-IAES","HK36TTC ECO Dimona"],
        ]

    self.countries = ["Do your choice...","Afghanistan","Albania","Algeria","Amazonia","American Samoa","Amsterdam And St. Paul Islands","Andaman Islands","Andorra","Angola","Anguilla","Antigua And Barbuda","Argentina","Armenia","Aruba","Ascension Island","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Baker Island","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bonaire","Bosnia And Herzegovina","Botswana","Bouvet Island","Brazil","British Isles","Brunei","Bulgaria","Burkina Faso","Burma","Burundi","Cambodia","Cameroon","Canada","Caribbean","Cayman Islands","Central African Republic","Ceuta","Chad","Channel Islands","Chile","China","Christmas Island","Cocos Islands","Colombia","Comoros","Congo, Democratic Republic","Congo, Republic","Cook Islands","Corsica","Costa Rica","Cote D'ivoire","Croatia","Crozet Islands","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Dhekelia","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Faeroe Islands","Falkland Islands","Fiji","Finland","France","French Guiana","French Polynesia","Gabon","Galapagos Islands","Gambia","Gaza Strip","Georgia, Republic","Germany","Ghana","Gibraltar","Gough Island","Greece","Greenland","Grenada","Guadeloupe","Guam","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Hawaii Island","Hawaiian Islands","Honduras","Hong Kong","Howland Island","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jarvis Island","Johnston Atoll","Jordan","Kahoolawe","Kauai","Kazakhstan","Kenya","Kerguelen Islands","Kingman Reef","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laeso","Lake Chad","Lake Malawi","Lake Tanganyika","Lake Victoria","Lanai","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Madeira","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Martinique","Maui","Mauritania","Mauritius","Melanesia","Mexico","Micronesia","Midway Atoll","Moldova","Molokai","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nauru","Navassa Island","Nepal","Netherlands Antilles","Netherlands","New Caledonia","New Zealand","Nicaragua","Nicobar Islands","Niger","Nigeria","Niihau","Niue","Norfolk Island","North Korea","Northern Mariana Islands","Norway","Oahu","Okinawa","Oman","Pakistan","Palau","Palestine","Palmyra Atoll","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn Island","Pitcairn Islands","Poland","Polynesia","Portugal","Puerto Rico","Qatar","Red Sea","Reunion","Romania","Russia","Rwanda","Saba","Sable Island","Samoa","San Marino","Sao Tome And Principe","Sardinia","Saudi Arabia","Scandinavia","Senegal","Serbia","Seychelles","Sicily","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Georgia Island","South Korea","South Orkney Islands","South Sandwich Islands","Spain","Spratly Islands","Sri Lanka","St Barthelemy","St Eustatius","St Helena","St Kitts And Nevis","St Lucia","St Maarten","St Martin","St Pierre And Miquelon","St Vincent And The Grenadines","Sudan","Suriname","Svalbard And Jan Mayen","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tokelau","Tonga","Trinidad And Tobago","Tristan Da Cunha","Tunisia","Turkey","Turkmenistan","Turks And Caicos Islands","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Virgin Islands","Wake Island","Wallis And Futuna Islands","Yemen","Zambia","Zanzibar","Zimbabwe"]