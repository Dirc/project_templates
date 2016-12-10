'''
Created on 10 dec 2016

@author: Dirc
Based on borstg
'''


import requests
from classes.config import Config
import json

class Rest(object):
    '''
    classdocs
    '''    
    config = Config()    

    def __init__(self,
                 url  = config.getConfig("rest", "url"),
                 user = config.getConfig("rest", "username"),
                 pwd  = config.getConfig("rest", "password"),
                 header_format = "application/json"):
        '''
        Constructor
        '''
        self.urlRoot       = url
        self.auth          = (user, pwd)
        self.header_format = header_format
        self.verify        = False
        self.session       = requests.Session()

    def printError(self, url, response):
            print "URL: " + url            
            print "Error-text: ", response.content
            print "http-status = s" + str(response.status_code)

        
    def get(self, uri, queryParms=None):
        url = self.urlRoot + uri
        headers = {'Accept': self.header_format} 
        # of: requests.get(...)           
        response = self.session.get(url, 
                                    params  = queryParms, 
                                    headers = headers, 
                                    verify  = self.verify,
                                    auth    = self.auth)       
        # Error        
        if response.status_code != requests.codes.get('ok'):
            self.printError(url, response)
        # Response
        return response.json()

    def post(self, uri, queryParms=None, data=None):
        url = self.urlRoot + uri
        headers = {'Content-type': self.header_format}
        response = requests.post(url, 
                                 params  = queryParms, 
                                 headers = headers, 
                                 verify  = self.verify,
                                 auth    = self.auth,
                                 data    = data)
        # Error        
        if response.status_code not in (requests.codes.get('ok'), requests.codes.get('no_content')):
            self.printError(url, response)
        # Response
        #return response.json()

    def put(self, uri, queryParms=None, data=None):
        url = self.urlRoot + uri
        headers = {'Content-type': self.header_format,'Accept': self.header_format}
        response = requests.put(url, 
                                params  = queryParms, 
                                headers = headers, 
                                verify  = self.verify,
                                auth    = self.auth,
                                data    = data)
        # Error
        if response.status_code not in (requests.codes.get('ok'), requests.codes.get('no_content')):
            self.printError(url, response)
        # Response
        return response.json()
     
    def dell(self, uri, queryParms=None):
        url = self.urlRoot + uri
        response = self.session.delete(url, 
                                       params  = queryParms,
                                       verify  = self.verify,
                                       auth    = self.auth)
                                        
        if response.status_code not in (requests.codes.get('ok'), requests.codes.get('no_content')):
            self.printError(url, response)
        # Response
        #return response.json()
        
        
if __name__ == '__main__':
    rest = Rest()
    uri = "testuri"
    output = rest.get(uri)
    print output
    output = rest.get(uri)
    print output