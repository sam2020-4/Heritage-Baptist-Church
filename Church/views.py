from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'church/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'church/contact.html',{'title': 'contact'})