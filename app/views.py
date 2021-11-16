from django.shortcuts import render, get_object_or_404

from rest_framework import generics

from .models import *
from .serializers import *


#---------------Создание колонки---------------#
class ColumnsCreateView(generics.CreateAPIView):
    serializer_class = ColumnsSerializer


#---------------Показ колонки---------------#
class ColumnsListView(generics.ListAPIView):
    serializer_class = ColumnsSerializer
    queryset = Columns.objects.all()


#---------------Изменение колонки---------------#
class ColumnsUpdateView(generics.UpdateAPIView):
    serializer_class = ColumnsSerializer
    queryset = Columns.objects.all()


#---------------Удаление колонки---------------#
class ColumnsDeleteView(generics.DestroyAPIView):
    serializer_class = ColumnsSerializer
    queryset = Columns.objects.all()


#---------------Создание задачи---------------#
class TasksCreateView(generics.CreateAPIView):
    serializer_class = TasksSerializer


#---------------Показ задачи---------------#
class TasksListView(generics.ListAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()


#---------------Изменение задачи---------------#
class TasksUpdateView(generics.UpdateAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()


#---------------Удаление задачи---------------#
class TasksDeleteView(generics.DestroyAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
