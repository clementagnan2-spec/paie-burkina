[app]
title = Paie Burkina
package.name = paieburkina
package.domain = org.paieburkina
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,kivymd==1.1.1,openpyxl==3.1.2,pillow
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = arm64-v8a
android.allow_backup = True
android.logcat_filters = *:S python:D
# Android packaging options
android.add_aars = 
android.gradle_dependencies = 
android.p4a_dir = 
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = "@android:style/Theme.NoTitleBar"
# iOS packaging options
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
[buildozer]
log_level = 2
warn_on_root = 1
