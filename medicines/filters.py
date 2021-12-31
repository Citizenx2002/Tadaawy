import django_filters
from .models import Medicines

class MedicineFilter(django_filters.FilterSet):
    manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')




    class Meta:
        model = Medicines
        fields = ['name']
        exclude=['image','attribute','active','price']