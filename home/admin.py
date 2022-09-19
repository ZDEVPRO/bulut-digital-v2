from django.contrib import admin
from home.models import Logo, Contact


class SiteLogo(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'favicon_tag']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'ip']
    readonly_fields = ['full_name', 'phone', 'message', 'ip']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Logo, SiteLogo)
