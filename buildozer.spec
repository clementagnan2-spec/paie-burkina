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
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.logcat_filters = *:S python:D
p4a.source_dir =
[buildozer]
log_level = 2
warn_on_root = 1
