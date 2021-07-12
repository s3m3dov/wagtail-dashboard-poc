from django.urls import path
from .views import (
    dashboard_view,
    simple_report_html,
    simple_report_json,
    example,
)

urlpatterns = [
    path('', dashboard_view, name='home'),

    path('simple-report/<slug:slug>/', simple_report_html, name='simple_report_html'),
    path('simple-report-JSON/<slug:slug>/', simple_report_json, name='simple_report_json'),
    path('example/', example, name='example'),
]
