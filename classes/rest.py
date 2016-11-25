'''
Created on 5 nov. 2014

@author: borstg
'''


import requests
from classes.config import Config
import json

class Rest(object):
    '''
    classdocs
    '''    
    config = Config()    

    def __init__(self):
        '''
        Constructor
        '''
        self.session = requests.Session()
        self.verify = False
        self.urlRoot = self.config.getConfigVar('waaa', 'waaa_url')
        self.auth = (self.config.getConfigVar('waaa', 'waaa_user'),self.config.getConfigVar('waaa', 'waaa_pswd'))

    def restGet(self, uri, queryParms=None):
        urlStr = self.urlRoot + uri
        if self.config.isDebugEnabled():
            print '>>>> DEBUG <<<< ' + Rest.restGet.__name__ + ': urlStr=' + urlStr 
            
        headers = {'Accept': 'application/json'}        
        response = self.session.get(urlStr, params=queryParms , headers=headers, verify=self.verify)       
        if self.config.isDebugEnabled():
                print Rest.restGet.__name__ + ' response content:', response.content
                
        if response.status_code != requests.codes.get('ok'):            
            print Rest.restGet.__name__ + ' error-text:', response.content
            raise RestException('RestException http-status=' + str(response.status_code))
        return response.json()
     
    def restDel(self, uri, queryParms=None):
        urlStr = self.urlRoot + uri
        if self.config.isDebugEnabled():
            print '>>>> DEBUG <<<< ' + Rest.restDel.__name__ + ': urlStr=' + urlStr
        response = self.session.delete(urlStr, params=queryParms, verify=self.verify, auth=self.auth) 
        if self.config.isDebugEnabled():
                print Rest.restDel.__name__ + ' response content:', response.content     
        
        if response.status_code not in (requests.codes.get('ok'), requests.codes.get('no_content')):
            print Rest.restDel.__name__ + ' error-text:', response.content
            raise RestException('RestException http-status=' + str(response.status_code))

    def restPost (self, uri, queryParms=None, jsonInput=None):
        urlStr = self.urlRoot + uri
        if self.config.isDebugEnabled():
            print '>>>> DEBUG <<<< ' + Rest.restPost.__name__ + ': urlStr=' + urlStr
            print '>>>> DEBUG <<<< ' + Rest.restPost.__name__ + ': payload=', jsonInput
        headers = {'Content-type': 'application/json'}
        response = requests.post(urlStr, headers=headers, params=queryParms, data=jsonInput, verify=self.verify, auth=self.auth)
        if self.config.isDebugEnabled():
                print Rest.restPost.__name__ + ' response content:', response.content
        
        if response.status_code not in (requests.codes.get('ok'), requests.codes.get('no_content')):
            print Rest.restPost.__name__ + ' error-text:', response.content
            raise RestException('RestException http-status=' + str(response.status_code))

    def restPut (self, uri, queryParms=None, jsonInput=None):
        urlStr = self.urlRoot + uri
        if self.config.isDebugEnabled():
            print '>>>> DEBUG <<<< ' + Rest.restPut.__name__ + ': urlStr=' + urlStr
            print '>>>> DEBUG <<<< ' + Rest.restPut.__name__ + ': jsonInput=', jsonInput
        headers = {'Content-type': 'application/json','Accept': 'application/json'}
        response = requests.put(urlStr, headers=headers, params=queryParms, data=jsonInput, verify=self.verify, auth=self.auth)
        if self.config.isDebugEnabled():
                print Rest.restPut.__name__ + ' response content:', response.content
        
        if response.status_code not in (requests.codes.get('ok'), requests.codes.get('no_content')):
            print Rest.restPut.__name__ + ' error-text:', response.content
            raise RestException('RestException http-status=' + str(response.status_code))
        return response.json()
        
        
class RestException(Exception):
    '''
    classdocs
    '''


    def __init__(self, value):
        '''
        Constructor
        '''
        self.value = value
        
    def __str__ (self):
        return repr(self.value)

if __name__ == '__main__':
    rest = Rest()
    waaaUrl = rest.config.getConfigVar('waaa', 'waaa_url')
    output = rest.restGet('appservers/e1wa04')
    print output
    output = rest.restGet('lpars/lsrv3028')
    print output