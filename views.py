from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader
from .models import student as tb

def show(request):
    '''time=datetime.datetime.now() #render current time and date
    htm='Current time is{}'.format(time)
    return HttpResponse(htm,"this is django view")'''

    temp=loader.get_template('home.html')           #temp is a variable
    return HttpResponse(temp.render())
# Create your views here.
def about(request):
    temp=loader.get_template('about.html')           #temp is a variable
    return HttpResponse(temp.render())

def contact(request):
    x=tb.objects.all().values()
    temp=loader.get_template('contact.html')           #temp is a variable
    context={
        "x":x,
    }
    return HttpResponse(temp.render(context,request))
def register(request):
    if request.method=='POST':
        data=tb()
        data.Name=request.POST["name"]            #1 attribute is of table and 2 is of form
        data.City=request.POST["place"]
        data.save()
        return render(request,"about.html")
    else:
        return render(request,"about.html")