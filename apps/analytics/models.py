import json
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .utils import (
    set_credentials,
    run_report,
)

class SimpleReport(models.Model):
    COUNTRY = 'country'
    PAGE_TITLE = 'pageTitle'
    DEVICE_CATEGORY = 'deviceCategory'

    DIMENSION_CHOICES = [
        (COUNTRY, 'Country'),
        (PAGE_TITLE, 'Page Title'),
        (DEVICE_CATEGORY, 'Device Category'),
    ]

    dimensions = models.CharField(
        max_length=100,
        choices=DIMENSION_CHOICES,
        default=COUNTRY
    )


    ACTIVE_USERS = 'activeUsers'
    SCREEN_PAGE_VIEWS = 'screenPageViews'

    METRIC_CHOICES = [
        (ACTIVE_USERS, 'Active Users'),
        (SCREEN_PAGE_VIEWS, 'Scree Page Views'),
    ]

    metrics = models.CharField(
        max_length=100,
        choices=METRIC_CHOICES,
        default=ACTIVE_USERS
    )


    BAR_CHART = 'bar'
    PIE_CHART = 'pie'
    DOUGHNUT_CHART = 'doughnut'
    LINE_CHART = 'line'

    CHART_TYPE_CHOICES = [
        (BAR_CHART, 'Bar Chart'),
        (PIE_CHART, 'Pie Chart'),
        (DOUGHNUT_CHART, 'Doughnut Chart'),
        (LINE_CHART, 'Line Chart'),
    ]

    chart_type = models.CharField(
        max_length=100,
        choices=CHART_TYPE_CHOICES,
        default=BAR_CHART
    )
    

    data = models.JSONField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)


    def save(self, *args, **kwargs):
        set_credentials()
        self.data = json.dumps(run_report(self.dimensions, self.metrics))
        self.slug = '-'.join((slugify(self.dimensions), 'by', slugify(self.metrics), slugify(self.chart_type)))
        return super().save(*args, *kwargs)


    def get_json_url(self):
        return reverse('dashboard:simple_report_json', kwargs={'slug':self.slug})

    def get_html_url(self):
        return reverse('dashboard:simple_report_html', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.dimensions.title()} by {self.metrics.title()}'