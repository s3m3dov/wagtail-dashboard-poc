import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, 
    Dimension,
    Metric,
    RunReportRequest
)

# Credentials
property_id = "278053950"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "apps/analytics/credentials/quickstart.json"


# Functions
def simple_report(property_id=property_id):
    data = {}
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


def pass_rows_to_dict(data, rows):
    for row in rows:
        if (row.metric_values[0].value).isdigit():
            data[row.dimension_values[0].value] = int(row.metric_values[0].value)
        else:
            data[row.dimension_values[0].value] = row.metric_values[0].value


if __name__ == "__main__":
    print(simple_report())
