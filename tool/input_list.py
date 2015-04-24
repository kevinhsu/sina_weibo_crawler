#!/usr/bin/env python
#coding=utf-8
"""
	返回crawl_list
"""

import sys
sys.path.append("..")
from conf.config import mypath

path=mypath+'list.txt'
try:
	f=open(path,'r')
except Exception, e:
	print path,'does not exist'
	sys.exit(1)

crawl_list=[]
while True:
	line=f.readline()
	if not line:break

	crawl_list.append(line.strip())		
f.close()

