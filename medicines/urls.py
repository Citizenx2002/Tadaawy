
from django.urls.conf import path
from . import views

urlpatterns=[
    path('medicines/',views.medicines,name="medicine"),
    path('<int:id>',views.single_medicine,name='single_medicine'),
    path('checkout/', views.check_out, name='checkout'),
    path('checkout/thanks/', views.thanks, name='thanks'),
]