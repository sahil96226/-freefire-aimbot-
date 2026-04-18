[app]
title = Free Fire Aimbot Controller
package.name = freefireaimbot
package.domain = com.github.ffaimbot

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,svg

version = 2.0
requirements = python3,kivy==2.1.0,pillow,numpy,opencv-python

android.permissions = SYSTEM_ALERT_WINDOW,WRITE_EXTERNAL_STORAGE,CAMERA

android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

android.enable_androidx = True
android.gradle_dependencies = 

[buildozer]
log_level = 2