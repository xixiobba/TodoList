# todos/urls.py
from django.urls import path

from . import views
# specifying which model to use and the specific fields on it we want to expose.
urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
]