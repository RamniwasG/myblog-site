from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_projects, name="all-projects-page"),
    path('projects/<slug:slug>', views.project_details, name="project-detail-page"),
]
