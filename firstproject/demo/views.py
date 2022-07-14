import email
from django.shortcuts import render,HttpResponse
from datetime import datetime
from demo.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    # context={"variable":"Aman is a badboy"}
    # return render(request, 'index.html',context)
    # messages.success(request,'this is the text msg')
    return render(request, 'index.html')
    # return HttpResponse('this is homepage')

def about(request):
    # return HttpResponse('this is about page')
    return render(request, 'about.html')

def services(request):
    # return HttpResponse('this is service page')
    return render(request, 'services.html')

def contact(request):
    if (request.method == "POST"):
        name=request.POST['name'] 
        email=request.POST['email']
        phone=request.POST['phone']


        # name= request.POST.get("name")
        # email=request.POST.get("email")
        # phone=request.post.get("phone")       
        contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
        print(name,email,phone)
        contact.save()
        messages.success(request, 'Your Messages has been sent')
    return render(request, 'contact.html')
    #return HttpResponse('this is Contact page')