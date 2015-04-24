#!/usr/bin/env python
#coding=utf-8
'''
 Created on 2014-7-10
 Author: Gavin_Han
 Email: muyaohan@gmail.com

 Modeified on 2015-4-19
 Author: Fancy
 Email: springzfx@gmail.com
'''

import threading
from parsers import WeiboParser, InfoParser, RelationshipParser
from log import logger
import sys
sys.path.append("..")
from conf.config import data


class UserCrawler(threading.Thread):
    def __init__(self, user, callbacks=None, storage=None):
        super(UserCrawler, self).__init__()

        logger.info('fetch user: %s' % user)
        self.uid = user
        if self.uid is not None:
            self.weibo_start = 'http://weibo.cn/%s/profile' % self.uid
            self.info_start = 'http://weibo.cn/%s/info' % self.uid   
            self.follow_start = 'http://weibo.cn/%s/follow' % self.uid
            self.fan_start = 'http://weibo.cn/%s/fans' % self.uid

            self.storage = storage
            self.callbacks = callbacks

    
    def crawl_weibos(self):
        weibo = WeiboParser(self.weibo_start, self.uid, self.storage)
        weibo.parse()
        return (not weibo.error)

    def crawl_info(self):
        info = InfoParser(self.info_start, self.uid, self.storage)
        info.parse()
        return (not info.error)
            
    def crawl_follow(self):
        relation = RelationshipParser(self.follow_start, self.uid, self.storage,'follow')
        relation.parse()
        return (not relation.error)
            
    def crawl_fans(self):
        relation = RelationshipParser(self.fan_start,self.uid, self.storage,'fans')
        relation.parse()
        return (not relation.error)
            
    def crawl(self):
        flag_follow=True
        flag_info=True
        flag_weibo=True
        flag_fans=True
        if data['info']==1:
            print "start to fetch %s's info" % self.uid
            flag_info = self.crawl_info()

        if data['follows']==1:
            print "start to fetch %s's follows" % self.uid
            flag_follow = self.crawl_follow()

        if data['fans']==1:
            print "start to fetch %s's fans" % self.uid
            flag_fans = self.crawl_fans()

        if data['weibo']==1:            
            print "start to fetch %s's weibo" % self.uid
            flag_weibo = self.crawl_weibos()
        
        if flag_follow and flag_info and flag_weibo and flag_fans:
        # Add to completes when finished
            print "complete",self.uid
            self.storage.complete()
            self.callbacks()
        else:
            self.storage.error()
            self.callbacks()

    def run(self):
        assert self.storage is not None
        assert self.uid is not None

        try:
            self.crawl()
        except Exception, e:
            # raise e
            logger.info('error when crawl: %s' % self.uid)
            logger.exception(e)
        finally:
            if hasattr(self.storage, 'close'):
                self.storage.close()

