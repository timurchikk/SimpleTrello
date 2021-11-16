from django.db.models import fields
from .models import *
from rest_framework import serializers


class ColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columns
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields  = '__all__'
