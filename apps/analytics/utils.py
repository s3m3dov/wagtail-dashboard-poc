import os
import collections
from django.conf import settings
from datetime import datetime
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, 
    Dimension,
    Metric,
    RunReportRequest
)

# Importants
def set_credentials():
    """
    Sets GA credentials to the environment
    """
    #os.environ['property_id'] = settings.GA4_ID
    os.environ['property_id'] = '278053950'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "apps/analytics/credentials/quickstart.json"


# Helper Functions
def pass_rows_to_dict(data, rows):
    """
    Renders json rows to python dict
    """
    for row in rows:
        metric_value = row.metric_values[0].value
        dimension_value = row.dimension_values[0].value

        data[dimension_value] = row.metric_values[0].value


def change_sort_time_data(old_data):
    data = {}
    for key in sorted(old_data):
        value = old_data[key]
        new_key = convert_date_to_conventional(key)
        data[new_key] = value
    
    return data


def convert_date_to_conventional(old_format):
    datetimeobject = datetime.strptime(old_format,'%Y%m%d')
    new_format = datetimeobject.strftime('%d %B %Y')

    return new_format


# Argument Based Reports
def run_report(dimensionNames, metricNames, startDate, endDate="today"):
    """
    Runs reports by passed args, such as
    "dimensions", "metrics
    """
    data = {}
    property_id = os.environ['property_id']
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name=dimensionNames)],
        metrics=[Metric(name=metricNames)],
        date_ranges=[DateRange(start_date=startDate, end_date=endDate)],
    )

    response = client.run_report(request)
    pass_rows_to_dict(data, response.rows)
    if dimensionNames == "date":
        data = change_sort_time_data(data)
    return data


# Main
if __name__ == "__main__":
    set_credentials()
    print(run_report("country", "activeUsers", "7daysAgo"))
    print(run_report("pageTitle", "screenPageViews", "7daysAgo"))


"""
DimensionNames: country, city, browser, deviceCategory, pageTitle, 
date, dateHour, day, dayOfWeek, month, week, year

MetricNames: activeUsers, totalUsers, screenPageViews
DateRanges: 7daysAgo, etc. (customs)
"""