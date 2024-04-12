from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugreports/', views.bugreports_list, name='bugreports_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bug/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('feature/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('bug/create/', views.bug_report_create, name='bug_report_create'),
    path('feature/create/', views.feature_request_create, name='feature_request_create'),
    path('bug/<int:bug_id>/update/', views.bug_report_update, name='bug_report_update'),
    path('bug/<int:bug_id>/delete/', views.bug_report_delete, name='bug_report_delete'),
    path('feature/<int:feature_id>/update/', views.feature_request_update, name='feature_request_update'),
    path('feature/<int:feature_id>/delete/', views.feature_request_delete, name='feature_request_delete'),
]
