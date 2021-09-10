import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from menu.models import FoodOption
from menu.models import Menu
from menu.models import Order


class FoodOptionModelTest(TestCase):
    """ Test class to test FoodOption model and methods """

    @classmethod
    def setUpTestData(cls):
        FoodOption.objects.create(name='meat', description='grilled meat')

    def test_object_name_is_the_name(self):
        """ Case to test the str method  return the correct object name"""
        food = FoodOption.objects.filter()[0]
        expected_object_name = '{}'.format(food.name)
        self.assertEquals(expected_object_name, str(food))


class MenuModelTest(TestCase):
    """ Test class to test Menu model and methods """

    @classmethod
    def setUpTestData(cls):
        food = FoodOption.objects.create(name='meat', description='grilled meat')
        menu = Menu.objects.create(name='special meat', menu_date=datetime.date.today())
        menu.food_plate.add(food.id)

    def test_object_name_is_the_name_capitalize(self):
        """ Case to test the str method  return the correct object name"""
        menu = Menu.objects.all()[0]
        expected_object_name = '{}'.format(menu.name).capitalize()
        self.assertEquals(expected_object_name, str(menu))

    def test_get_food_plates_return_all_food_plates(self):
        """ Case to test class method with decorator @property return the all food_plate linked """
        menu = Menu.objects.all()[0]
        expected_result = menu.food_plate.all().count()
        self.assertEquals(expected_result, menu.get_food_plates.count())


class OrderModelTest(TestCase):
    """ Test class to test Order model and methods """

    @classmethod
    def setUpTestData(cls):
        food = FoodOption.objects.create(name='meat', description='grilled meat')
        menu = Menu.objects.create(name='special meat', menu_date=datetime.date.today())
        menu.food_plate.add(food.id)
        user = User.objects.create_user('camilo', '', 'camilo123456')
        Order.objects.create(user=user, menu=menu, order_suggestion='without sauces', order_date=datetime.date.today())

    def test_object_name_is_str_with_id_username_and_order_date(self):
        """ Case to test the str method  return the correct object name """
        order = Order.objects.get(id=1)
        expected_object_name = 'Order num: {0}, from customer: {1} and date {2}'.format(order.id, order.user.username,
                                                                                        order.order_date)
        self.assertEquals(expected_object_name, str(order))




