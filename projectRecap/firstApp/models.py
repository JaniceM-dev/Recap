from os import name

from django.db import models

# Create your models here.
class Food (models.Model):

    CATEGORY_CHOICES = [
        ('protein','Protein'),
        ('cabohydrate','Carb'),
        ('vegetable','Veggie'),
        ('fruit','Fruit')
    ]




    name= models.CharField (max_length= 350)
    category = models.CharField (
        max_length= 200,
        choices= CATEGORY_CHOICES  
        )
    description = models.CharField (max_length= 400)
    image = models.CharField (max_length= 300)
    price = models.FloatField (
        default= 0.00
    )
    # created_at = models.DateField (auto_now_add=True)
    # updated_at = models.DateField (auto_now=True)

    def __str__(self):
       return self.name
    
