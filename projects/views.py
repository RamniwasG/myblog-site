from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Projects

def all_projects(request):
    latest_projects = Projects.objects.all().order_by('-id')
    return render(request, 'projects/all-projects.html', {
        "projects": latest_projects
    })

def project_details(request, slug):
    identified_project = get_object_or_404(Projects, slug=slug)
    return render(request, 'projects/project-detail.html', {
        "project": identified_project,
        "project_tags": identified_project.tags.all(),
        "languages": identified_project.languages.all(),
        'technologies': identified_project.technologies.all()
    })