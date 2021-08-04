import json
import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .utils import (
    set_credentials,
    run_report,
)


class SimpleReport(models.Model):
    COUNTRY = 'country'
    CITY = 'city'
    BROWSER = 'browser'
    DEVICE_CATEGORY = 'deviceCategory'
    PAGE_TITLE = 'pageTitle'

    DATE = 'date'
    DATE_HOUR = 'dateHour'
    DAY = 'day'
    DAY_OF_WEEK = 'dayOfWeek'
    MONTH = 'month'
    WEEK ='week'
    YEAR = 'year'

    """
    NTH_MONTH = 'nthMonth'
    """

    DIMENSION_CHOICES = [
        (COUNTRY, 'Country'),
        (CITY, 'City'),
        (BROWSER, 'Browser'),
        (DEVICE_CATEGORY, 'Device Category'),
        (PAGE_TITLE, 'Page Title'),

        (DATE, 'Date'),
        (DATE_HOUR, 'Date & Hour'),
        (DAY, 'Day of the Month'),
        (DAY_OF_WEEK, 'Day of the Week'),
        (MONTH, 'Month'),
        (WEEK, 'Week'),
        (YEAR, 'Year'),
    ]

    dimensions = models.CharField(
        max_length=100,
        choices=DIMENSION_CHOICES,
        default=COUNTRY
    )


    ACTIVE_USERS = 'activeUsers'
    TOTAL_USERS = 'totalUsers'
    NEW_USERS = 'newUsers'
    SCREEN_PAGE_VIEWS = 'screenPageViews'

    METRIC_CHOICES = [
        (ACTIVE_USERS, 'Active Users'),
        (TOTAL_USERS, 'Total Users'),
        (NEW_USERS, 'New Users'),
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

    SEVEN_DAYS_AGO = "7 Days Ago"
    ONE_MONTH_AGO = "1 Month Ago"
    THREE_MONTHS_AGO = "3 Months Ago"
    SIX_MONTHS_AGO = "6 Months Ago"
    TWELWE_MONTHS_AGO = "12 Months Ago"

    DATE_RANGE_CHOICES = [
        (SEVEN_DAYS_AGO, '7 Days Ago'),
        (ONE_MONTH_AGO, '1 Month Ago'),
        (THREE_MONTHS_AGO, '3 Months Ago'),
        (SIX_MONTHS_AGO, '6 Months Ago'),
        (TWELWE_MONTHS_AGO, '12 Months Ago'),
    ]

    date_range = models.CharField(
        max_length=100,
        choices=DATE_RANGE_CHOICES,
        default=SEVEN_DAYS_AGO
    )
    

    data = models.JSONField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)


    def save(self, *args, **kwargs):
        set_credentials() # set credentials for GA
        func_start_date = self.update_date_range() # add custom start date
        self.data = json.dumps(run_report(self.dimensions, self.metrics, func_start_date)) # get GA DATA and save
        self.slug = '-'.join((slugify(self.dimensions), 'by', slugify(self.metrics), slugify(self.chart_type))) # slug
        return super().save(*args, *kwargs) # save


    def update_date_range(self):
        """ 
        Adds start_date based on today's date and selected interval
        """
        today = datetime.date.today()
        date_vals = self.date_range.split()
        month_num = int(date_vals[0])
        is_month = date_vals[1].lower().startswith("month")

        if is_month:
            return (today - datetime.timedelta(month_num * 365 / 12)).isoformat()
        else:
            return "7daysAgo"

    def get_json_url(self):
        return reverse('dashboard:simple_report_json', kwargs={'slug':self.slug})

    def get_html_url(self):
        return reverse('dashboard:simple_report_html', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.dimensions} by {self.metrics}'