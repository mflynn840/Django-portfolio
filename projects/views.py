from django.shortcuts import render
from projects.models import ProjectEntry
# Create your views here.

def project_index(request):
    
    #preform query
    projects = ProjectEntry.objects.all()
    
    #construct dictionary
    context = {
        "projects" : projects
    }
    
    #render the html page using the query results
    return render(request, "projects/project_index.html", context)


'''
    request: html request
    pk: the primary key of the requested project
'''
def project_detail(request, pk):
    
    #get the requested project entry
    project = ProjectEntry.objects.get(pk=pk)
    context = {
        "project" : project
    }
    #render page with that project
    return render(request, "projects/project_detail.html", context)
