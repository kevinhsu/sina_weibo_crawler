# -*- mode: python -*-
a = Analysis(['main.py'],
             pathex=['C:\\Program\\Anaconda\\Scripts\\sina_weibo_crawler'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SinaCrawler.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='a.ico')
coll = COLLECT(exe,
               [('conf.yaml', 'conf/conf.yaml', 'DATA'),('savecookie.txt','conf/savecookie.txt','DATA'),('crawler.log', 'crawler/crawler.log', 'DATA'),('parselist.py','tool/parselist.py','DATA')],
               strip=None,
               upx=True,
               name='dist')
