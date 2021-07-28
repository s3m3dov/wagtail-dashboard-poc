from django.contrib import admin

from .models import (
    SimpleReport
)

@admin.register(SimpleReport)
class SimpleReportAdmin(admin.ModelAdmin):
    def report_created(self, obj):
        return obj.created.strftime("%d %b %Y")
    
    def report_updated(self, obj):
        return obj.updated.strftime("%d %b %Y, %H:%M")

    def report_chart_type(self, obj):
        return obj.chart_type.title()

    def report_dimensions(self, obj):
        return obj.dimensions.title()
    
    def report_metrics(self, obj):
        return obj.metrics.title()


    report_chart_type.short_description = 'Chart Type'
    report_chart_type.admin_order_field = 'chart_type'

    report_dimensions.short_description = 'Dimensions'
    report_dimensions.admin_order_field = 'dimensions'

    report_metrics.short_description = 'Metrics'
    report_metrics.admin_order_field = 'metrics'

    report_updated.short_description = 'Last Updated [GMT 0]'
    report_updated.admin_order_field = 'updated'
        
    report_created.short_description = 'Report Created'

    list_display = ('__str__', 'report_dimensions', 'report_metrics',  'report_chart_type', 'report_updated', 'report_created')