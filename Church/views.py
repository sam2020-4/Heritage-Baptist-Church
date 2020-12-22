from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'church/about.html', {'title': 'About'})

<<<<<<< HEAD
def index(request):
    return render(request, 'church/index.html',{'title': 'Home'})
=======
def contact(request):
    return render(request, 'church/contact.html',{'title': 'contact'})
>>>>>>> ddf1a07f8bd89f8e8af5886d33ae8fb449e86f2b
