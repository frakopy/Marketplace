from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        user = get_object_or_404(User, id=instance.id)
        print(f"User with the username {user.username} has been created")
