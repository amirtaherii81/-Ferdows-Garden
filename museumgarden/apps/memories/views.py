from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.forms import inlineformset_factory
from .models import MemoryGallery, Memory, MemoryLike
from .forms import MemoryForm, MemoryGalleryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


class ShowMemoriesView(View):
    def get(self, request, *args, **kwargs):
        memories = Memory.objects.filter(is_active=True)
        if request.user.is_authenticated:
            list_memory_kiked = MemoryLike.objects.filter(user_like_id=request.user.id).values('memory_id')
            list_memory_kiked_id = [memory['memory_id'] for memory in list_memory_kiked]
            return render(request, 'memories_app/show_memories.html', {'memories':memories, 'list_memory_kiked_id':list_memory_kiked_id})
        return render(request, 'memories_app/show_memories.html', {'memories':memories})



@login_required
def add_memory(request):
    ImageFormSet = inlineformset_factory(Memory ,MemoryGallery, form=MemoryGalleryForm, extra=4)
    if request.method == 'GET':
        memory_form = MemoryForm()
        image_formset = ImageFormSet(queryset=MemoryGallery.objects.none())
        context = {
            'memory_form':memory_form,
            'image_formset':image_formset
        }
        return render(request, 'memories_app/register_memory.html', context)
    elif request.method=="POST":
        memory_form = MemoryForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if memory_form.is_valid() and image_formset.is_valid():
            data = memory_form.cleaned_data
            mem_obj=Memory.objects.create(
                memory_title = data['memory_title'],
                memory_text = data['memory_text'],
                user_registered = request.user
            )

            for form in image_formset.cleaned_data:
                if form:
                    MemoryGallery.objects.create(
                        memory_image_name = form['memory_image_name'],
                        memory = mem_obj
                    )
            messages.success(request, "ثبت خاطره با موفقیت انجام شد", 'success')
            return redirect('main:index')

        else:
            context = {
                'memory_form':memory_form,
                'image_formset':image_formset
        }
            messages.error(request, 'اطلاعات وارد شده معتبر نمیباشد', 'error')
            return render(request, 'memories_app/register_memory.html', context)
        
    # return render(request, 'memories_app/register_memory.html', {'form':form})

def like(request):
    if request.method == 'GET':
        memory_id = request.GET.get('memory_id')
        memory = MemoryLike.objects.get(id=memory_id)
        likememory= MemoryLike.objects.filter(memory_id=memory.id, user_like=request.user)
        if not likememory:
            likememory=MemoryLike(memory=memory)
            likememory.user_like= request.user
            likememory.save()
        return HttpResponse('success')
    return HttpResponse('unsuccess')