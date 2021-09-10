from datetime import datetime
import os
from django.template.loader import get_template
from sesame.utils import get_query_string
from restaurant.celery import app
from django.contrib.auth.models import User
from menu.models import Menu
from person.choices import ProfileRoles
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@app.task()
def send_today_menu_options():
    """
    This task send email for all customer user profile rol the all today menus options.
    """
    customers_users = User.objects.filter(profile__rol=ProfileRoles.CUSTOMER)
    today_menu_options = Menu.objects.filter(menu_date__year=datetime.today().year,
                                             menu_date__month=datetime.today().month,
                                             menu_date__day=datetime.today().day)
    subject = "Nora's Restaurant - Today Menu Options"
    template = get_template('send_today_menu_options.html')
    for customer in customers_users:

        content = template.render({
            'user': customer,
            'today_menu_options': today_menu_options,
            # join the base of site project, the create new order view url and the user key to loin access with sesame.
            'take_order_link': os.path.join(settings.SITE_URL, 'menu/order/create/', get_query_string(customer))
        })
        message = EmailMultiAlternatives(subject, "Nora's Restaurant", settings.EMAIL_HOST_USER, [customer.email])
        message.attach_alternative(content, 'text/html')
        message.send()
