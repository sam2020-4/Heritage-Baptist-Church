from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'church/about.html', {'title': 'About'})

def index(request):
    return render(request, 'church/index.html',{'title': 'Home'})
def contact(request):
    return render(request, 'church/contact.html',{'title': 'contact'})
