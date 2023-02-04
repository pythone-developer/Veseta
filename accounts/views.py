from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm,UserCreationForm,Update_User_Form,Update_Profile_Form
from django.contrib.auth import authenticate,login
# Create your views here.

def doctors_list(request):
    doctors =User.objects.all()
    return render(request,"user/doctors_list.html",{
        'doctors':doctors,
    })


def doctors_detail(request,slug):
    doctors_detail =Profile.objects.get(slug=slug)
    return render(request,"user/doctors_detail.html",{
        'doctors_detail':doctors_detail,
    })


def Signup(request):
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect('accounts:doctors_list')
    else:
        form =UserCreationForm()
    return render(request,"user/signup.html",{
        'form':form
    })
   