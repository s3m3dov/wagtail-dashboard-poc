import os
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
    os.environ['property_id'] = "278053950"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "apps/analytics/credentials/quickstart.json"


# Functions
def pass_rows_to_dict(data, rows):
    """
    Renders json rows to python dict
    """
    for row in rows:
        if (row.metric_values[0].value).isdigit():
            data[row.dimension_values[0].value] = int(row.metric_values[0].value)
        else:
            data[row.dimension_values[0].value] = row.metric_values[0].value


# Report Types
def users_by_country():
    """
    Returns user counts by their country origin as a dict 
    by help of 'pass_rows_to_dict
    Weekly'
    """
    data = {}
    property_id = os.environ['property_id']
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    
    response = client.run_report(request)
    pass_rows_to_dict(data, response.rows)
    return data


def page_views():
    """
    Returns statistics of visited pages
    """
    data = {}
    property_id = os.environ['property_id']
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pageTitle")],
        metrics=[Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    
    response = client.run_report(request)
    pass_rows_to_dict(data, response.rows)
    return data




if __name__ == "__main__":
    set_credentials()
    print(page_views())