from django.urls import path
from gsauth import views

urlpatterns = [
    # path('',views.home,{'check':'OK'},name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('changepass1/',views.user_change_pass1,name='changepass1'),
    path('success/',views.success,name='sucess'),
    
]
