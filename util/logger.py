'''
Created on Mar 11, 2016

@author: eric
'''
import logging
import os


'''
>>>> NOT FINISHED <<<<<
'''

class Logger(object):
    '''
    classdocs
    '''


    def __init__(self, log_filename='script.log'):
        '''
        Constructor
        '''
        self.log_filename = log_filename
        self.app_base = os.path.dirname(os.path.dirname(__file__))
        self.log_file = os.path.join(self.app_base,'log',self.log_filename)
        self.logging = logging
        
        # set up logging to file - see previous section for more details
        self.logging.basicConfig(level=logging.DEBUG,
                                          format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                          datefmt='%m-%d %H:%M',
                                          filename=self.log_file,
                                          filemode='w')
 
    def getlogger(self,section):
        self.logging.getLogger(section)
        print section
        
    def debug(self, msg):
        self.logging.debug(msg)

    def info(self, msg):
        self.logging.info(msg)
    
    def warning(self, msg):
        self.logging.warning(msg)

    def error(self, msg):
        self.logging.error(msg)
"""
# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
"""        