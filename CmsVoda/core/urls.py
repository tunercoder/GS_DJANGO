from django.urls import path, register_converter
from core.converters import DateConverter
from . import views

register_converter(DateConverter, 'date')

urlpatterns = [
    path('core/<int:msisdn>/<date:startdate>/<date:enddate>/', views.home,name='home'),
]
