from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = (
        ('New', 'Новая'),
        ('In Progress', 'В работе'),
        ('Completed', 'Завершена'),
    )

    PRIORITY_CHOICES = (
        (1, 'Очень низкий'),
        (2, 'Низкий'),
        (3, 'Средний'),
        (4, 'Высокий'),
        (5, 'Очень высокий'),
    )

    title = models.CharField(max_length=255, verbose_name='Краткое описание бага')
    description = models.TextField(verbose_name='Полное описание бага')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Задача')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New', verbose_name='Статус бага')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3, verbose_name='Приоритет бага')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего обновления записи')

    def __str__(self):
        return self.title


from django.db import models
from tasks.models import Project, Task

class FeatureRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    )

    PRIORITY_CHOICES = (
        ('Low', 'Низкий'),
        ('Medium', 'Средний'),
        ('High', 'Высокий'),
    )

    title = models.CharField(max_length=255, verbose_name='Название запроса на новую функцию')
    description = models.TextField(verbose_name='Описание запроса')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Задача')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name='Статус запроса')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium', verbose_name='Приоритет запроса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания запроса')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего обновления запроса')

    def __str__(self):
        return self.title
