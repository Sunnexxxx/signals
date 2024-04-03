from .models import Profile, Pizza, Topping
from django.contrib.auth.models import User
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         print('Created')
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print('Updated')
#     instance.profile.save()

@receiver(m2m_changed, sender=Pizza.toppings.through)
def topping_changed(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        print('Added')
    if action == 'post_remove':
        print('Removed')
    if action == 'post_clear':
        print('Cleaned')
