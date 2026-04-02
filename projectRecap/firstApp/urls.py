from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home ,name='Home'),
    path('addFood',views.addFood, name='addFood'),
    path ('readAllFoods',views.readAllFoods , name='readAllFoods' ),
    path ('readOneFood/<str:pk>',views.readOneFood, name='readOneFood' ),
    path ('updateOneFood/<str:pk>',views.updateOneFood, name='updateOneFood' ),
    path ('deleteOneFood/<str:pk>',views.deleteOneFood, name='deleteOneFood' ),
    path ('index',views.index, name='index' ),
    path ('makePayment',views.makePayment, name='makePayment' )

]