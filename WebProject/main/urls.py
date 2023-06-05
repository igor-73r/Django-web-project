from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('change_table/', views.change_table)
]