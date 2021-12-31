from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicines
from django.contrib.auth.decorators import login_required
from .filters import MedicineFilter
# Create your views here.
@login_required
def medicines(request):
    medicine=Medicines.objects.all()
    myfilter=MedicineFilter(request.GET,queryset=medicine)
    return render(request,'medicine.html',{'medicine':medicine,'myfilter':myfilter})
@login_required
def single_medicine(request,id):
    med = get_object_or_404(Medicines, pk=id)
    return render(request,'medicine-single.html',{'med':med})   

