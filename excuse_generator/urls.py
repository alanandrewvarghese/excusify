from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('custom/excuse', views.custom_excuse, name='custom_excuse'),
]