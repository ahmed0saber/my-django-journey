from django.shortcuts import render

# Create your views here.

def home(response):
    degree = 0
    if response.method == "POST":
        answers = response.POST.get('answers')
        result = response.POST.get('result')
        if answers == "django":
            degree += 50
        if result == "3":
            degree += 50
    return render(response, "main/home.html", {"degree": degree})
