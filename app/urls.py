from django.urls import path
from .views import *


urlpatterns = [
    path('create_column/', ColumnsCreateView.as_view()),
    path('list_column/', ColumnsListView.as_view()),
    path('update_column/<int:pk>/', ColumnsUpdateView.as_view()),
    path('delete_column/<int:pk>/', ColumnsDeleteView.as_view()),
    path('create_task/', TasksCreateView.as_view()),
    path('list_task/', TasksListView.as_view()),
    path('update_task/<int:pk>/', TasksUpdateView.as_view()),
    path('delete_task/<int:pk>/', TasksDeleteView.as_view()),
]