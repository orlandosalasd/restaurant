from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from person.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Method to create a Profile instance when new user is created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Method to call save method from profile instance
    when save in User instance.
    """
    instance.profile.save()
