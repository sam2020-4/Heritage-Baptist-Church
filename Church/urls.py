from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'), 
    path('give/',views.give, name='give'), 
    path('children/',views.children, name='children'),
    path('youth/',views.youth, name='youth'),
]

if settings.DEBUG:urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


