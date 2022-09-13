from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.LCStudentAPI.as_view(),name='stuapi'),    
    path('stuapi/<int:pk>/', views.RUDStudentAPI.as_view(),name='stuapirud'),    
]