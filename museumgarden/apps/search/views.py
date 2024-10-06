from django.shortcuts import render
from django.views import View
from apps.memories.models import Memory
from apps.workshops.models import Workshop
from django.db.models import Q
# Create your views here.
class SeachResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        memories = Memory.objects.filter(
            Q(memory_title__icontains=query)
        )
        workshops = Workshop.objects.filter(
            Q(title__icontains=query)
        )
        context={
            'memories':memories,
            'workshops': workshops
        }
        return render(request,'search_app/search_results.html',context)