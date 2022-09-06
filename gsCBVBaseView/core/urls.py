from re import template
from django.urls import path
from core import views 

urlpatterns = [
    path('fbv/', views.fbv,name='fbv'),
    path('cbv/', views.Myview.as_view(name='rahul'),name='cbv'),
    path('home/',views.home,name='home'),
    path('homecbv/', views.MyHomeView.as_view(),name='homecbv'),

    path('home/',views.home,name='home'),
    path('homecbv/', views.MyHomeView.as_view(),name='homecbv'),

    path('aboutfun/',views.aboutfun,name='aboutfun'),
    path('aboutfuncbv/', views.AboutFunView.as_view(),name='aboutfuncbv'),

    path('contact/',views.contact,name='contact'),
    path('contactcbv/', views.ContactView.as_view(),name='contactcbv'),

    
    path('newsfun/',views.newsfun,{'template_name':'core/newsfun.html'},name='newsfun'),
    path('newsfun2/',views.newsfun,{'template_name':'core/newsfun2.html'},name='newsfun2'),

    path('newsfuncbv/',views.NewsFunView.as_view(template_name='core/newsfun.html'),name='newsfuncbv')
]
