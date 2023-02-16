from django.http import HttpResponse
from landingPage.models import Project

def project_view(request, id=None): 
    #id = request.GET.get("id")
    projects = Project.objects.all()
    
    
    if id == None: 
        response = ""
        for id in range(1, 6):
            project = projects.get(id=id)
            response += " / " + str(project) + " \ " 

        print(projects)
        return HttpResponse(f'<h1> Meus Projetos <h1> {response}' )
    else:
        project = projects.get(id=id) 
        return HttpResponse(f'<h1> Projeto #{id} <h1>')


    