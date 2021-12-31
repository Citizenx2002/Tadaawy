from django.urls import path
from . import views

urlpatterns=[
    path('diseases/',views.diseases,name="disease"),
    path('diseases/<str:dname>/',views.single_disease,name="sdisease"),
]