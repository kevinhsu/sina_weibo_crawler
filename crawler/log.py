#!/usr/bin/env python
#coding=utf-8
'''
 Created on 2014-7-10
 Author: Gavin_Han
 Email: muyaohan@gmail.com
'''

import logging
import logging.handlers
import os,sys

from conf.config import instance_index

class FixedLogger(logging.Logger):
    def exception(self, msg, *args):
        """
        Convenience method for logging an ERROR with exception information.
        """
        extra = {'instance': instance_index}
        self.error(msg, exc_info=1, extra=extra, *args)

def get_logger(filename):
    logger = FixedLogger(logging.getLogger('crawler'))
    
    handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # set level to INFO
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    return logger

# if getattr(sys, 'frozen', None):
#     basedir = sys._MEIPASS
# else:
#     basedir = os.path.dirname(__file__)
if getattr(sys, 'frozen', None):
    basedir = os.path.abspath(os.path.dirname(sys.executable))  
else:
    basedir = os.path.dirname(os.path.abspath(__file__))
logger = get_logger(os.path.join(basedir, 'crawler.log'))