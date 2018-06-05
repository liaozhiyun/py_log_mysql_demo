#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%Y-%m-%d %H:%M:%S',  
                    filename='./run.log',  
                    filemode='a')  
''' 
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message') 
'''
