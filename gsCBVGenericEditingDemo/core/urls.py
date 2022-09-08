from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(),name='contact'),
    path('thankyou/', views.ThankyouView.as_view(),name='thankyou'),
    path('studentcreate/', views.StudentCreateView.as_view(),name='studentcreate'),
]
