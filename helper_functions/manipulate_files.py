'''
Created on 10 jun. 2015

@author: cornetee
'''

import shutil, os

###
### Variables
###

secapicfg_dir = "C:\\tools\\Deployit\\rwa\\"
secapicfg_file= "manipulate_file.txt"
applicationcode = "bbs"


###
### Helper functions
###
def fileOpen(src_dir, src_file):
    # Backup file in current directory
    shutil.copyfile(src_dir+src_file, src_dir+src_file + ".backup")

    # Open file
    # r+: reading and writing
    file_to_manipulate = open(src_dir+src_file, "r+")
    
    print "Open file: " + src_file
    print "Ready for file manipulations..."
    print "..."
    return file_to_manipulate

# ?
def closeFile(file_to_manipulate, src_dir, src_file):
    # Close file
    print "Closing file: " + file_to_manipulate.name
    file_to_manipulate.close()   
    
    # Rename file
    # if rwaapplication
    os.chdir(secapicfg_dir)
    os.rename(secapicfg_file,"secapi-" + applicationcode + ".cfg")   

    
###
### Secapi.cfg
###
secapi = fileOpen(secapicfg_dir, secapicfg_file)

for line in secapi:
    secapi.write(line.replace("DirSrv=","DirSrv=test_substitutie"))
    


# Close file
print "Closing file: " + secapi.name
secapi.close()   

# Rename file
# if rwaapplication
os.chdir(secapicfg_dir)
os.rename(secapicfg_file,"secapi-" + applicationcode + ".cfg")  


