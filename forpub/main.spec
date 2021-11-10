# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py','F:\\db2moxing\\modelCase\\forExcel.py','F:\\db2moxing\\modelCase\\ibm_db_dbi.py'],
             pathex=['\\modelCase\\checkCallProNewBiaoZhun.py', '\\modelCase\\conDb2.py', '\\modelCase\\forExcel.py', '\\modelCase\\forFinal.py', '\\modelCase\\ibm_db_dbi.py', 'F:\\db2moxing'],
             binaries=[('C:\\Program Files\\Python36\\Lib\\site-packages\\ibm_db_dlls\\ibm_db.dll', '.\\ibm_db_dlls')],
             datas=[('c:\\program files\\python36\\lib\\site-packages\\clidriver', '.\\clidriver')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
