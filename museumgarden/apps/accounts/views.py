from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class RegisterUserView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterUserForm()
        return render(request, "accounts_app/register.html", {'form':form})
    
    
    def post(self, request, *args,**kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user=User(
                first_name = data['first_name'],
                last_name = data['last_name'],
                username = data['username'],
            )
            user.set_password(data["password1"])
            user.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد', 'success')
            return redirect('main:index')
        else:
            messages.error(request, "اطلاعات وارد شده معتبر نمی باشد", 'danger')
            return render(request, "accounts_app/register.html",{"form": form})

class LoginUserView(View):
    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(request, 'accounts_app/login.html', {'form':form})
        
    def post(self, request, *args, **kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد')
                next_url = request.GET.get('next')
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return redirect('main:index')
            else:
                messages.warning(request, 'کاربر یافت نشد')
                return render(request, 'accounts_app/login.html',{'form': form})
        else:
            messages.warning(request, "اطلاعات وارد شده معتبر نمی باشد")
            return render(request, 'accounts_app/login.html',{'form':form})


            
class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request,'goodby')
        return redirect('main:index')



