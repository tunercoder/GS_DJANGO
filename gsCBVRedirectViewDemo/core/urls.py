
from ast import pattern
from django.urls import path,include
from . import views
urlpatterns = [
    path('rehome/', views.RedirectView.as_view(url='/core/'),name='home'),
    path('index/', views.TemplateView.as_view(template_name='core/home.html'),name='index'),
    path('', views.TemplateView.as_view(template_name='core/home.html'),name='blankhome'),
   
    #by inherted
    path('geeky/', views.GeekyRedirectView.as_view(),name='geeky'),

    #by pattern name for url
    path('pattern/', views.RedirectView.as_view(pattern_name='index'),name='pattern'),

    #pass captured data to redirect page
    path('home/<int:pk>/', views.GeekRedirectView.as_view(),name='homepasskwargs'),
    path('homewithkwargs/<int:pk>/', views.TemplateView.as_view(template_name='core/home.html'),name='homewithkwargs'),



]


