from django.contrib import admin
from .models import ServiceType, Service


class ServiceInLine(admin.TabularInline):
    model = Service
    extra = 3

class ServiceTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'comment']}),
    ]
    inlines = [ServiceInLine]


admin.site.register(ServiceType, ServiceTypeAdmin)