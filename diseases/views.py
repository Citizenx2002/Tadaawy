from django.shortcuts import render, get_object_or_404, redirect
from .models import Diseases
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def diseases(request):
    disease=Diseases.objects.all()
    return render(request,'disease.html',{'disease':disease})
    
@login_required
def single_disease(request,dname):
    des = get_object_or_404(Diseases, name=dname)
    return render(request,'disease-single.html',{'des':des}) 