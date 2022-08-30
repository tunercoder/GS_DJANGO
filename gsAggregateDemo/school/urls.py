from django.urls import path
from school import views
urlpatterns = [
    path('list/',views.student_list,name='list'),
]
