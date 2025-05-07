[app]

# Configuración básica
title = HolaMundo
package.name = holamundo
package.domain = com.midominio
source.dir = .
source.include_exts = py,png,jpg,kv,ttf,otf
version = 1.0

# Configuración principal
requirements = python3==3.8.5,kivy==2.0.0  # Versiones específicas
orientation = portrait
fullscreen = 0

# Entrada principal
main.py = main.py

# Icono (debe ser PNG y preferiblemente 512x512px)
icon.filename = icon.png

# Configuración Android
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 34
android.arch = armeabi-v7a


# Opciones de compilación
p4a.branch = master