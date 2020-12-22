from django.shortcuts import render
from .models import Team

# Create your views here.
def about(request):
    teams = Team.objects.all()
    return render(request, 'church/about.html', {'title': 'About', 'teams': teams})