import contextlib
import re

from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from .forms import FoodForm
from.models import Food

# Create your views here.
def Home (request):
    return render (request, 'home.html' )

def addFood(request):
    form = FoodForm
    context = {"form":form}

    if request.method == "POST":
       form = FoodForm (request.POST)
       if form.is_valid():
           form.save ()
           return redirect ("readAllFoods")
    
    return render (request, 'form.html' , context )

def readAllFoods (request):
    foods = Food.objects.all ()
    context = {"foods" : foods}
    return render (request,'foods.html', context )

def readOneFood (request,pk):
    food = Food.objects.get (id=pk)
    context = {"food" : food}
    return render (request, 'food.html' , context )

def updateOneFood (request,pk):
    food = Food.objects.get (id=pk)
    form = FoodForm (instance=food )

    if request.method == "POST":
        form = FoodForm (request.POST , instance=food)
        if form.is_valid ():
            form.save ()
            return redirect ("readAllFoods")
    context = {"form" : form}
    return render (request,'form.html',context)

def deleteOneFood (request,pk):
    food = Food.objects.get (id=pk)
    
    if request.method == "POST":
        food.delete ()
        return redirect ("readAllFoods")
    context = {"food":food}
    return render (request, 'delete.html' , context )