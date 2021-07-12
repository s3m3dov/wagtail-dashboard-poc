import json
from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render

from apps.analytics.models import SimpleReport



def dashboard_view(request):
    simple_reports = SimpleReport.objects.all()
    context = {
        'simple_reports' : simple_reports,
    }
    return render(request, 'dashboard.html', context)


def simple_report_json(request, slug=None):
    simple_report = get_object_or_404(SimpleReport, slug=slug)
    report_data = json.loads(simple_report.report_data)

    labels = list(report_data.keys())
    data = list(report_data.values())

    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'report_type': simple_report.report_type,
    })


def simple_report_html(request, slug=None):
    simple_report = get_object_or_404(SimpleReport, slug=slug)
    context = {
        'simple_report' : simple_report
    }
    return render(request, 'simple_report.html', context)


def example(request):
    return render(request, 'example.html')