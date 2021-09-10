from django.test import TestCase
from django.contrib.auth.models import User
from person.choices import ProfileRoles
from django.urls import reverse


class SignUpViewTest(TestCase):
    """ Test Class to test SignUp View """

    def setUp(self):
        admin_user = User.objects.create_user('test_user', '', 'camilo123456')
        admin_user.profile.rol = ProfileRoles.ADMINISTRATOR
        admin_user.save()

    def test_user_creation(self):
        """ Case test to validate the correct creation instance with view """
        login = self.client.login(username='test_user', password='camilo123456')
        data = {
            'first_name': 'laura',
            'last_name': 'perez',
            'email': 'laura@dominio.com',
            'username': 'lauraperez',
            'password1': 'lp123456',
            'password2': 'lp123456',
            'rol': ProfileRoles.CUSTOMER,
        }
        resp = self.client.post(reverse('singup'), data=data)
        self.assertEqual(resp.status_code, 302)
