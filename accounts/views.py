
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, UserForm , ProfileForm
from medicines.models import Medicines
from diseases.models import Diseases
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.urls import reverse

# Create your views here.

def index (request):
    medicine=Medicines.objects.all()
    disease=Diseases.objects.all()
    return render(request,'index.html',{'medicine':medicine,'disease':disease})


def signup (request):
    form=SignUpForm()
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('index')
        else:
            print(form.errors)
    return render(request,'signup.html',{'form':form})


def check_out(request):
    return render(request,'checkout.html')

def thanks (request):
    return render(request,'thankyou.html')

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'profile.html',{'profile':profile})




@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        post_data=request.POST or None
        clean_data=request.FILES or None
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(post_data ,clean_data,instance=request.user.profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()

            return redirect(reverse('profile'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request,'profile-edit.html',{'userform':userform , 'profileform':profileform})