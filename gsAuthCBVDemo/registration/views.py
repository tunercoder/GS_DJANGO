from django.shortcuts import render
from django.views.generic import TemplateView

class ProfileTemplateView(TemplateView):
    template_name='registration/profile.html'