# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['comm_collect.py'],
    pathex=[],
    binaries=[],
    datas=[("c:/Users/geg82/AppData/Local/Programs/Python/Python311/Lib/site-packages/konlpy/", "./konlpy"), ("c:/Users/geg82/AppData/Local/Programs/Python/Python311/Lib/site-packages/konlpy/java/", "./konlpy/java"), ("c:/Users/geg82/AppData/Local/Programs/Python/Python311/Lib/site-packages/konlpy/data/tagset/*", "./konlpy/data/tagset"),],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='comm_collect',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
