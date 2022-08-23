from django.urls import path,include
from . import views
urlpatterns = [
    path('django/',views.learndjango,name='courseone'),
]
