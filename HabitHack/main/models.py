from django.db import models

# Create your models here.

# This is our first model


class User(models.Model):
    username = models.OneToOneField(Credentials, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    age = models.IntegerField()
    gender_choice = (('MALE', 'M'), ('FEMALE', 'F'))
    gender = models.CharField(max_length=1, choices=gender_choice)


class Credentials(models.Model):
    username = models.CharField(max_length=20, primary_key=True, unique=True)
    password = models.CharField(max_length=20)

