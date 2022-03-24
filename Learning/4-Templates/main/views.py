from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, id):
    list = ToDoList.objects.get(id=id)
    my_dict = {"name":list.name}
    return render(response, "main/base.html", my_dict)

def home(response):
    return render(response, "main/home.html", {"name":"Not Found"})
