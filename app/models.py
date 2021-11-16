from django.db import models
from django.db.models.base import Model


#----------Колонки----------#
class Columns(models.Model):
    title = models.CharField(
        verbose_name = 'Колонки',
        max_length = 25
    )

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'

    def __str__ (self):
        return self.title


#----------Задачи----------#
class Tasks(models.Model):
    column = models.ForeignKey(
        Columns,
        verbose_name = 'Задача',
        on_delete = models.CASCADE
    )
    title = models.CharField(
        verbose_name = 'Заголовок',
        max_length=25
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
    
    def __str__ (self):
        return self.title