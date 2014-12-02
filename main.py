#!/usr/bin/env python
#coding=utf-8
'''
 Created on 2014-7-10
 Author: Gavin_Han
 Email: muyaohan@gmail.com
'''
import time, datetime
from crawler.crawler import UserCrawler
from crawler.storage import MongoStorage, FileStorage
from crawler.login import WeiboLogin
from conf.config import login_list, startUid, mypath
from crawler.log import logger
            
mythreads = range(5) #id线程池

def callback(threadId):
    def inner():
        if threadId not in mythreads:
            mythreads.append(threadId)
    return inner

def main(db='file', folder=None, uids=[]):
    change = 1; i = 0; 
    username = login_list[i]['username']
    password = login_list[i]['password']
    WBLogin = WeiboLogin(username, password)
    WBLogin.login()
    end = datetime.datetime.now()
    i += 1
    if len(uids) == 0:
        print 'startUid is null.'
    else:
        while uids:
            begin = datetime.datetime.now()
            interval = (begin-end).seconds
            while mythreads and uids:
                end = datetime.datetime.now()
                #如果有三次爬取用户的间隔时间都超过了10秒，那么就换下一个用户登录，防止反爬虫或掉线
                if interval > 10:
                    if change >= 3:
                        change = 1
                        if i <= len(login_list)-1:
                            time.sleep(20)
                            username = login_list[i]['username']
                            password = login_list[i]['password']
                            WBLogin = WeiboLogin(username, password)
                            WBLogin.login()
                            i += 1
                        else:
                            i = 0
                            username = login_list[i]['username']
                            password = login_list[i]['password']
                            WBLogin = WeiboLogin(username, password)
                            WBLogin.login()
                    change += 1

                uid = uids.pop() #分配一个uid
                threadId = mythreads.pop() #分配一个线程id
                cb = callback(threadId)  #当该线程结束后调用cb，将线程id返回线程池

                try:
                    if db == 'file' and folder is not None:
                        storage = FileStorage(uid, folder)
                    elif db == 'mongo':
                        storage = MongoStorage(uid)
                    else:
                        raise ValueError('db must be "file" or "mongo", ' + 
                                         'when is "file", you must define folder parameter.')
                    crawler = UserCrawler(uid, callbacks=cb, storage=storage)
                    
                    #crawler.start()
                    
                    if not storage.completes.find_one({'uid': uid}):
                        crawler.start()
                    else:
                        cb()
                        continue
                except Exception, e:
                    logger.exception(e)

                    

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    db = 'mongo'
    folder = mypath
    uids = startUid
    main(db=db, folder=folder, uids=uids)
    