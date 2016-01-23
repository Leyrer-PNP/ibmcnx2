'''
** Create a documentation of j2ee roles **

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       5.0.1
Date:          09/19/2015

License:       Apache 2.0
'''


def convertRoles2Dict(appname, list):
    # function to convert backup txt files of Security Role Backup to a dictionary
    # print '\tPATH: ' + path
    count = 0
    dict = {}

    for line in list.splitlines():
        # for loop through file to read it line by line
        if (':' in line) and (count > 12):
            value = line.split(':')[0]
            # cred = line.split(':')[1].strip('\n')
            cred = line.split(':')[1]
            # cred = cred.strip(' ')
            cred = cred.strip()
            if value == "Role":
                role = cred
                dict[role] = {}
            dict[role][value] = cred.replace('|', ', ')
        count += 1
    return dict

apps = AdminApp.list()
appsList = apps.splitlines()

for app in appsList:
    dictionary = convertRoles2Dict(app, AdminApp.view(app, "-MapRolesToUsers"))
    print "\n\n==== " + app.upper() + "\n"
    print "[cols=\"1,1,1,1,1\", options=\"header\"]"
    print "|==="
    print "|Role |Everyone |All authenticated |Mapped Users |Mapped Groups"

    for role in dictionary.keys():
        # Loop through Roles
        print "|" + role.upper()
        print "|" + dictionary[role]['Everyone?']
        print "|" + dictionary[role]['All authenticated?']
        print "|" + dictionary[role]['Mapped users']
        print "|" + dictionary[role]['Mapped groups']

    print "|==="
