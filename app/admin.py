from django.contrib import admin
from django.db import models
# Register your models here.
from .models import HojaCargo, InformePCR

# Register the admin class with the associated model
@admin.register(InformePCR)
class InformePCRAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fechais']
    search_fields = ['nombre']
    pass

admin.site.register(HojaCargo)