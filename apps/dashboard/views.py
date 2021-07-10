import json
from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render

from apps.analytics.models import SimpleReport



def simpleReport_JSONView(request):
    labels = []
    data = []

    report_data = json.loads(getattr(SimpleReport.objects.latest('report_created'), 'report_data'))
    countries = list(report_data.keys())
    counts = list(report_data.values())

    for i in range(len(countries)):
        labels.append(countries[i])
        data.append(counts[i])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

simple_report_html = TemplateView.as_view(template_name='simple_report.html')
simple_report_json = simpleReport_JSONView



def example(request):
    return render(request, 'example.html')