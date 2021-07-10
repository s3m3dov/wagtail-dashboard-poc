from django.contrib import admin

from .models import (
    SimpleReport
)

@admin.register(SimpleReport)
class SimpleReportAdmin(admin.ModelAdmin):
    def report_date(self, obj):
        return obj.report_created.strftime("%d %b %Y")
        
    report_date.admin_order_field = 'timefield'
    report_date.short_description = 'Report Created'

    list_display = ('__str__', 'report_date', )