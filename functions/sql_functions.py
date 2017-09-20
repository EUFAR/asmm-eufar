import logging
from PyQt5.QtCore import QDate

def objectsInit(self):
    logging.debug('sql_functions.py - MyAbout - objectsInit starting ...')
    self.ground_site_list = []
    self.research_vessel_list = []
    self.arm_site_list = []
    self.arm_mobile_list = []
    self.date_dt.setDate(QDate.currentDate())
    self.images_pdf_path = []
    self.images_display_path = []
    self.out_file_name = None
    self.saved = False
    self.modified = False
    self.create_date = None
    self.sa_ck_list = []
    self.sa_ckL = 0
    self.sa_x = 0
    self.sa_y = 0
    self.sa_xy_list = [0, 0]
    self.gr_ck_list = []
    self.gr_ckL = 0
    self.gr_x = 0
    self.gr_y = 0
    self.gr_xy_list = [0, 0]
    self.af_ck_list = []
    self.af_ckL = 0
    self.af_x = 0
    self.af_y = 0
    self.af_xy_list = [0, 0]
    self.ct_ck_list = []
    self.ct_ckL = 0
    self.ct_x = 0
    self.ct_y = 0
    self.ct_xy_list = [0, 0]
    self.ps_ck_list = []
    self.ps_ckL = 0
    self.ps_x = 0
    self.ps_y = 0
    self.ps_xy_list = [0, 0]
    self.so_ck_list = []
    self.so_ckL = 0
    self.so_x = 0
    self.so_y = 0
    self.so_xy_list = [0, 0]
    self.ar_ck_list = []
    self.ar_ckL = 0
    self.ar_x = 0
    self.ar_y = 0
    self.ar_xy_list = [0, 0]
    self.fm_ck_list = []
    self.fm_ckL = 0
    self.fm_x = 0
    self.fm_y = 0
    self.fm_xy_list = [0, 0]
    self.sc_ck_list = []
    self.sc_ckL = 0
    self.sc_x = 0
    self.sc_y = 0
    self.sc_xy_list = [0, 0]
    
    
    self.ck_list_dict = {'sa':self.sa_ck_list,
                         'gr':self.gr_ck_list,
                         'af':self.af_ck_list,
                         'ct':self.ct_ck_list,
                         'ps':self.ps_ck_list,
                         'so':self.so_ck_list,
                         'ar':self.ar_ck_list,
                         'fm':self.fm_ck_list,
                         'sc':self.sc_ck_list
                         }
    
    self.ck_num_dict = {'sa':self.sa_ckL,
                        'gr':self.gr_ckL,
                        'af':self.af_ckL,
                        'ct':self.ct_ckL,
                        'ps':self.ps_ckL,
                        'so':self.so_ckL,
                        'ar':self.ar_ckL,
                        'fm':self.fm_ckL,
                        'sc':self.sc_ckL
                        }
    
    self.ck_x_dict = {'sa':self.sa_x,
                      'gr':self.gr_x,
                      'af':self.af_x,
                      'ct':self.ct_x,
                      'ps':self.ps_x,
                      'so':self.so_x,
                      'ar':self.ar_x,
                      'fm':self.fm_x,
                      'sc':self.sc_x
                      }
    
    self.ck_y_dict = {'sa':self.sa_y,
                      'gr':self.gr_y,
                      'af':self.af_y,
                      'ct':self.ct_y,
                      'ps':self.ps_y,
                      'so':self.so_y,
                      'ar':self.ar_y,
                      'fm':self.fm_y,
                      'sc':self.sc_y
                      }
    
    self.ck_xy_dict = {'sa':self.sa_xy_list,
                      'gr':self.gr_xy_list,
                      'af':self.af_xy_list,
                      'ct':self.ct_xy_list,
                      'ps':self.ps_xy_list,
                      'so':self.so_xy_list,
                      'ar':self.ar_xy_list,
                      'fm':self.fm_xy_list,
                      'sc':self.sc_xy_list
                      }
    
    self.ck_lay_dict = {'sa':self.gridLayout_5,
                        'gr':self.gridLayout_8,
                        'af':self.gridLayout_9,
                        'ct':self.gridLayout_10,
                        'ps':self.gridLayout_11,
                        'so':self.gridLayout_16,
                        'ar':self.gridLayout_14,
                        'fm':self.gridLayout_15,
                        'sc':self.gridLayout_25
                        }
    
    self.im_image_in = []
    self.im_image_out = []
    self.im_horlay = []
    self.im_verlay = []
    self.im_label = []
    self.im_caption = []
    self.im_textbox = []
    self.im_number = 0
    self.im_del = []
    
    
    self.scientific_aims_check_dict = {self.satelliteCalValCheck:'Satellite Cal/Val',
                                       self.aerosolCheck:'Aerosol',
                                       self.aerosolRadiativeCheck:'Radiative properties/impacts (Aerosol)',
                                       self.aerosolMicrophysicalCheck:'Cloud microphysical impacts (Aerosol)',
                                       self.anthroPollutionCheck:'Anthropogenic pollution',
                                       self.mesoscaleImpactsCheck:'Mesoscale atmospheric impacts',
                                       self.cloudMicrophysicsCheck:'Microphysics (Cloud)',
                                       self.cloudDynamicsCheck:'Dynamics (Cloud)',
                                       self.cloudRadiativeCheck:'Radiative properties (Cloud)',
                                       self.cloudConvectionCheck:'Convection dynamics (Cloud)',
                                       self.blCloudCheck:'Cloud (Boundary-layer)',
                                       self.blDynamicsCheck:'Dynamics (Boundary-layer)',
                                       self.radiationCheck:'Radiation',
                                       self.radiationAtmosSpectroscopyCheck:'Atmospheric spectroscopy (Radiation)',
                                       self.radiationSurfPropertiesCheck:'Surface properties/retrievals (Radiation)',
                                       self.radiationOtherCheck:'Other (Radiation)',
                                       self.gasChemCheck:'Gas chemistry',
                                       self.gasChemOrganicsCheck:'Organics (Gas chemistry)',
                                       self.gasChemOxidantsCheck:'Oxydants (Gas chemistry)',
                                       self.gasChemOtherCheck:'Other (Gas chemistry)'
                                       }

    self.geographical_region_check_dict = {self.polarCheck:'Polar',
                                           self.midLatitudesCheck:'Mid-latitudes',
                                           self.subTropicalCheck:'Sub-tropical',
                                           self.tropicalCheck:'Tropical',
                                           self.maritimeCheck:'Maritime',
                                           self.continentalCheck:'Continental',
                                           self.oceanicIslandsCheck:'Oceanic islands',
                                           self.geogOtherCheck:'Other (Geographical region)'
                                           }

    self.atmospheric_features_check_dict = {self.stationaryCheck:'Stationary',
                                            self.stationaryAnticyclonicCheck:'Stationary anticyclonic',
                                            self.stationaryCyclonicCheck:'Stationary cyclonic',
                                            self.warmFrontCheck:'Warm front',
                                            self.warmConveyorBeltCheck:'Warm conveyor belt',
                                            self.coldFrontCheck:'Cold front',
                                            self.occludedFrontCheck:'Occluded front',
                                            self.warmSectorCheck:'Warm sector',
                                            self.postColdFrontalAirMassCheck:'Post-cold-frontal air-mass',
                                            self.arcticColdAirOutbreakCheck:'Arctic cold-air outbreak',
                                            self.orographicInfluenceCheck:'Orographic influence',
                                            self.seaBreezeFrontCheck:'Sea-breeze front',
                                            self.stratosphericFoldCheck:'Stratospheric fold/intrusion',
                                            self.extendedConvergenceLineCheck:'Extended convergence line',
                                            self.easterlyWaveCheck:'Easterly wave',
                                            self.equatorialWaveCheck:'Equatorial wave',
                                            self.tropicalCycloneCheck:'Tropical cyclone',
                                            self.mesoscaleOrganizedConvectionCheck:'Mesoscale organized convection'
                                            }

    self.cloud_types_check_dict = {self.waterCloudsCheck:'Water clouds',
                                   self.mixedPhaseCloudsCheck:'Mixed-phase clouds',
                                   self.iceCloudsCheck:'Ice clouds',
                                   self.cirrusCheck:'Cirrus',
                                   self.contrailsCheck:'Contrails',
                                   self.stratocumulusCheck:'Stratocumulus',
                                   self.shallowCumulusCheck:'Shallow cumulus',
                                   self.cumulusCongestusCheck:'Cumulus congestus',
                                   self.cumulonimbusToweringCumulusCheck:'Cumulonimbus/towering cumulus',
                                   self.altostratusAltocumulusCheck:'Altostratus/altocumulus',
                                   self.waveCloudsCheck:'Wave clouds',
                                   self.deepFrontalStratiformCloudsCheck:'Deep frontal stratiform clouds',
                                   self.cloudFreeAboveAircraftCheck:'Cloud-free above aircraft',
                                   self.cloudFreeBelowAircraftCheck:'Cloud-free below aircraft'
                                   }

    self.particles_sampled_check_dict = {self.rainCheck:'Rain',
                                         self.drizzleCheck:'Drizzle',
                                         self.dropletsCheck:'Droplets (Liquid)',
                                         self.pristineIceCrystalsCheck:'Pristine ice crystals',
                                         self.snowOrAggregatesCheck:'Snow/aggregates',
                                         self.graupelOrHailCheck:'Graupel/hail',
                                         self.seaSaltAerosolCheck:'Sea-salt aerosol',
                                         self.continentalAerosolCheck:'Continental aerosol',
                                         self.urbanPlumeCheck:'Urban plume',
                                         self.biomassBurningCheck:'Biomass burning',
                                         self.desertOrMineralDustCheck:'Desert/mineral dust',
                                         self.volcanicAshCheck:'Volcanic ash'
                                         }

    self.surfaces_overflown_check_dict = {self.oceanCheck:'Ocean',
                                          self.semiAridCheck:'Semi-arid',
                                          self.seaIceCheck:'Sea-ice',
                                          self.desertCheck:'Desert',
                                          self.snowCheck:'Snow',
                                          self.urbanCheck:'Urban',
                                          self.lakeIceCheck:'Lake-ice',
                                          self.mountainousCheck:'Mountainous',
                                          self.vegetationCheck:'Vegetation',
                                          self.hillyCheck:'Hilly',
                                          self.forestCheck:'Forest',
                                          self.flatCheck:'Flat'
                                          }

    self.altitude_ranges_check_dict = {self.boundaryLayerCheck:'Boundary-layer',
                                       self.blNearSurfaceCheck:'Near-surface (Boundary-layer)',
                                       self.blSubCloudCheck:'Sub-cloud (Boundary-layer)',
                                       self.blInCloudCheck:'In-cloud (Boundary-layer)',
                                       self.lowerTroposphereCheck:'Lower troposphere',
                                       self.midTroposphereCheck:'Mid troposphere',
                                       self.upperTroposphereCheck:'Upper troposphere',
                                       self.lowerStratosphereCheck:'Lower stratosphere'
                                       }

    self.flight_types_check_dict = {self.straightLevelRunsCheck:'Straight/level runs',
                                    self.stackedStraightLevelRunsCheck:'Stacked (Straight/level runs)',
                                    self.separatedStraightLevelRuns:'Separated (Straight/level runs)',
                                    self.racetracksCheck:'Racetracks',
                                    self.orbitsCheck:'Orbits',
                                    self.lagrangianDescentsCheck:'Lagrangian descents',
                                    self.deepProfileAscentDescentsCheck:'Deep profile ascents/descents',
                                    self.dropsondeDeployedCheck:'Dropsonde deployed',
                                    self.selfCalibrationCheck:'Self-calibration'
                                    }

    self.satellite_coordination_check_dict = {self.polarMetopCheck:'METOP (Polar)',
                                              self.polarNpoessCheck:'NPOESS (Polar)',
                                              self.polarAtrainCheck:'A-train (Polar)',
                                              self.polarOtherCheck:'Other (Polar)',
                                              self.geosynchMsgCheck:'MSG (Geosynch)',
                                              self.geosynchOtherCheck:'Other (Geosynch)',
                                              self.modisCheck:'MODIS',
                                              self.cloudsatCheck:'Cloudsat',
                                              self.caliopCheck:'CALIOP',
                                              self.iasiCheck:'IASI',
                                              self.airsCheck:'AIRS',
                                              self.crisCheck:'CriS',
                                              self.amsuMhsCheck:'AMSU/MHS'
                                              }

    self.old_scientific_aims_check_dict = {self.satelliteCalValCheck:'satelliteCalVal',
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

    self.old_geographical_region_check_dict = {self.polarCheck:'polar',
                                           self.midLatitudesCheck:'midLatitudes',
                                           self.subTropicalCheck:'subTropical',
                                           self.tropicalCheck:'tropical',
                                           self.maritimeCheck:'maritime',
                                           self.continentalCheck:'continental',
                                           self.oceanicIslandsCheck:'oceanicIslands',
                                           self.geogOtherCheck:'other'
                                           }

    self.old_atmospheric_features_check_dict = {self.stationaryCheck:'stationary',
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

    self.old_cloud_types_check_dict = {self.waterCloudsCheck:'waterClouds',
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

    self.old_particles_sampled_check_dict = {self.rainCheck:'rain',
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

    self.old_surfaces_overflown_check_dict = {self.oceanCheck:'ocean',
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

    self.old_altitude_ranges_check_dict = {self.boundaryLayerCheck:'boundaryLayer',
                                       self.blNearSurfaceCheck:'blNearSurface',
                                       self.blSubCloudCheck:'blSubCloud',
                                       self.blInCloudCheck:'blInCloud',
                                       self.lowerTroposphereCheck:'lowerTroposphere',
                                       self.midTroposphereCheck:'midTroposphere',
                                       self.upperTroposphereCheck:'upperTroposphere',
                                       self.lowerStratosphereCheck:'lowerStratosphere'
                                       }

    self.old_flight_types_check_dict = {self.straightLevelRunsCheck:'straightLevelRuns',
                                    self.stackedStraightLevelRunsCheck:'stackedStraightLevelRuns',
                                    self.separatedStraightLevelRuns:'separatedStraightLevelRuns',
                                    self.racetracksCheck:'racetracks',
                                    self.orbitsCheck:'orbits',
                                    self.lagrangianDescentsCheck:'lagrangianDescents',
                                    self.deepProfileAscentDescentsCheck:'deepProfileAscentDescents',
                                    self.dropsondeDeployedCheck:'dropsondeDeployed',
                                    self.selfCalibrationCheck:'selfCalibration'
                                    }

    self.old_satellite_coordination_check_dict = {self.polarMetopCheck:'polarMetop',
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
        ["CzechGlobe","Cessna 208","CzechGlobe","Cessna 208"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Cessna 208","DLR","Cessna 208"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Dornier DO-228 D-CFFU","DLR","DO-228"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Dornier DO-228 D-CODE","DLR","DO-228"],
        ["Deutsches Zentrum fur Luft- und Raumfahrt","Mystere/Falcon 20","DLR","Mystere/Falcon 20"],
        ["ENVISCOPE","Learjet 35","Enviscope","Learjet 35"],
        ["ENVISCOPE","Partenavia P-68","Enviscope","P-68"],
        ["NERC - Facility for Airborne Atmospheric Measurements","BAe-146","FAAM","BAe-146"],
        ["FUB - Institut fur Weltraumwissenschaften","Cessna 207","FUB-ISS","Cessna 207"],
        ["Instituto Nacional de Tecnica Aeroespacial","CASA-212 AR EC-DTV","INTA","CASA-212 EC-DTV"],
        ["Instituto Nacional de Tecnica Aeroespacial","CASA-212 RS EC-DUQ","INTA","CASA-212 EC-DUQ"],
        ["KIT - Institute of Meteorology and Climate Research","Enduro","KIT-IMK-IFU","Enduro"],
        ["NERC - Airborne Research Facility","Dornier DO-228","NERC-ARF","DO-228"],
        ["NERC - British Antarctic Survey","DHC-6 Twin Otter VP-FAZ","NERC-BAS","DHC-6 VP-FAZ"],
        ["NERC - British Antarctic Survey","DHC-6 Twin Otter VP-FBL","NERC-BAS","DHC-6 VP-FBL"],
        ["SAFIRE","ATR-42","SAFIRE","ATR-42"],
        ["SAFIRE","Mystere/Falcon 20","SAFIRE","Mystere/Falcon 20"],
        ["SAFIRE","Piper PA23","SAFIRE","PA23"],
        ["UEDIN - Airborne GeoSciences","HK36TTC ECO Dimona","UEDIN-IAES","HK36TTC ECO Dimona"],
        ]
    
    self.new_operators_aircraft = [
        ['AWI','Basler Turbo Conversions, BT-67','C-GAWI','DE'],
        ['CNR-ISAFoM','3I / Magnaghi Aeronautica, Sky Arrow 650 TCNS','I-AMMO','IT'],
        ['CNR-IMAA','Partenavia / Vulcanair, P-68 Observer 2','I-OBPC','IT'],
        ['CzechGlobe','Cessna Aircraft Company, C-208 B Grand Caravan','OK-CZG','CZ'],
        ['DLR','Cessna Aircraft Company, C-208 B Grand Caravan','D-FDLR','DE'],
        ['DLR','Dornier Flugzeugwerke, Do 228 - 212','D-CFFU','DE'],
        ['DLR','Dornier Flugzeugwerke, Do 228 - 101','D-CODE','DE'],
        ['DLR','Dassault Aviation, Mystere / Falcon 20 E-5','D-CMET','DE'],
        ['Enviscope','Partenavia / Vulcanair, P-68B','D-GERY','DE'],
        ['Enviscope','Learjet / Bombardier Aerospace, 35A','D-CGFD','DE'],
        ['FAAM','BAE Systems, BAe146-301','G-LUXE','GB'],
        ['FUB','Cessna Aircraft Company, T207A Turbo Skywagon','D-EAFU','DE'],
        ['INTA','Construcciones Aeronauticas S.A, C-212-200','EC-DTV','ES'],
        ['INTA','Construcciones Aeronauticas S.A, C-212-200','EC-DUQ','ES'],
        ['KIT, IMK-IFU','Ultraleichtflug Schmidtler, Enduro','D-MIFU','DE'],
        ['NERC','De Havilland Canada, DHC-6 Twin Otter','VP-FAZ','GB'],
        ['NERC','De Havilland Canada, DHC-6 Twin Otter','VP-FBL','GB'],
        ['SAFIRE','ATR, ATR42-320','F-HMTO','FR'],
        ['SAFIRE','Piper Aircraft, PA23-250 Aztec','F-BLEB','FR'],
        ['SAFIRE','Dassault Aviation, Mystere / Falcon 20 GF','F-GBTM','FR'],
        ['UEDIN','Diamond Aircraft, HK36 TTC ECO Dimona','G-GEOS','GB']
        ]
    
    
    self.new_country_code = {
        'Afghanistan':'AF',
        'Aland Islands':'AX',
        'Albania':'AL',
        'Algeria':'DZ',
        'American Samoa':'AS',
        'Andorra':'AD',
        'Angola':'AO',
        'Anguilla':'AI',
        'Antarctica':'AQ',
        'Antigua And Barbuda':'AG',
        'Argentina':'AR',
        'Armenia':'AM',
        'Aruba':'AW',
        'Australia':'AU',
        'Austria':'AT',
        'Azerbaijan':'AZ',
        'Bahamas':'BS',
        'Bahrain':'BH',
        'Bangladesh':'BD',
        'Barbados':'BB',
        'Belarus':'BY',
        'Belgium':'BE',
        'Belize':'BZ',
        'Benin':'BJ',
        'Bermuda':'BM',
        'Bhutan':'BT',
        'Bolivia':'BO',
        'Bonaire':'BQ',
        'Bosnia And Herzegovina':'BA',
        'Botswana':'BW',
        'Bouvet Island':'BV',
        'Brazil':'BR',
        'British Indian Ocean Territory':'IO',
        'Brunei':'BN',
        'Bulgaria':'BG',
        'Burkina Faso':'BF',
        'Burundi':'BI',
        'Cabo Verde':'CV',
        'Cambodia':'KH',
        'Cameroon':'CM',
        'Canada':'CA',
        'Cayman Islands':'KY',
        'Central African Republic':'CF',
        'Chad':'TD',
        'Chile':'CL',
        'China':'CN',
        'Christmas Island':'CX',
        'Cocos Islands':'CC',
        'Colombia':'CO',
        'Comoros':'KM',
        'Congo, Democratic Republic':'CD',
        'Congo, Republic':'CG',
        'Cook Islands':'CK',
        'Costa Rica':'CR',
        "Cote d'Ivoire":'CI',
        'Croatia':'HR',
        'Cuba':'CU',
        'Curacao':'CW',
        'Cyprus':'CY',
        'Czech Republic':'CZ',
        'Denmark':'DK',
        'Djibouti':'DJ',
        'Dominica':'DM',
        'Dominican Republic':'DO',
        'Ecuador':'EC',
        'Egypt':'EG',
        'El Salvador':'SV',
        'Equatorial Guinea':'GQ',
        'Eritrea':'ER',
        'Estonia':'EE',
        'Ethiopia':'ET',
        'Falkland Islands':'KF',
        'Faroe Islands':'FO',
        'Fiji':'FJ',
        'Finland':'FI',
        'France':'FR',
        'French Guiana':'GF',
        'French Polynesia':'PF',
        'French Southern Territories':'TF',
        'Gabon':'GA',
        'Gambia':'GM',
        'Georgia, Republic':'GE',
        'Germany':'DE',
        'Ghana':'GH',
        'Gibraltar':'GI',
        'Greece':'GR',
        'Greenland':'GL',
        'Grenada':'GD',
        'Guadeloupe':'GP',
        'Guam':'GU',
        'Guatemala':'GT',
        'Guernsey':'GG',
        'Guinea':'GN',
        'Guinea-Bissau':'GW',
        'Guyana':'GY',
        'Haiti':'HT',
        'Heard Island and McDonald':'HM',
        'Holy See':'VA',
        'Honduras':'HN',
        'Hong Kong':'HK',
        'Hungary':'HU',
        'Iceland':'IS',
        'India':'IN',
        'Indonesia':'ID',
        'Iran':'IR',
        'Iraq':'IQ',
        'Ireland':'IE',
        'Isle of Man':'IM',
        'Israel':'IL',
        'Italy':'IT',
        'Jamaica':'JM',
        'Japan':'JP',
        'Jersey':'JE',
        'Jordan':'JO',
        'Kazakhstan':'KZ',
        'Kenya':'KE',
        'Kiribati':'KI',
        "Korea (the Democratic People's Republic of)":'KP',
        'Korea (the Republic of)':'KR',
        'Kuwait':'KW',
        'Kyrgyzstan':'KG',
        "Lao People's Democratic Republic (the)":'LA',
        'Latvia':'LV',
        'Lebanon':'LB',
        'Lesotho':'LS',
        'Liberia':'LR',
        'Libya':'LY',
        'Liechtenstein':'LI',
        'Lithuania':'LT',
        'Luxembourg':'LU',
        'Macao':'MO',
        'Macedonia':'MK',
        'Madagascar':'MG',
        'Malawi':'MW',
        'Malaysia':'MY',
        'Maldives':'MV',
        'Mali':'ML',
        'Malta':'MT',
        'Marshall Islands':'MH',
        'Martinique':'MQ',
        'Mauritania':'MR',
        'Mauritius':'MU',
        'Mayotte':'YT',
        'Mexico':'MX',
        'Micronesia':'FM',
        'Moldova':'MD',
        'Monaco':'MC',
        'Mongolia':'MN',
        'Montenegro':'ME',
        'Montserrat':'MS',
        'Morocco':'MA',
        'Mozambique':'MZ',
        'Myanmar':'MM',
        'Namibia':'NA',
        'Nauru':'NR',
        'Nepal':'NP',
        'Netherlands':'NL',
        'New Caledonia':'NC',
        'New Zealand':'NZ',
        'Nicaragua':'NI',
        'Niger':'NE',
        'Nigeria':'NG',
        'Niue':'NU',
        'Norfolk Island':'NF',
        'Northern Mariana Islands':'MP',
        'Norway':'NO',
        'Oman':'OM',
        'Pakistan':'PK',
        'Palau':'PW',
        'Palestine':'PS',
        'Panama':'PA',
        'Papua New Guinea':'PG',
        'Paraguay':'PY',
        'Peru':'PE',
        'Philippines':'PH',
        'Pitcairn':'PN',
        'Poland':'PL',
        'Portugal':'PT',
        'Puerto Rico':'PR',
        'Qatar':'QA',
        'Reunion':'RE',
        'Romania':'RO',
        'Russia':'RU',
        'Rwanda':'RW',
        'Saint Helena, Ascension and Tristan da Cunha':'SH',
        'Saint Kitts and Nevis':'KN',
        'Saint Lucia':'LC',
        'Saint Martin':'MF',
        'Saint Pierre and Miquelon':'PM',
        'Saint Vincent and the Grenadines':'VC',
        'Samoa':'WS',
        'San Marino':'SM',
        'Sao Tome And Principe':'ST',
        'Saudi Arabia':'SA',
        'Senegal':'SN',
        'Serbia':'RS',
        'Seychelles':'SC',
        'Sierra Leone':'SL',
        'Singapore':'SG',
        'Sint Maarten':'SX',
        'Slovakia':'SK',
        'Slovenia':'SI',
        'Solomon Islands':'SB',
        'Somalia':'SO',
        'South Africa':'ZA',
        'South Georgia and the South Sandwich Island':'GS',
        'South Sudan':'SS',
        'Spain':'ES',
        'Sri Lanka':'LK',
        'Sudan':'SD',
        'Suriname':'SR',
        'Svalbard And Jan Mayen':'SJ',
        'Swaziland':'SZ',
        'Sweden':'SE',
        'Switzerland':'CH',
        'Syria':'SY',
        'Taiwan':'TW',
        'Tajikistan':'TJ',
        'Tanzania':'TZ',
        'Thailand':'TH',
        'Timor-Leste':'TL',
        'Togo':'TG',
        'Tokelau':'TK',
        'Tonga':'TO',
        'Trinidad And Tobago':'TT',
        'Tunisia':'TN',
        'Turkey':'TR',
        'Turkmenistan':'TM',
        'Turks And Caicos Islands':'TC',
        'Tuvalu':'TV',
        'Uganda':'UG',
        'Ukraine':'UA',
        'United Arab Emirates':'AE',
        'United Kingdom':'GB',
        'United States Minor Outlying Islands':'UM',
        'United States of America':'US',
        'Uruguay':'UY',
        'Uzbekistan':'UZ',
        'Vanuatu':'VU',
        'Venezuela':'VE',
        'Vietnam':'VN',
        'Virgin Islands (British)':'VG',
        'Virgin Islands (U.S.)':'VI',
        'Wallis And Futuna':'WF',
        'Western Sahara':'EH',
        'Yemen':'YE',
        'Zambia':'ZM',
        'Zimbabwe':'ZW'}
    
    
    
    self.countries = [
                      "Make a choice...",
                      "Afghanistan",
                      "Albania",
                      "Algeria",
                      "Amazonia",
                      "American Samoa",
                      "Amsterdam And St. Paul Islands",
                      "Andaman Islands",
                      "Andorra",
                      "Angola",
                      "Anguilla",
                      "Antigua And Barbuda",
                      "Argentina","Armenia",
                      "Aruba",
                      "Ascension Island",
                      "Australia",
                      "Austria",
                      "Azerbaijan",
                      "Bahamas",
                      "Bahrain",
                      "Baker Island",
                      "Bangladesh",
                      "Barbados",
                      "Belarus",
                      "Belgium",
                      "Belize",
                      "Benin",
                      "Bhutan",
                      "Bolivia",
                      "Bonaire",
                      "Bosnia And Herzegovina",
                      "Botswana",
                      "Bouvet Island",
                      "Brazil",
                      "British Isles",
                      "Brunei",
                      "Bulgaria",
                      "Burkina Faso",
                      "Burma",
                      "Burundi",
                      "Cambodia",
                      "Cameroon",
                      "Canada",
                      "Caribbean",
                      "Cayman Islands",
                      "Central African Republic",
                      "Ceuta",
                      "Chad",
                      "Channel Islands",
                      "Chile",
                      "China",
                      "Christmas Island",
                      "Cocos Islands",
                      "Colombia",
                      "Comoros",
                      "Congo, Democratic Republic",
                      "Congo, Republic",
                      "Cook Islands",
                      "Corsica",
                      "Costa Rica",
                      "Cote D'ivoire",
                      "Croatia",
                      "Crozet Islands",
                      "Cuba",
                      "Curacao",
                      "Cyprus",
                      "Czech Republic",
                      "Denmark",
                      "Dhekelia",
                      "Djibouti",
                      "Dominica",
                      "Dominican Republic",
                      "Ecuador",
                      "Egypt",
                      "El Salvador",
                      "Equatorial Guinea",
                      "Eritrea",
                      "Estonia",
                      "Ethiopia",
                      "Faeroe Islands",
                      "Falkland Islands",
                      "Fiji",
                      "Finland",
                      "France",
                      "French Guiana",
                      "French Polynesia",
                      "Gabon",
                      "Galapagos Islands",
                      "Gambia",
                      "Gaza Strip",
                      "Georgia, Republic",
                      "Germany",
                      "Ghana",
                      "Gibraltar",
                      "Gough Island",
                      "Greece",
                      "Greenland",
                      "Grenada",
                      "Guadeloupe",
                      "Guam",
                      "Guatemala",
                      "Guinea",
                      "Guinea-Bissau",
                      "Guyana",
                      "Haiti",
                      "Hawaii Island",
                      "Hawaiian Islands",
                      "Honduras",
                      "Hong Kong",
                      "Howland Island",
                      "Hungary",
                      "Iceland",
                      "India",
                      "Indonesia",
                      "Iran",
                      "Iraq",
                      "Ireland",
                      "Israel",
                      "Italy",
                      "Jamaica",
                      "Japan",
                      "Jarvis Island",
                      "Johnston Atoll",
                      "Jordan",
                      "Kahoolawe",
                      "Kauai",
                      "Kazakhstan",
                      "Kenya",
                      "Kerguelen Islands",
                      "Kingman Reef",
                      "Kiribati",
                      "Kosovo",
                      "Kuwait",
                      "Kyrgyzstan",
                      "Laeso",
                      "Lake Chad",
                      "Lake Malawi",
                      "Lake Tanganyika",
                      "Lake Victoria",
                      "Lanai",
                      "Laos",
                      "Latvia",
                      "Lebanon",
                      "Lesotho",
                      "Liberia",
                      "Libya",
                      "Liechtenstein",
                      "Lithuania",
                      "Luxembourg",
                      "Macau",
                      "Macedonia",
                      "Madagascar",
                      "Madeira",
                      "Malawi",
                      "Malaysia",
                      "Maldives",
                      "Mali",
                      "Malta",
                      "Marshall Islands",
                      "Martinique",
                      "Maui",
                      "Mauritania",
                      "Mauritius",
                      "Melanesia",
                      "Mexico",
                      "Micronesia",
                      "Midway Atoll",
                      "Moldova",
                      "Molokai",
                      "Monaco",
                      "Mongolia",
                      "Montenegro",
                      "Montserrat",
                      "Morocco",
                      "Mozambique",
                      "Namibia",
                      "Nauru",
                      "Navassa Island",
                      "Nepal",
                      "Netherlands Antilles",
                      "Netherlands",
                      "New Caledonia",
                      "New Zealand",
                      "Nicaragua",
                      "Nicobar Islands",
                      "Niger",
                      "Nigeria",
                      "Niihau",
                      "Niue",
                      "Norfolk Island",
                      "North Korea",
                      "Northern Mariana Islands",
                      "Norway",
                      "Oahu",
                      "Okinawa",
                      "Oman",
                      "Pakistan",
                      "Palau",
                      "Palestine",
                      "Palmyra Atoll",
                      "Panama",
                      "Papua New Guinea",
                      "Paraguay",
                      "Peru",
                      "Philippines",
                      "Pitcairn Island",
                      "Pitcairn Islands",
                      "Poland",
                      "Polynesia",
                      "Portugal",
                      "Puerto Rico",
                      "Qatar",
                      "Red Sea",
                      "Reunion",
                      "Romania",
                      "Russia",
                      "Rwanda",
                      "Saba",
                      "Sable Island",
                      "Samoa",
                      "San Marino",
                      "Sao Tome And Principe",
                      "Sardinia",
                      "Saudi Arabia",
                      "Scandinavia",
                      "Senegal",
                      "Serbia",
                      "Seychelles",
                      "Sicily",
                      "Sierra Leone",
                      "Singapore",
                      "Slovakia",
                      "Slovenia",
                      "Solomon Islands",
                      "Somalia",
                      "South Africa",
                      "South Georgia Island",
                      "South Korea",
                      "South Orkney Islands",
                      "South Sandwich Islands",
                      "Spain",
                      "Spratly Islands",
                      "Sri Lanka",
                      "St Barthelemy",
                      "St Eustatius",
                      "St Helena",
                      "St Kitts And Nevis",
                      "St Lucia",
                      "St Maarten",
                      "St Martin",
                      "St Pierre And Miquelon",
                      "St Vincent And The Grenadines",
                      "Sudan",
                      "Suriname",
                      "Svalbard And Jan Mayen",
                      "Swaziland",
                      "Sweden",
                      "Switzerland",
                      "Syria",
                      "Taiwan",
                      "Tajikistan",
                      "Tanzania",
                      "Thailand",
                      "Togo",
                      "Tokelau",
                      "Tonga",
                      "Trinidad And Tobago",
                      "Tristan Da Cunha",
                      "Tunisia",
                      "Turkey",
                      "Turkmenistan",
                      "Turks And Caicos Islands",
                      "Tuvalu",
                      "Uganda",
                      "Ukraine",
                      "United Arab Emirates",
                      "United Kingdom",
                      "United States of America",
                      "Uruguay",
                      "Uzbekistan",
                      "Vanuatu",
                      "Vatican City",
                      "Venezuela",
                      "Vietnam",
                      "Virgin Islands",
                      "Wake Island",
                      "Wallis And Futuna Islands",
                      "Yemen",
                      "Zambia",
                      "Zanzibar",
                      "Zimbabwe"]
    
    self.locations = [
                      "Make a choice...",
                      "Continents",
                      "Countries",
                      "Oceans",
                      "Regions"
                      ]
    
    self.continents = [
                       "Make a choice...",
                       "Africa",
                       "Antarctica",
                       "Asia",
                       "Oceania",
                       "Europe",
                       "North America",
                       "South America"
                       ]
    
    self.oceans = [
                   "Make a choice...",
                   "Atlantic Ocean",
                   "Arctic Ocean",
                   "Indian Ocean",
                   "Pacific Ocean",
                   "Southern Ocean"
                   ]
    
    self.regions = [
                    "Make a choice...",
                    "Arctic Region",
                    "Atlantic Ocean Islands",
                    "Central Africa",
                    "Central America",
                    "Central Europe",
                    "Eastern Africa",
                    "Eastern Asia",
                    "Eastern Europe",
                    "Indian Ocean Islands",
                    "Middle East",
                    "North America",
                    "Northern Africa",
                    "Northern Europe",
                    "Pacific Islands",
                    "South America",
                    "Southcentral Asia",
                    "Southern Asia",
                    "Southern Europe",
                    "Western Africa",
                    "Western Asia",
                    "Western Europe"
                    ]
    
    self.buttonInformation = [
                              "<p align=justify>Use this button to add a new checkbox. Each activate"
                              + "d checkbox is then saved in the XML file with the code <b>xx_User</"
                              + "b>.</p><p align=center style='color:#C80000'><b>All non-activated c"
                              + "heckboxes will not be saved and will be lost.</b></p><p align=justi"
                              + "fy>As the PDF report generator is limited to 12 checkboxes per sect"
                              + "ion, you cannot create more than 12 checkboxes per section in ASMM "
                              + "Creator Online.</p>",
                              "<p align=justify>This is the acronym of the project.</p><p><u>Exampl"
                              + "e:</u> DACCIWA</p>",
                              "<p align=justify>This is the date of the flight.<p><u>Example:</u> 2"
                              + "016/02/05</p>",
                              "<p align=justify>This element uniquely identifies the flight and it"
                              + " is generally formed with mandatory and/or optional string codes. T"
                              + "his element is then used to name the ASMM xml file.</p><p><u>Exampl"
                              + "e:</u> PS001_20160205_xxxxx</p>",
                              "<p align=justify>This is the name of the Project Investigator.</p><"
                              + "p><u>Example:</u> John Doe</p>",
                              "<p align=justify>This is the name of the person in charge of the fl"
                              + "ight.</p><p><u>Example:</u> Jane Doe</p>",
                              "<p align=justify>The institution operating the aircraft has to be c"
                              + "hosen first, then a new list to select the aircraft will be availab"
                              + "le.</p><p><u>Example:</u> SAFIRE - ATR-42</p>",
                              "<p align=justify>The location of the flight. Once the category has "
                              + "been selected, details will be available.</p><p><u>Example:</u> Cou"
                              + "ntries - France</p>",
                              "<p align=justify>This is the name of the person who created the cur"
                              + "rent ASMM file.</p><p><u>Example:</u> John Doe</p>",
                              "<p align=justify>This is the role of the person who created the cur"
                              + "rent ASMM file.</p><p><u>Example:</u> Scientist</p>",
                              "<p align=justify>This is the electronic address of the person who c"
                              + "reated the current ASMM file.</p><p><u>Example:</u> John.Doe@email."
                              + "com</p>",
                              "<p align=justify>This is the extent of the resource in the geographic"
                              + " space, given as a bounding box. The southbound and northbound long"
                              + "itudes of the bounding box shall be expressed in decimal degree (-9"
                              + "0.00 for South to 90.00 for North) with a precision of two decimals"
                              + ".</p>",
                              "<p align=justify>This is the extent of the resource in the geographic"
                              + " space, given as a bounding box. The westbound and eastbound longit"
                              + "udes of the bounding box shall be expressed in decimal degree (-180"
                              + ".00 for West to 180.00 for East) with a precision of two decimals.<"
                              + "/p>",
                              "<p align=justify>This is the extent of the resource in the geographic"
                              + " space, given as a bounding box. The minimum and maximum altitudes "
                              + "of the bounding box shall be expressed in meters (0.00 for the grou"
                              + "nd to xxxx.xx for the maximum altitude) with, if possible, a precis"
                              + "ion of two decimals.</p>",
                              "<p align=justify>If the flight was in linked to supporting surface-"
                              + "based instruments, you can add there name here.</p><p><u>Example:</"
                              + "u> CIMEL sunphotometers</p>",
                              "<p align=justify>In this field, you can write comments based on the"
                              + " category to which the field belongs to.</p>",
                              "<p align=justify>Checkboxes are here to give details about a flight"
                              + ". It can be scientific aims, details about the clouds, or manoeuvre"
                              + "s performed by the aircraft.</p>"
                              ]
    
    self.mandatory_line_edit_list = [
        [self.projectAcronym_ln, self.projectAcronym_lb, "text", 0],
        [self.flightNumber_ln, self.flightNumber_lb, "text", 0],
        [self.missionSci_ln, self.missionSci_lb, "text", 0],
        [self.flightManager_ln, self.flightManager_lb, "text", 0],
        [self.newOperator_ln, self.operator_lb, "text", 0],
        [self.newAircraft_ln, self.aircraft_lb, "text", 0],
        [self.contactName_ln, self.contactName_lb, "text", 1],
        [self.contactEmail_ln, self.contactEmail_lb, "email", 1]
        ]
    
    self.mandatory_combobox_list = [
        [self.operator_cb, self.operator_lb, 0],
        [self.aircraft_cb, self.aircraft_lb, 0],
        [self.location_cb, self.location_lb, 0],
        [self.detailList, self.location_lb, 0],
        [self.contact_cb, self.contact_lb, 1]
        ]
    
    self.mandatory_datebox_list = [
        [self.date_dt, self.date_lb, 0]
        ]
    
    self.coordinate_units_list = {
        "°n": 2,
        "°e": 2,
        "°N": 2,
        "°E": 2,
        "n": 1,
        "e": 1,
        "m": 1,
        "N": 1,
        "E": 1,
        "M": 1,
        "°s": -2,
        "°w": -2,
        "°S": -2,
        "°W": -2,
        "s": -1,
        "w": -1,
        "S": -1,
        "W": -1,
        "°": 0
        }
    
    logging.debug('sql_functions.py - MyAbout - objectsInit finished')
    
    