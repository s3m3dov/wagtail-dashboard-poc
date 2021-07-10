from django.urls import path
from .views import (
    example,
    simple_report_html,
    simple_report_json
)

urlpatterns = [
    path('example', example, name='example'),
    path('simple-report', simple_report_html, name='simple_report_html'),
    path('simple-report-JSON', simple_report_json, name='simple_report_json'),
]
