from django.urls import path 

from .views import PortfolioListview

urlpatterns=[
    path('',PortfolioListview.as_view(), name='home'),
    ]