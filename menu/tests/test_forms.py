from django.test import TestCase
from menu.forms import OrderForm
from menu.forms import MenuForm
from menu.models import Menu
from menu.models import FoodOption
import datetime


class OrderFormTest(TestCase):
    """ Test class to test OrderForm Form  """

    @classmethod
    def setUpTestData(cls):

        food = FoodOption.objects.create(name='fish', description='fish meat')
        menu = Menu.objects.create(name='special fish', menu_date=datetime.date.today())
        menu.food_plate.add(food.id)

        food = FoodOption.objects.create(name='chicken', description='grilled chicken')
        menu = Menu.objects.create(name='special chicken',
                                   menu_date=datetime.datetime.now() + datetime.timedelta(days=1))
        menu.food_plate.add(food.id)

    def test_menu_model_choice_field_return_only_today_instances(self):
        """ Case to test the menu model choice field method only get today instances created """
        form = OrderForm()
        expected_today_options_menu = Menu.objects.filter(menu_date__year=datetime.datetime.today().year,
                                                          menu_date__month=datetime.datetime.today().month,
                                                          menu_date__day=datetime.datetime.today().day).count()
        self.assertEquals(expected_today_options_menu, form.fields['menu'].queryset.count())

    def test_try_to_call_the_form_after_eleven_am(self):
        """ Case to test the clean validation to try the create a order instance before 11 am """
        today_options_menu = Menu.objects.filter(menu_date__year=datetime.datetime.today().year,
                                                 menu_date__month=datetime.datetime.today().month,
                                                 menu_date__day=datetime.datetime.today().day)[0]
        order_suhhestion = 'without sauces'
        form_data = {'menu': today_options_menu, 'order_suggestion': order_suhhestion}
        form = OrderForm(data=form_data)
        if datetime.datetime.now().hour > 11:
            self.assertFalse(form.is_valid())
        else:
            self.assertTrue(form.is_valid())


class MenuFormTest(TestCase):
    """ Test class to test MenuForm Form  """

    @classmethod
    def setUpTestData(cls):

        food = FoodOption.objects.create(name='fish', description='fish meat')
        food = FoodOption.objects.create(name='chicken', description='grilled chicken')

    def test_food_plates_model_choices_queryset_return_all_instances(self):
        """ Case to test the food_plates model choice field to get all instances in query set """
        form = MenuForm()
        expected_food_options = FoodOption.objects.all().count()
        self.assertEquals(expected_food_options, form.fields['food_plates'].queryset.count())






