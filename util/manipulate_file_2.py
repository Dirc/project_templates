'''
Created on 10 jun. 2015

@author: cornetee
'''


import fileinput
import re

###
### Variables
###

secapicfg_dir = "C:\\tools\\Deployit\\rwa\\"
secapicfg_file= "manipulate_file.txt"
applicationcode = "bbs"



def replaceLine2(filename, search_string, replace_line):
    #Add wildcard to pattern to replace whole line containing this string.
    search_pattern = search_string + "*.*"
    for line in fileinput.input(filename, inplace=1, backup='.backup'):
        line = re.sub(search_pattern, replace_line, line.rstrip())
        print(line)
    print "New value: " + replace_line

#replaceLine(secapicfg_dir+secapicfg_file, "DirSrv=","DirSrv=test_substitutie")
#replaceLine(secapicfg_dir+secapicfg_file, "LogMode=","LogMode=3")

line = "/=/etc/rwa/secapi.cfg"
search_string = "/=/etc/rwa/secapi.cfg"

search_pattern = "" + search_string + ".*"
pattern_found = False
if re.search(search_pattern, line):
    pattern_found = True

print "STRING FOUND"
print pattern_found



print "\n\n####################################\n"    

def configureCgi(filename, env):
    # define Directory CGI OT
    directory_cgi_ot = """<Directory "/usr/local/rwa/cgi-bin">
    AllowOverride None
    Options None
    Order deny,allow
    Allow from all
    # we only allow connections from localhost, for 2 reasons:
    # - prevent inter-host communications where RWA-client on host A connects to RWA CGI on host B
    # - checkconfig discloses security related information
</Directory>"""
    # define Directory CGI AP
    directory_cgi_ap = """<Directory "/usr/local/rwa/cgi-bin">
    AllowOverride None
    Options None
    Order deny,allow
    Deny from all
    # we only allow connections from localhost, for 2 reasons:
    # - prevent inter-host communications where RWA-client on host A connects to RWA CGI on host B
    # - checkconfig discloses security related information
    Allow from localhost 127.0.0.1
</Directory>"""
    
    # Determine CGI
    if env == "o" or env == "t" :        
        directory_cgi_env = directory_cgi_ot
        print "Configure CGI for OT"
    elif env == "a" or env == "pa" or env == "p":
        directory_cgi_env = directory_cgi_ap
        print "Configure CGI for AP"
    else:
        print "Error, can't evaluate environment value: " + str(env)
        print "Allowed values: o, t, a, pa, p."
    
    # Replace CGI
    cgi_pattern = "^<Directory " + ".*"
    for line in fileinput.input(filename, inplace=1):
        if re.match(cgi_pattern, line):
            print directory_cgi_env
            fileinput.close()
        else:
            print line.rstrip()
    fileinput.close()


    
configureCgi(secapicfg_dir + "testfile", "o") 
print "Done..."   
    

print "\n\n####################################\n"       

import os

# Check if file exists os.access return True, False
def checkIfFileExist(filename):  
    if os.access(filename,os.F_OK) == True:
        print "File exists on host: " + filename
    else:
        print "ERROR File doesn't exists on host: " + filename    
    
checkIfFileExist("testfiles")   

print "\nDone" 
    
    
    
    
    
    