from dataclasses import fields

from django.forms import ModelForm
from . import models


class FoodForm (ModelForm):
    class Meta:
        model = models.Food
        fields = '__all__'