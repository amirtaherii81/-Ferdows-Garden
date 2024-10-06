from django.shortcuts import render, redirect
from django.views import View
from .models import Place, TicketPrice, Message
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from .forms import MessageForm
from django.contrib import messages
# Create your views here.

class ShowGardenHistoryView(View):
    def get(self, request):
        return render(request, 'places_app/history.html')
    

class  ShowGardenPartsView(View):
    def get(self, request):
        places = Place.objects.all()
        return render(request, 'places_app/places.html', {'places': places})
        
        
class ShowPartDetailView(View):
    def get(self, request, id):
        place = Place.objects.get(id=id)
        return render(request, 'places_app/part_detial.html', {'place': place})
    

class DownloadPathGardenView(View):
    def get(self, request):
        fs = FileSystemStorage()
        file_name = 'direction_pdf/direction.pdf'
        if fs.exists(file_name):
            with fs.open(file_name) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition']='attachment; filename=ferdowsGardenPath.pdf'
                return response
            
        else:
            return HttpResponseNotFound('فایل شما پیدا نشد!')
        

class ShowTimeRuleView(View):
    def get(self, request):
        places = Place.objects.all()
        ticket_price = TicketPrice.objects.all()
        context = {
            'places': places,
            'ticket_price': ticket_price,
        }
        return render(request, 'places_app/ticket_price.html', context)

def false():
    # class ContectView(View):
    #     def get(self, request):
    #         form = MessageForm(request.POST)
    #         if form.is_valid():
    #             cd = form.cleaned_data
    #             msg = Message()
    #             msg.full_name = cd['full_name']
    #             msg.email = cd['email']
    #             msg.subject = cd['subject']
    #             msg.message = cd['message']
    #             msg.save()
    #             return redirect('main:index')
    #         return render(request, 'places_app/contact.html',{'form': form}
    pass



class ContactView(View):
    def get(self, request):
        form = MessageForm()
        return render(request, 'places_app/contact.html', {'form': form})
    
    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            msg = Message()
            msg.full_name = cd['full_name']
            msg.email = cd['email']
            msg.subject = cd['subject']
            msg.message = cd['message']
            msg.save()
            messages.success(request, "پیام شما ارسال شد", "success")
            return redirect('main:index')
        return render(request, 'places_app/contact.html', {'form': form})
