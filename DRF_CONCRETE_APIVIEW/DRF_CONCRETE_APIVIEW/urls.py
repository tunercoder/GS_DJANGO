from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.StudentListCreateAPI.as_view(),name='stuapi'),    
    path('stuapi/<int:pk>/', views.StudentRetrieveUpdateDestroyAPI.as_view(),name='stuapirud'),    
]