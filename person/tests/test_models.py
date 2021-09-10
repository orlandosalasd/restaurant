from django.test import TestCase
from django.contrib.auth.models import User
from person.choices import ProfileRoles


class ProfileModelTest(TestCase):
    """ Test class to test Profile model and methods """

    @classmethod
    def setUpTestData(cls):
        admin_user = User.objects.create_user('admin_user', '', 'camilo123456')
        admin_user.profile.rol = ProfileRoles.ADMINISTRATOR
        admin_user.save()

        customer_user = User.objects.create_user('customer_user', '', 'camilo123456')
        customer_user.profile.rol = ProfileRoles.CUSTOMER
        customer_user.save()

    def test_is_administrator_method_return_true_from_profiles_roles_administrator(self):
        """ Case to test the is_administrator method with @property decorator to validate if the user is admin rol"""
        admin_profile = User.objects.get(username='admin_user').profile
        self.assertTrue(admin_profile.is_administrator)

    def test_is_customer_method_return_true_from_profiles_roles_customer(self):
        """ Case to test the is_customer method with @property decorator to validate if the user is customer rol"""
        customer_profile = User.objects.get(username='customer_user').profile
        self.assertTrue(customer_profile.is_customer)

    def test_after_save_the_admin_user_rol_must_have_admin_access_permission(self):
        """
        Case to test the save method, before save if the user have admin rol,
        must have the admin access permission
        """
        admin_user = User.objects.get(username='admin_user')
        self.assertTrue('person.administrator_access' in admin_user.get_all_permissions())

    def test_after_save_the_customer_user_rol_must_have_customer_access_permission(self):
        """
        Case to test the save method, before save if the user have admin rol,
        must have the admin access permission
        """
        customer_user = User.objects.get(username='customer_user')
        self.assertTrue('person.customer_access' in customer_user.get_all_permissions())

