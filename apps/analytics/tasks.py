#from __future__ import absolute_import, unicode_literals
from celery.app import shared_task

from .models import (
    SimpleReport
)

@shared_task
def fetch_reports_15m():
    objects = []
    reports = SimpleReport.objects.all()

    for report in reports:
        report.save()
        objects.append(report.report_type)

    return objects