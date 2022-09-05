from django.urls import path
from . import views
urlpatterns = [
    path('core/all/',views.db_data,name='alldata'),
]