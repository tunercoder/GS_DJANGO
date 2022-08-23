from django.urls import path
from course import views

urlpatterns = [
    path('',views.index),
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
]
