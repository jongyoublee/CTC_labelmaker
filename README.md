# CTC_labelmaker

Python 3.9.13
Pyqt5, Pyinstaller

1. Label maker for Clinical Trial Center
2. Input Clinical Trial information from Protocol
3. It will makes PK Label and Box Label

# How to Build
pyinstaller -w --onefile main.py

add "ui = [('MainWindow.ui', '.')]" to main.spec and change datas from main.spec

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=ui,
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

pyinstaller main.spec
