from django.urls import path,include
from . import views
urlpatterns = [
    path('studentlist/', views.StudentListView.as_view(),name='studentlist'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(),name='studentdetail'),
    
]
