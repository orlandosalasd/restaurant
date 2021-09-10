from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class FoodOption(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    food_plate = models.ManyToManyField(FoodOption)
    menu_date = models.DateField()

    def __str__(self):
        return self.name.capitalize()

    @property
    def get_food_plates(self):
        """
        Method to return all food plate linked in a query.
        """
        return self.food_plate.all()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_suggestion = models.TextField()
    order_date = models.DateField()

    def __str__(self):
        return 'Order num: {0}, from customer: {1} and date {2}'.format(self.id, self.user.username, self.order_date)







