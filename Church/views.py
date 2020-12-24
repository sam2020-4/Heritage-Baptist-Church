from django.shortcuts import render
from .models import Team

# Create your views here.
def about(request):
    teams = Team.objects.all()
    return render(request, 'church/about.html', {'title': 'About', 'teams': teams})

def index(request):
    return render(request, 'church/index.html',{'title': 'Home'})
  
def contact(request):
    return render(request, 'church/contact.html',{'title': 'contact'})
    
