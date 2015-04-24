Sina Weibo Crawler

The program is based on yaml/pymongo/chardet, which is python library .
Environment: Python 2.7.5

Notes:

1. The crawler could crawl weibo/follows/fans/info/personal domain. You can decide which to be downloaded, through configure conf.yaml

2. Enter the conf folder and open conf.yaml, sign in your username password,you can add multiple accounts. 

3. You can choose the form of storage file or mongodb, if you choose the file storage you should write the position in conf.yaml.

4. I suggest you choose mongodb for storage, because it is more perfect. And file storage is also OK, but without exist(already crawled) detection.

5. If you use file for storage, you need enter a path(exactly 'mypath' in conf.yaml) to store you output. 

6. A 'list.txt' file is defaultly put in 'mypath', which indicates those users you want to crawl. Each user_id per line.

7. Then just run command "python main.py" in shell.

8. I also offer an executale file built in windowsX64, under the exe folder.

others:

conf/conf.yaml ----- configure file

conf/savecookie.txt  ------ cookies

crawler/crawler.log  ------ log for exception

setup.spec ----- for pyinstaller(a python module) to bulid an exe, see setup.txt
