from django.urls import path
from enroll import views

urlpatterns = [
    path('',views.home,{'check':'OK'},name='home'),
    path('userreg/',views.userreg),
    path('success/',views.success),
    path('userdet/<int:id>/',views.userdetail,name='userdetail'),
]
