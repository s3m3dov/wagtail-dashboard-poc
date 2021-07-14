#from __future__ import absolute_import, unicode_literals
from django.shortcuts import get_object_or_404
from celery.app import shared_task

from .models import (
    SimpleReport
)

#@task(name='fetch_reports_8h') 
@shared_task
def fetch_reports_8h():
    objects = []
    reports = SimpleReport.objects.all()

    for report in reports:
        report.save()
        objects.append(report.report_data)

    return objects

"""
@shared_task
def fetch_reports_8h():
    report = get_object_or_404(SimpleReport, report_type='Users by Country')
    report.save()
    #report.save(update_fields=['report_data'])
    return report.report_data
"""