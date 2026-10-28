---
name: desktop-application-packaging-and-shortcuts
description: >-
  Package Python applications (CustomTkinter, PyQt, Electron, or Flask/WebView) into standalone Windows executables with PyInstaller, embed custom assets/icons, generate silent VBS launchers, and automate desktop shortcut creation. Use when shipping desktop software to end users.
---

# Desktop Application Packaging, Silent Launchers & Windows Shortcuts

## Overview
Derived from both the Tharun ScholasticPulse and Gann Ephemeris desktop deployments, this skill provides a complete recipe for compiling Python applications into standalone, single-executable Windows binaries with high-DPI desktop shortcuts and silent launching.

---

## 1. PyInstaller Build Script Pattern
Avoid fragile command-line invocations by using a dedicated `.spec` file or automated Python build script:

```python
import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'main.py',
    '--name=MyDesktopApp',
    '--noconsole',
    '--onefile',
    '--icon=assets/app_icon.ico',
    '--add-data=assets;assets',
    '--clean'
])
```

---

## 2. Silent VBS Launcher Pattern (`LAUNCH_SILENT.vbs`)
When launching a Python background server or non-console script without displaying an unwanted black Command Prompt window:

```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "pythonw.exe main.py", 0, False
Set WshShell = Nothing
```

---

## 3. Automated Windows Desktop Shortcut Script (PowerShell)
Provide an automated shortcut creator (`CREATE_DESKTOP_SHORTCUT.ps1`):

```powershell
$WshShell = New-Object -ComObject WScript.Shell
$DesktopPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop)
$ShortcutPath = Join-Path -Path $DesktopPath -ChildPath "My Desktop App.lnk"
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = "$PSScriptRoot\dist\MyDesktopApp.exe"
$Shortcut.WorkingDirectory = "$PSScriptRoot"
$Shortcut.IconLocation = "$PSScriptRoot\assets\app_icon.ico"
$Shortcut.Description = "Launch My Desktop Application"
$Shortcut.Save()
Write-Host "Desktop shortcut created successfully at: $ShortcutPath"
```
