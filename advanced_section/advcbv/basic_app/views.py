from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from . import models
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello, World!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'school_list.html'
    context_object_name = 'schools'
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_detail.html'
    context_object_name = 'school'