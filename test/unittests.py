'''
Created on Mar 11, 2016

@author: eric
'''
import unittest
from util.config import Config



class Test(unittest.TestCase):


    def setUp(self):
        self.config1 = Config('conf_file_1.cfg')
        self.config2 = Config('conf_file_2.cfg')


    def tearDown(self):
        pass


    def testConfig(self):
        self.assertTrue(self.config1.getConfigVar("testsection", "test")=='ok')
        self.assertTrue(self.config2.getConfigVar("testsection", "test")=='ok')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConfig']
    unittest.main()