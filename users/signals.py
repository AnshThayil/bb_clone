from django.contrib.auth.models import User
from boulders.models import Sender
from users.models import Profile
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance, grade_format_font = True)

@receiver(post_save, sender=Sender)
def add_points(sender, instance, created, **kwargs):
    if created:
        try:
            profile = Profile.objects.get(user  = instance.sender)
            profile.points += instance.boulder.grade
            if instance.flash:
                profile.points += 1
            profile.save()
        except:
            pass

@receiver(pre_delete, sender=Sender)
def remove_points(sender, instance, using, **kwargs):
    try:
        profile = Profile.objects.get(user = instance.sender)
        profile.points -= instance.boulder.grade
        if instance.flash:
            profile.points -= 1
        profile.save()
    except:
        pass
