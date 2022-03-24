from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    list = ToDoList.objects.get(id=id)
    my_dict = {"list":list}
    
    if response.method == "POST":
        if response.POST.get('save'):
            for item in list.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get('add'):
            txt = response.POST.get('new')
            if len(txt) > 2:
                list.item_set.create(text=txt, complete=False)
            else:
                print("invalid, less then 2 characters")
    
    return render(response, "main/base.html", my_dict)

def home(response):
    return render(response, "main/home.html", {"name":"Not Found"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

