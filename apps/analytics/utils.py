import os
from django.conf import settings
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
        if (row.metric_values[0].value).isdigit():
            data[row.dimension_values[0].value] = int(row.metric_values[0].value)
        else:
            data[row.dimension_values[0].value] = row.metric_values[0].value


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
    return data


# Main
if __name__ == "__main__":
    set_credentials()
    print(run_report("country", "activeUsers", "7daysAgo"))
    print(run_report("pageTitle", "screenPageViews", "7daysAgo"))


"""
DimensionNames: country, deviceCategory, pageTitle
MetricNames: activeUsers, screenPageViews
DateRanges: 7daysAgo, etc. (customs)
"""