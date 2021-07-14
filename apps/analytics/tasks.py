# from __future__ import absolute_import, unicode_literals
from celery.app import shared_task

from .models import (
    SimpleReport
)

#@task(name='fetch_reports_8h') 
@shared_task
def fetch_reports_8h():
    reports = SimpleReport.objects.all()
    for report in reports:
        report.save()
        print(report)