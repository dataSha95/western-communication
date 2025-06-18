from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')
def careers(request):
    return render(request, 'home/careers.html')
def contact(request):
    return render(request, 'home/contact.html')
