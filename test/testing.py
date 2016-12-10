'''
Created on Mar 11, 2016

@author: eric
'''

from util.logger import Logger

log = Logger('app.log')


log.info('test line')

log.getlogger('sec.tion')

log.debug('Quick zephyrs blow, vexing daft Jim.')
log.info('How quickly daft jumping zebras vex.')
log.warning('Jail zesty vixen who grabbed pay from quack.')
log.error('The five boxing wizards jump quickly.')
