from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=16, blank=True)
    address = models.CharField(max_length=255, blank=True)


class Topping(models.Model):
    name = models.CharField(max_length=55)


class Pizza(models.Model):
    title = models.CharField(max_length=255)
    toppings = models.ManyToManyField(Topping, blank=True, null=True)
