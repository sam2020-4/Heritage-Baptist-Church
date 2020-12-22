from django.urls import path
from Church import views

urlpatterns = [
    path('',views.about, name='about'),
    path('index',views.index, name='home'),
    path('contact/',views.contact, name='contact'),    
]