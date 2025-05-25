from django.contrib import admin
from .models import LogoSettings, GeneralSettings, ColorSettings

@admin.register(LogoSettings)
class AppConfigAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_light', 'logo_dark', 'favicon', 'invoice_logo']

@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ('application_name', 'author', 'default_menu', 'search_feature')

@admin.register(ColorSettings)
class ColorSettingsAdmin(admin.ModelAdmin):
    list_display = ('default_color_mode', 'primary_color', 'primary_hover_link_color', 'whatsapp_button_shed_color')
