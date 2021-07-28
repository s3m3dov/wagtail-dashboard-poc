
# Hard-coded reports
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
        date_ranges=[DateRange(start_date="7monthsAgo", end_date="today")],
    )
    
    response = client.run_report(request)
    pass_rows_to_dict(data, response.rows)
    return data


def device_category():
    """
    Returns statistics of device categories
    (Mobile, Tablet, Desktop) for 28 days.
    """
    data = {}
    property_id = os.environ['property_id']
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="deviceCategory")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    
    response = client.run_report(request)
    pass_rows_to_dict(data, response.rows)
    return data
 
