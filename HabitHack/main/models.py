from django.db import models

# Create your models here.

# This is our first model
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # ...

    # TODO:
    #   specify all fields and their constraints,
    #   add __str__ method
