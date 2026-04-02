from django.shortcuts import render ,redirect
from django.http import HttpResponse, response 
from .forms import FoodForm
from.models import Food
from django_daraja.mpesa.core import MpesaClient

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

def index(request):
    # cl = MpesaClient()
    # phone_number = '0116960694'
    # amount = 100
    # account_reference = 'RECAP'
    # transaction_desc = 'Learning Purposes'
    # callback_url = 'https://api.darajambili.com/express-payment'
    # response = cl.stk_push (phone_number,amount,account_reference,transaction_desc,callback_url)
    return  HttpResponse (" Hello World")

def makePayment (request):
    #get user phone number
    # get the amount
    # trigger an stk push

    if request.method == "POST":
        phoneNumber = request.POST.get ("phoneNumber")
        amount = int(float(request.POST.get ("amount")))
        cl = MpesaClient ()
        phone_number = phoneNumber
        amount = amount
        account_reference = 'WAGITHIMBUIIIII!!!!'
        transaction_desc = 'Helping those in need'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    else :
        pass
    context ={}
    return render (request,'buy.html',context )


