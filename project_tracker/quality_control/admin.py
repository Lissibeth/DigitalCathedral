from django.contrib import admin
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task

class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Project Info', {
            'fields': ('project', 'task', 'status', 'priority'),
            'classes': ('collapse',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    autocomplete_fields = ['project', 'task']  # Добавляем автозаполнение для полей project и task


class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Project Info', {
            'fields': ('project', 'task', 'status', 'priority'),
            'classes': ('collapse',)
        }),
        ('Dates', {
            'fields': (),
            'classes': ('collapse',)
        }),
    )

admin.site.register(BugReport, BugReportAdmin)
admin.site.register(FeatureRequest, FeatureRequestAdmin)


