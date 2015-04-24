#!/usr/bin/env python
#coding=utf-8

"""
 Created on 2015-4-19
 Author: Fancy
 Email: springzfx@gmail.com

"""

import sys
import urllib,urllib2
import chardet 
import random, time
import cookielib
sys.path.append("..")
from conf.config import cookiepath



class GetPage(object):
    def __init__(self,enableProxy=False):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        cj = cookielib.LWPCookieJar()
        #从文件中读取cookie
        if cookiepath is not None:
            cj.load(cookiepath)
        #将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
        cookie_processor = urllib2.HTTPCookieProcessor(cj)

        if enableProxy:
            proxy_support = urllib2.ProxyHandler({'http':'202.106.16.36:3128'})#使用代理
            self.opener = urllib2.build_opener(proxy_support, cookie_processor, urllib2.HTTPHandler)
            print "Proxy enabled"
        else:
            self.opener = urllib2.build_opener(cookie_processor, urllib2.HTTPHandler)
            
        #将包含了cookie、http处理器、http的handler的资源和urllib2对象绑定在一起
        urllib2.install_opener(self.opener)

               
    def fetch(self,url,span = False):
        print "fetch ",url
        if span:
            print "sleeping"
            time.sleep(random.uniform(0,40))
            print "waking"
            

        tries = 0
        while tries <= 6:
            try:    
                req = urllib2.Request(url= url, data=urllib.urlencode({}), headers=self.headers)
                result = urllib2.urlopen(req)  
                
                if result.geturl()!=url:
                    print result.geturl()
                    raise ValueError(result.geturl())

                html = result.read()
                chinesecode=chardet.detect(html)['encoding']
                html=html.decode(chinesecode).encode('utf-8')
                break
            except Exception, e:
                sec = 10 * (tries + 1) if tries <= 2 else (600 * (tries - 2) if tries < 6 else 3600)
                print "fetch sleeping"
                print e
                exit()
                time.sleep(sec)
                print "fetch waking"
                tries += 1
        if tries > 6:
            return None
        else:
            return html


page = GetPage()