from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.core.signing import settings
import os
from django.http import Http404
# Create your views here.

class ShowWorkshopView(ListView):
    model = Workshop
    template_name = 'workshops_app/workshoplist.html'
    context_object_name = 'workshops'
    queryset = Workshop.objects.order_by('-is_active')
    paginate_by = 2


class ShowWorkshopReport(DetailView):
    model = Workshop
    template_name = 'workshops_app/workshopreport.html'
    context_object_name = 'workshop'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        try:
            workshop = Workshop.objects.get(id = pk)
            workshop.view_number += 1
            workshop.save()
            path=settings.MEDIA_ROOT+ 'images/workshop/reports/' + str(pk)
            if os.path.isdir(path):
                image_list = os.listdir(path)
                context['image_list'] = image_list
            return context
        except Workshop.DoesNotExist:
            raise Http404("workshop not found.")
        