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
    
    #instancemethod    
    def getParams(self):
        return self.params
    
    @staticmethod
    def classIndependentMethod(x,y):
        # Method is independent from data of the class or instance
        # Note: there is no self parameters
        return x, y
    
    @classmethod
    def instanceIndependentMethod(cls):
        # Method is independent from individual instances
        # Dependendt from class
        # Note: the self parameter is changed to the cls parameter.
        pass

class SubClass(SuperClass):
    def __init__(self, extra_params):
        SuperClass.__init__(self, "params_SuperClass_values")
        self.extra_params = extra_params
        
    def getExtraParams(self):
        return self.extra_params