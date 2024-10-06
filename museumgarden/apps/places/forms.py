from django import forms

class MessageForm(forms.Form):
    full_name=forms.CharField(label='نام و نام خانوادگی')
    email=forms.EmailField(label='ایمیل')
    subject=forms.CharField(label='عنوان پیام')
    message=forms.CharField(label='متن پیام', widget=forms.Textarea)

    