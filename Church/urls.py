from django.urls import path
from . import views

urlpatterns = [
    path('',views.about, name='about'),
<<<<<<< HEAD
    path('index',views.index, name='home'),

=======
    path('contact/',views.contact, name='contact'),    
>>>>>>> ddf1a07f8bd89f8e8af5886d33ae8fb449e86f2b
]