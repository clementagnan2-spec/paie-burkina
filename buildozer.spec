[app]
title = Paie Burkina
package.name = paieburkina
package.domain = org.paieburkina
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,kivymd,openpyxl,pillow
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
[buildozer]
log_level = 2
warn_on_root = 1
