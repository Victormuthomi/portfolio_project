from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class PortfolioListview(TemplateView):
    template_name = 'home.html'
