'''
Created on 17 jun. 2015

@author: cornetee
'''


import shutil, os

###
### General Variables (default AND applicative)
###

etc_rwa_dir = "C:\\tools\\Deployit\\rwa\\"
secapicfg_file = "secapi.cfg"
urltable_file = "urltable.conf"

rwaconf_dir = "C:\\tools\\Deployit\\rwa\\"
rwaconf_file = "rwa.conf"

shutil.copy("rwa.conf.generic.ap", rwaconf_dir+rwaconf_file)
print "done..."

def configureRwaConf(filename, env):
    print "\n##### Configure rwa.conf: " + filename
    print "Environment detected: " + env
    # Remove original file    
    if os.access(filename,os.F_OK) == True:
        os.remove(filename)
        print "File removed"
    else:
        print "File doesn't exists on host."
    # Copy file from template 
    if env == "o" or env == "t":
        shutil.copy("rwa.conf.generic.ot", filename)
    elif env == "a" or env == "pa" or env == "p":
        shutil.copy("rwa.conf.generic.ap", filename)  
    else:
        print "Error, can't evaluate environment value: " + str(env)
        print "Allowed values: o, t, a, pa, p."
    # Set permissions
    print "chmod 644 " + filename   
    os.system("chmod 644 " + filename)
         
