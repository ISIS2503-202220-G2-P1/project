from django.urls import path
from . import views

urlpatterns = [
    path('', views.solicitud_view , name='solicitud_view'),
]