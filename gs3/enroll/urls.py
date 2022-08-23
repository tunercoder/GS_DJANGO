from django.urls import path,include
from .import views

urlpatterns = [
    path('stu/',views.studeninfo),
    path('sturegister/',views.studentRegistration),
    path('success/',views.thankyou),
]
