from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import BugReport, FeatureRequest
from .forms import BugReportForm 
from .forms import FeatureRequestForm

def index(request):
    bug_report_form_url = reverse('quality_control:bug_report_create')
    feature_request_form_url = reverse('quality_control:feature_request_create')
    return render(request, 'quality_control/index.html', {'bug_report_form_url': bug_report_form_url, 'feature_request_form_url': feature_request_form_url})
    #return render(request, 'quality_control/index.html')
    #BugReport_list_url = reverse('quality_control:bugreports_list')
    #FeatureRequest_list_url = reverse('quality_control:feature_list')
    #html = f"<h1>Страница приложения Quality Control</h1><a href='{BugReport_list_url}'>Список всех багов</a>"
    #return HttpResponse(html)

def bugreports_list(request):
    bugs = BugReport.objects.all()
   # bugs_html = '<h1>Список багов</h1><ul>'
   # for bug in bugs:  # вместо for bugs in bugs
    #    bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
   # bugs_html += '</ul>'
    return render(request, 'quality_control/bugreports_list.html', {'bugs': bugs})
    #return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
  #  features_html = '<h1>Список запросов на улучшение</h1><ul>'
  #  for feature in features:
   #     features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
   # features_html += '</ul>'
   # return HttpResponse(features_html)
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': features})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    #return HttpResponse(f"<h1>{bug.status}</h1><p>{bug.description}</p>")
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    #return HttpResponse(f"<h1>{feature.status}</h1><p>{feature.description}</p>")
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:index')  
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def feature_request_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:index')  
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def bug_report_update(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:index')  # Перенаправление на главную страницу после успешного обновления
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def bug_report_delete(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    if request.method == 'POST':
        bug.delete()
        return redirect('quality_control:index')  # Перенаправление на главную страницу после успешного удаления
    return render(request, 'quality_control/bug_report_confirm_delete.html', {'bug': bug})

def feature_request_update(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:index')  # Перенаправление на главную страницу после успешного обновления
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def feature_request_delete(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    if request.method == 'POST':
        feature.delete()
        return redirect('quality_control:index')  # Перенаправление на главную страницу после успешного удаления
    return render(request, 'quality_control/feature_request_confirm_delete.html', {'feature': feature})

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm

class BugReportListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugreports_list.html'
    context_object_name = 'bugs'

class BugReportDetailView(DetailView):
    model = BugReport
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:index')

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:index')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("bug_id")
        return get_object_or_404(BugReport, id=id_)

class BugReportDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bug_report_confirm_delete.html'
    success_url = reverse_lazy('quality_control:index')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("bug_id")
        return get_object_or_404(BugReport, id=id_)

    def post(self, request, *args, **kwargs):
        id_ = self.kwargs.get("bug_id")
        bug = get_object_or_404(BugReport, id=id_)
        bug.delete()
        return redirect(self.success_url)

class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'
    context_object_name = 'features'

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:index')

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:index')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("feature_id")
        return get_object_or_404(FeatureRequest, id=id_)

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    template_name = 'quality_control/feature_request_confirm_delete.html'
    success_url = reverse_lazy('quality_control:index')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("feature_id")
        return get_object_or_404(FeatureRequest, id=id_)

    def post(self, request, *args, **kwargs):
        id_ = self.kwargs.get("feature_id")
        feature = get_object_or_404(FeatureRequest, id=id_)
        feature.delete()
        return redirect(self.success_url)
