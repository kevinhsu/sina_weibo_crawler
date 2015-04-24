#!/usr/bin/env python
#coding=utf-8
f=open('follows_fans.txt','r')
s=open('list.txt','w')
while True:
	line=f.readline()
	if not line:break

	part=line.split(':')
	if (part[0]=="follow"):
		s.write(part[1]+'\n')

f.close()
s.close()

