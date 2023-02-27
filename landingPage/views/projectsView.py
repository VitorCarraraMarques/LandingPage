from django.shortcuts import render
from landingPage.models import Project

def project_view(request, id=None): 
    #id = request.GET.get("id")
    projects = Project.objects.all()
    

    if id == None: 
        return render(request, template_name='projects/projects.html', status=200)
    else: 
        return render(request, template_name='projects/project.html', status=200)


    