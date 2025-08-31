from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='index.html'

class AboutMePage(TemplateView):
    template_name='aboutMe.html'


class ProjectsPage(TemplateView):
    template_name='projects.html'

class ServicesPage(TemplateView):
    template_name='services.html'

class ContactMe(TemplateView):
    template_name='contactMe.html'