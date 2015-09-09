'''
Set the Version Stamp to actual time and date

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0
'''

import ibmcnx.functions

print "\nSet Version Stamp in LotusConnections-config.xml to actual Date and Time\n"

# Check properties if temppath is defined
if (ibmcnx.functions.tempPath() == ''):
    path = raw_input("Path and Folder where config is temporarily stored: ")
else:
    path = ibmcnx.functions.tempPath()

execfile("connectionsConfig.py")
LCConfigService.checkOutConfig(path, AdminControl.getCell())
LCConfigService.updateConfig("versionStamp", "")
LCConfigService.checkInConfig(path, AdminControl.getCell())
synchAllNodes()
