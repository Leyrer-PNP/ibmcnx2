######
#  Change DataSource DB Host and Port
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.org
#
#  Version:       1.0
#  Date:          2014-10-31
#
#  License:       Apache 2.0
#
#  This scripts creates a list of all databases in scope Cell and changes 
#  the db host and port value

import ibmcnx.functions

# Ask user for new Database Host and Port
newDBHost = raw_input( 'New DB Host: ' )
newDBPort = raw_input( 'New DB Port: ' )

# Security Question if User really want to change:
answer = raw_input( 'Are sure to change the DB Host to ' + newDBHost + ':' + newDBPort + '?')
allowed_answer = ['yes', 'y', 'ja', 'j']

# Get a list of all DataSources
datasources = AdminConfig.list('DataSource', AdminConfig.getid( '/Cell:'+AdminControl.getCell()+'/' )).splitlines()
# new list for database names
dbList = []
for datasource in datasources:
    # split DataSource and DataSource ID
    datasource = datasource.split('(')
    ds = datasource[0]
    # Remove Default Datasources
    if ( ds != 'DefaultEJBTimerDataSource' ) and ( ds != 'OTiSDataSource' ):
        # check for " (e.g. "oauth provider)
        if ( len(ds.split('"')) > 1):
            ds = ds.split('"')[1]
        # write datasouce to database list
        dbList.append( ds )
dbList.sort()        

if answer.lower() in allowed_answer:
    for count in range(len(dbList)):
        db = dbList[count]
        # Loop through all databases in our dictionary
        print '\tChange DBHost for: ' + db.upper(),
        try:
            # get the id of the datasource
            dsid = ibmcnx.functions.getDSId( db )
            properties = AdminConfig.list('J2EEResourceProperty', dsid).splitlines()
            # Change dbHost and dbPort
            for prop in properties:
                propName = AdminConfig.showAttribute(prop, 'name') 
                if (propName == "serverName"):
                    AdminConfig.modify(prop,'[[value ' + newDBHost + ']]')
                elif (propName == "portNumber"):
                    AdminConfig.modify(prop,'[[value ' + newDBPort + ']]')
            print ' - successfully set!'
        except:
            print ' - ERROR'  
    ibmcnx.functions.saveChanges()
else:
    print '\t\tNothing changed! '
