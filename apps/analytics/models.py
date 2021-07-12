import json
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .utils import (
    set_credentials,
    users_by_country,
    page_views,
)

class SimpleReport(models.Model):
    USERS_BY_COUNTRY = 'Users by Country'
    PAGE_VIEWS = 'Page Views by Title'
    REPORT_TYPE_CHOICES = [
        (USERS_BY_COUNTRY, 'Users by Country'),
        (PAGE_VIEWS, 'Page Views by Title'),
    ]

    report_type = models.CharField(
        max_length=100,
        choices=REPORT_TYPE_CHOICES,
        default=USERS_BY_COUNTRY
    )
    report_data = models.JSONField(null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    report_created = models.DateTimeField(auto_now_add=True)
    report_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        set_credentials()
        self.make_particular_report()
        self.slug = slugify(self.report_type)
        return super().save(*args, *kwargs)

    def make_particular_report(self):
        """
        Determines report type, calls and saves data 
        to the 'report_data' based on 'report_type'
        """
        if self.report_type == self.USERS_BY_COUNTRY:
            self.report_data = json.dumps(users_by_country())
        elif self.report_type == self.PAGE_VIEWS:
            self.report_data = json.dumps(page_views())


    def get_json_url(self):
        return reverse('dashboard:simple_report_json', kwargs={'slug':self.slug})

    def get_html_url(self):
        return reverse('dashboard:simple_report_html', kwargs={'slug':self.slug})

    def __str__(self):
        return self.report_type