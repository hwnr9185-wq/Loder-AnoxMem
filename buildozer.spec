[app]

title = Loader
package.name = loader
package.domain = org.anooni

source.dir = .
source.include_exts = py,jpg,png

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[android]

android.api = 35
android.minapi = 21
android.archs = arm64-v8a

android.accept_sdk_license = True
