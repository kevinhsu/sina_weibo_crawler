Sina Weibo Crawler

The program is based on yaml/pymongo, which is python library .
Environment: Python 2.7.5 [GCC 4.8.1] on linux (Ubuntu 12.04)

Notes:

1. The crawler now could crawling weibo/follows/fans/info/personal domain. (unknown)

2. Enter the conf folder and open conf.yaml, sign in your username password,you can add multiple accounts. Then you should write in the startuid. (unknown)

3. You can choose the form of storage file or mongodb, if you choose the file storage you should write the position in conf.yaml then just run command "python main.py" in shell. (unknown)

4.I suggest you choose mongodb for storage, because it is more perfect. And file storage may occur some problem. (2014/12/2)

5.If SinaWeibo change their cookie,the cookies file used here(savecookie.txt and row 30 in crawler/parsers.py) need to be changed too. You can extract cookie by yourself if necessary.  (2014/12/2)

6.Further,I will make it a breadth first crawler.  (2014/12/2)


Enjoy~ :-)

