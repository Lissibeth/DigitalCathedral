from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import BugReport, FeatureRequest

def index(request):
    BugReport_list_url = reverse('quality_control:bugreports_list')
    FeatureRequest_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Страница приложения Quality Control</h1><a href='{BugReport_list_url}'>Список всех багов</a>"
    return HttpResponse(html)

def bugreports_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:  # вместо for bugs in bugs
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return HttpResponse(f"<h1>{bug.status}</h1><p>{bug.description}</p>")

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return HttpResponse(f"<h1>{feature.status}</h1><p>{feature.description}</p>")
