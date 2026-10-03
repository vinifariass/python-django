from django.views.generic import (TemplateView, ListView, DetailView,CreateView, UpdateView, DeleteView)
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
    template_name = 'basic_app/school_list.html'

class StudentListView(ListView):
    context_object_name = 'students'
    model = models.Student
    template_name = 'basic_app/student_list.html'
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    
class SchoolCreateView(CreateView):
    fields = ('name', 'location', 'principal')
    model = models.School
    template_name = 'basic_app/school_form.html'