from django import forms
from .models import Memory, MemoryGallery



class MemoryForm(forms.ModelForm):
    memory_title = forms.CharField(label="عنوان خاطره", widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "عنوان خاطره را بنویسید"}))
    memory_text = forms.CharField(label="متن خاطره", widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"متن خاطره بنوسید"}))

    class Meta:
        model = Memory
        # fields = '__all__'
        fields = ['memory_title', 'memory_text']




class MemoryGalleryForm(forms.ModelForm):
    class Meta:
        model = MemoryGallery
        fields = ['memory_image_name',]