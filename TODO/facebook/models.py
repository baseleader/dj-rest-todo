from django.db import models
from users.models import User


class Facebook(models.Model):
    name_project = models.CharField(max_length=30, verbose_name='Название проекта', unique=True)
    repo_url = models.URLField(verbose_name='Ссылка на репозиторий проекта')
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name_project


class ToDo(models.Model):
    annotation = models.CharField(max_length=50, verbose_name='Заметка')
    project = models.ForeignKey(Facebook, related_name='project', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активная', default=True)
