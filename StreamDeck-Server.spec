# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/Coding/Python/StreamDeck/StreamDeck-Server/server.py'],
             pathex=['D:\\Coding\\Python\\StreamDeck'],
             binaries=[],
             datas=[('D:/Coding/Python/StreamDeck/StreamDeck-Server/routes', 'routes/'), ('D:/Coding/Python/StreamDeck/StreamDeck-Server/systray', 'systray/'), ('D:/Coding/Python/StreamDeck/StreamDeck-Server/systray/tray.py', '.'), ('D:/Coding/Python/StreamDeck/StreamDeck-Server/routes/discord.py', '.'), ('D:/Coding/Python/StreamDeck/StreamDeck-Server/routes/photoshop.py', '.'), ('D:/Coding/Python/StreamDeck/StreamDeck-Server/routes/start.py', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='StreamDeck-Server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , version='D:\\Coding\\Python\\StreamDeck\\StreamDeck-Server\\compile\\VERSIONFILE.txt', icon='D:\\Coding\\Python\\StreamDeck\\Project\\ICON.ico')
