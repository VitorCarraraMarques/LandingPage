from django.urls import path 
from landingPage.views.projectsView import project_view

urlpatterns = [
    path("", project_view, name="projects"),
    path("<int:id>", project_view, name="project")
]