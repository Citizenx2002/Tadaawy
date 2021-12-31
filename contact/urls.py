from django.urls.conf import path
from . import views


urlpatterns=[
        path('contact/',views.contact,name='contact'),
]