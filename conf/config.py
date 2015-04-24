#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Created on 2014-7-10
 Author: Gavin_Han
 Email: muyaohan@gmail.com

 Modeified on 2015-4-19
 Author: Fancy
 Email: springzfx@gmail.com
'''

import os,sys
import yaml


if getattr(sys, 'frozen', None):
    base = os.path.abspath(os.path.dirname(sys.executable))  
else:
    base = os.path.dirname(os.path.abspath(__file__))

# base = os.path.dirname(os.path.abspath(__file__))
user_conf = os.path.join(base, 'conf.yaml')
print "Read:   "+user_conf

conf_file = open(user_conf)
config = yaml.load(conf_file)

login_list = config['login']

threadNum = config['threadnum']
# startUid = config['startUid']

mongo_host = config['mongo']['host']
mongo_port = config['mongo']['port']
db_name = config['db']

instances = config['instances']
mypath = config['mypath']

instance_index = config['instance_index']

cookiepath = os.path.join(base,'savecookie.txt')

data=config['data']