from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from home.models import Contact

# Create your views here.
def index(request):

    return render(request,'index.html')

def contact(request):
    def contact(request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            desc = request.POST.get('desc')
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, 'Form submitted successfully')
    return render(request,'contact.html')


def Privacy(request):
    return render(request,'Privacy.html')

def terms(request):
    return render(request,'terms.html')

def login(request):
    return render(request,'login.html')