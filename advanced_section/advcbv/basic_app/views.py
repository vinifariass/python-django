from django.shortcuts import render
from django.views.generic import TemplateView

class CBView(TemplateView):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")