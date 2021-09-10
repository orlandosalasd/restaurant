from datetime import datetime
from django.core.exceptions import ValidationError
from django import forms
from menu.models import Menu
from menu.models import FoodOption


class OrderForm(forms.Form):
    """ Class Form to create a Order """
    menu = forms.ModelChoiceField(queryset=Menu.objects.filter(menu_date__year=datetime.today().year,
                                                               menu_date__month=datetime.today().month,
                                                               menu_date__day=datetime.today().day))
    order_suggestion = forms.CharField(help_text="Enter any suggestions for your order.")

    def clean(self):

        # validate if the order takes after to 11 am
        if datetime.now().hour > 11:
            raise ValidationError('Orders must be placed before 11 AM')

        return self.cleaned_data


class MenuForm(forms.Form):
    """ Class Form to create a Menu """
    name = forms.CharField(help_text="Enter menu name")
    food_plates = forms.ModelMultipleChoiceField(queryset=FoodOption.objects.all())



