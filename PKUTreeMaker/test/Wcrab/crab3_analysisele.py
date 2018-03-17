from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'SEle16B-v1'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles =['Summer16_23Sep2016BCDV4_DATA_L1FastJet_AK4PFchs.txt','Summer16_23Sep2016BCDV4_DATA_L2Relative_AK4PFchs.txt','Summer16_23Sep2016BCDV4_DATA_L3Absolute_AK4PFchs.txt','Summer16_23Sep2016BCDV4_DATA_L2L3Residual_AK4PFchs.txt','Summer16_23Sep2016BCDV4_DATA_L1FastJet_AK4PFPuppi.txt','Summer16_23Sep2016BCDV4_DATA_L2Relative_AK4PFPuppi.txt','Summer16_23Sep2016BCDV4_DATA_L3Absolute_AK4PFPuppi.txt','Summer16_23Sep2016BCDV4_DATA_L2L3Residual_AK4PFPuppi.txt']
# Name of the CMSSW configuration file
config.JobType.psetName    = 'analysis_data.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 80
config.Data.lumiMask = 'Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
#config.Data.runRange = '246908-258750'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'SEle16B-v1'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'  #2_CH_CERN'



