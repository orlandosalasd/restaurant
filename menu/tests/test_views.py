import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from person.choices import ProfileRoles
from django.urls import reverse
from menu.models import Menu
from menu.models import FoodOption
from menu.models import Order


class IndexViewTest(TestCase):
    """ Test Class to test Index View """
    def setUp(self):
        admin_user = User.objects.create_user('admin_user', '', 'camilo123456')
        admin_user.profile.rol = ProfileRoles.ADMINISTRATOR
        admin_user.save()

        customer_user = User.objects.create_user('customer_user', '', 'camilo123456')
        customer_user.profile.rol = ProfileRoles.CUSTOMER
        customer_user.save()

        food = FoodOption.objects.create(name='meat', description='grilled meat')
        menu = Menu.objects.create(name='special meat', menu_date=datetime.date.today())
        menu.food_plate.add(food.id)

    def test_logged_in_uses_correct_template(self):
        """ Case to test if the view render in the correct template """
        login = self.client.login(username='admin_user', password='camilo123456')
        resp = self.client.get(reverse('index'))

        self.assertEqual(str(resp.context['user']), 'admin_user')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_all_todays_menus_in_context(self):
        """ Case to test if the view render the correct context information """
        login = self.client.login(username='admin_user', password='camilo123456')
        resp = self.client.get(reverse('index'))

        expected_menu_options = Menu.objects.filter(menu_date__year=datetime.datetime.today().year,
                                                    menu_date__month=datetime.datetime.today().month,
                                                    menu_date__day=datetime.datetime.today().day).count()

        self.assertTrue('today_menu_options' in resp.context)
        self.assertEqual(len(resp.context['today_menu_options']), expected_menu_options)


class UserOrderViewTest(TestCase):
    """ Test Class to test UserOrder List View """

    def setUp(self):
        admin_user = User.objects.create_user('admin_user', '', 'camilo123456')
        admin_user.profile.rol = ProfileRoles.ADMINISTRATOR
        admin_user.save()

        customer_user = User.objects.create_user('customer_user', '', 'camilo123456')
        customer_user.profile.rol = ProfileRoles.CUSTOMER
        customer_user.save()

        food = FoodOption.objects.create(name='meat', description='grilled meat')
        menu = Menu.objects.create(name='special meat', menu_date=datetime.date.today())
        menu.food_plate.add(food.id)

        Order.objects.create(user=customer_user, menu=menu, order_suggestion='without sauces', order_date=datetime.date.today())
        Order.objects.create(user=admin_user, menu=menu, order_suggestion='gluten free',
                             order_date=datetime.date.today())

    def test_logged_in_uses_correct_template(self):
        """ Case to test if the view render in the correct template """
        login = self.client.login(username='admin_user', password='camilo123456')
        resp = self.client.get(reverse('order'))

        self.assertEqual(str(resp.context['user']), 'admin_user')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user_order_list.html')

    def test_if_the_view_render_the_correct_admin_context(self):
        """ Case to test if the view render th correct context """

        login = self.client.login(username='admin_user', password='camilo123456')
        resp = self.client.get(reverse('order'))

        expected_orders = Order.objects.filter(order_date__year=datetime.datetime.today().year,
                                               order_date__month=datetime.datetime.today().month,
                                               order_date__day=datetime.datetime.today().day).count()

        self.assertTrue('object_list' in resp.context)
        self.assertEqual(len(resp.context['object_list']), expected_orders)

    def test_if_the_view_render_the_correct_customer_context(self):
        """ Case to test if the view render th correct context """

        login = self.client.login(username='customer_user', password='camilo123456')
        resp = self.client.get(reverse('order'))

        expected_orders = Order.objects.filter(order_date__year=datetime.datetime.today().year,
                                               order_date__month=datetime.datetime.today().month,
                                               order_date__day=datetime.datetime.today().day,
                                               user__username='customer_user').count()

        self.assertTrue('object_list' in resp.context)
        self.assertEqual(len(resp.context['object_list']), expected_orders)


class DeleteOrderViewTest(TestCase):
    """ Test Class to test DeleteOrder View """

    def setUp(self):
        admin_user = User.objects.create_user('admin_user', '', 'camilo123456')
        admin_user.profile.rol = ProfileRoles.ADMINISTRATOR
        admin_user.save()

        customer_user = User.objects.create_user('customer_user', '', 'camilo123456')
        customer_user.profile.rol = ProfileRoles.CUSTOMER
        customer_user.save()

        food = FoodOption.objects.create(name='meat', description='grilled meat')
        menu = Menu.objects.create(name='special meat', menu_date=datetime.date.today())
        menu.food_plate.add(food.id)

        Order.objects.create(user=customer_user, menu=menu, order_suggestion='without sauces', order_date=datetime.date.today())
        Order.objects.create(user=admin_user, menu=menu, order_suggestion='gluten free',
                             order_date=datetime.date.today())

    def text_the_customer_user_only_can_delete_his_orders(self):
        """ Case to test customer only can delete his orders """

        login = self.client.login(username='customer_user', password='camilo123456')

        customer_order = Order.objects.filter(order_date__year=datetime.datetime.today().year,
                                              order_date__month=datetime.datetime.today().month,
                                              order_date__day=datetime.datetime.today().day,
                                              user__username='customer_user')[0]

        resp = self.client.get(reverse('order-delete', kwargs={'pk': customer_order.id}))
        self.assertEqual(resp.status_code, 200)


class CreateOrderViewTest(TestCase):
    """ Test Class to test DeleteOrder View """

    def setUp(self):

        customer_user = User.objects.create_user('customer_user', '', 'camilo123456')
        customer_user.profile.rol = ProfileRoles.CUSTOMER
        customer_user.save()

        food = FoodOption.objects.create(name='meat', description='grilled meat')
        menu = Menu.objects.create(name='special meat', menu_date=datetime.date.today())
        menu.food_plate.add(food.id)

    def test_creation_order(self):
        """ Case test to validate the correct creation instance with view """
        login = self.client.login(username='customer_user', password='camilo123456')
        data = {
            'menu': Menu.objects.all()[0],
            'order_suggestion': 'without sauces',
        }
        resp = self.client.post(reverse('order-create'), data=data)
        self.assertEqual(resp.status_code, 200)


class CreateMenuViewTest(TestCase):
    """ Test Class to test DeleteOrder View """

    def setUp(self):
        admin_user = User.objects.create_user('admin_user', '', 'camilo123456')
        admin_user.profile.rol = ProfileRoles.ADMINISTRATOR
        admin_user.save()
        food = FoodOption.objects.create(name='meat', description='grilled meat')

    def test_creation_menu(self):
        """ Case test to validate the correct creation instance with view """
        login = self.client.login(username='admin_user', password='camilo123456')
        data = {
            'name': 'special meet',
            'order_suggestion': FoodOption.objects.all(),
        }
        resp = self.client.post(reverse('order-create'), data=data)
        self.assertEqual(resp.status_code, 200)
