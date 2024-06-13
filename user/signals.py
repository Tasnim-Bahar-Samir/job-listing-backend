# model
from .models import Profile, RegisterUser


# assets
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=RegisterUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)