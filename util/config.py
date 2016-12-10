'''
Created on 5 nov. 2014

@author: borstg
'''
import ConfigParser
import os

class Config(object):
    '''
    classdocs
    '''
    config = ConfigParser.ConfigParser()

    def __init__(self, conf_filename):
        '''
        Constructor
        '''    
        self.conf_filename = conf_filename
        self.config = ConfigParser.ConfigParser()
        self.app_base = os.path.dirname(os.path.dirname(__file__))
        self.config_file = os.path.join(self.app_base,'config_templates',self.conf_filename)
        self.config.read(self.config_file)
        
    def getConfigVar(self, item, key):
        return self.config.get(item,key)
    
    def isDebugEnabled(self):
        return self.config.get('config','debug') == 'on'
    
    def configInfo(self):
        return self.app_base, self.config_file
    
    
    
if __name__ == '__main__':    
        config = Config()
        print config.config_file