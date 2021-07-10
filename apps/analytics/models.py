import json
from django.db import models

from .utils import (
    set_credentials,
    simple_report
)

class SimpleReport(models.Model):
    report_name = models.CharField(max_length=100, null=True, blank=True)
    report_data = models.JSONField(null=True, blank=True)
    report_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        set_credentials()
        self.report_data = json.dumps(simple_report())
        return super().save(*args, *kwargs)

    def __str__(self):
        return self.report_name
