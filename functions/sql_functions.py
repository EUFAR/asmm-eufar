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
    
    