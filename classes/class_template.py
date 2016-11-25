'''
Created on 25 nov. 2016

@author: Eric Cornet
'''

class SuperClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.params = params
        
    def getParams(self):
        return self.params
    
    @staticmethod
    def classIndependentMethod(x,y):
        # Method is independent from data of the class
        # Note: there is no self parameters
        return x, y
    

class SubClass(SuperClass):
    def __init__(self, extra_params):
        SuperClass.__init__(self, "params_SuperClass_values")
        self.extra_params = extra_params
        
    def getExtraParams(self):
        return self.extra_params