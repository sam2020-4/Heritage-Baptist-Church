from django.shortcuts import render
from .models import Team, Sermon, Children, Youth, Event

# Create your views here.
def about(request):
    teams = Team.objects.all()
    return render(request, 'church/about.html', {'title': 'About', 'teams': teams})

def index(request):
    sermons = Sermon.objects.all()
    return render(request, 'church/index.html',{'title': 'Home', 'sermons': sermons})
  
def contact(request):
    return render(request, 'church/contact.html',{'title': 'contact'})

def give(request):
    return render(request, 'church/give.html',{'title': 'give'})

def children(request):
    children = Children.objects.all()
    return render(request, 'church/children.html', {'children': children})

def youth(request):
    youths = Youth.objects.all()
    return render(request, 'church/youth.html', {'youths': youths})

def events(request):
    events = Event.objects.all()
    return render(request,'church/events.html', {'events': events})
