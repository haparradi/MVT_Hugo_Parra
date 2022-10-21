from django.shortcuts import render
from .models import Family
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def family_members(request, name, age, date):

    family = Family(name=name, age=age, date=date)
    family.save()
    
    template = loader.get_template("template1.html")

    document = template.render()
    
    return HttpResponse(document)

def list_of_members(request):

    list = Family.objects.all()

    return render(request, "template2.html" , {"list_of_members": list})
