from time import time
from django.shortcuts import render, HttpResponse
from datetime import datetime
from my_app.models import Contact
def index(request):
    context={
        'variable':'Django',
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('This is an about page')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        return HttpResponse('Your response has been recorded successfully')

    return render(request, 'contact.html')

def categories(request):
    return HttpResponse('This is services page')
