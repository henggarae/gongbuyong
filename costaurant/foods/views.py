from django.shortcuts import render
from django.http import HttpResponse,Http404
from datetime import datetime
# Create your views here.

def index(request):
    today = datetime.today().date()
    context = {"date":today}
    return render(request, 'foods/index.html', context = context)

def food_detail(request,food):
    context = dict()
    if food == "chicken":
        context["name"] = "코딩에 빠진 닭"
        context["description"] = "치킨이에요"
        context["price"] = "10000"
        context["img__path"] = "foods/images/chicken.jpg"
    else:
        raise Http404("그런건 없다 당신의 전역처럼")
    return render(request, 'foods/detail.html', context=context)