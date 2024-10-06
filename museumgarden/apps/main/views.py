from django.shortcuts import render
from django.views import View
from django.conf import settings
# Create your views here.

def media_admin(request):
    return {"media_url": settings.MEDIA_URL}


class ShowView(View):
    def get(self, request):
        return render(request, 'main_app/index.html')
