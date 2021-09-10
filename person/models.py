from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

from person.choices import ProfileRoles
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ProfileRoles.CHOICES)

    class Meta:
        permissions = [
            ('administrator_access', 'Administrator access'),
            ('customer_access', 'Customer access')
        ]

    @property
    def is_administrator(self):
        """ Method return bool if the user is administrator. """
        return self.rol == ProfileRoles.ADMINISTRATOR or self.user.is_staff

    @property
    def is_customer(self):
        """ Method return bool if the user is customer. """
        return self.rol == ProfileRoles.CUSTOMER

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # Add profile permision if not have
        if not self.user.get_all_permissions():
            if self.rol == ProfileRoles.CUSTOMER:
                permission = Permission.objects.filter(name='Customer access')
                self.user.user_permissions.set(permission)
            elif self.rol == ProfileRoles.ADMINISTRATOR:
                permission = Permission.objects.filter(name='Administrator access')
                self.user.user_permissions.set(permission)
        super(Profile, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                  update_fields=update_fields)

