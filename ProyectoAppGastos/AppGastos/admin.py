from django.contrib import admin
from .models import movimientos, usuario,objetivo 

# Register your models here.

admin.site.register(objetivo)

admin.site.register(movimientos)

admin.site.register(usuario)