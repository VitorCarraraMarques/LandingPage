from django.urls import path 
from landingPage.views.homeView import home_view

urlpatterns = [
    path("", home_view),
]