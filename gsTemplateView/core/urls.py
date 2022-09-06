
from django.urls import path,include

from django.views.generic.base import TemplateView
from .views import MyTemplateView
urlpatterns = [
    path('home/', TemplateView.as_view(template_name='core/home.html'),name='home'),
    path('fun/', TemplateView.as_view(template_name='core/fun.html'),name='fun'),

    path('homein/', MyTemplateView.as_view(),name='homein'),

     path('homeextracontext/<int:salary>/', MyTemplateView.as_view(extra_context={'course':'python'}),name='homeextracontext'),
]

