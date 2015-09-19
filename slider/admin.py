import os
from django.contrib import admin
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    actions=['really_delete_selected']

    def get_actions(self, request):
        actions = super(SliderAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            os.remove(obj.image.path)
        queryset.delete()

    really_delete_selected.short_description = "Delete selected slide"

admin.site.register(Slider, SliderAdmin)