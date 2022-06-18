from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from projects.models import Project

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
