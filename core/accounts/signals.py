from .models import Profile, CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
create a signal to automatically create a Profile model after a CustomUser model is created.
"""
@receiver(post_save, sender= CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)