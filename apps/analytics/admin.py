from django.contrib import admin

from .models import (
    SimpleReport
)

@admin.register(SimpleReport)
class SimpleReportAdmin(admin.ModelAdmin):
    def report_create(self, obj):
        return obj.report_created.strftime("%d %b %Y")
    
    def report_update(self, obj):
        return obj.report_updated.strftime("%d %b %Y, %H:%M")
        
    report_create.short_description = 'Report Created'
    report_update.short_description = 'Last Updated [GMT 0]'
    report_update.admin_order_field = 'report_updated'


    list_display = ('__str__', 'report_update', 'report_create')