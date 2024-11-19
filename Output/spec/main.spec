# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['G:\\Works\\Application\\Motivation-App\\Source Code\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('G:\\Works\\Application\\Motivation-App\\Source Code\\backend', 'backend'), ('G:\\Works\\Application\\Motivation-App\\Source Code\\Images', 'Images'), ('G:\\Works\\Application\\Motivation-App\\Source Code\\GUI', 'GUI')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['G:\\Works\\Application\\Motivation-App\\Source Code\\Images\\Icon.ico'],
)
