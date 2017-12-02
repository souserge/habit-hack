# from django.db import models
#
# # Create your models here.
# class Credentials(models.Model):
#     username = models.CharField(max_length=20, primary_key=True, unique=True)
#     password = models.CharField(max_length=20)
#
# class User(models.Model):
#     username = models.OneToOneField(Credentials, on_delete=models.CASCADE, primary_key=True)
#     name = models.CharField(max_length=40)
#     email = models.CharField(max_length=50)
#     city = models.CharField(max_length=20)
#     country = models.CharField(max_length=20)
#     age = models.IntegerField()
#     gender_choice = (('MALE', 'M'), ('FEMALE', 'F'))
#     gender = models.CharField(max_length=1, choices=gender_choice)
#
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    age = models.IntegerField()
    gender_choice = (('MALE', 'M'), ('FEMALE', 'F'))
    gender = models.CharField(max_length=1, choices=gender_choice)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

#DO NOT DELETE IT'S IMPORTANT, BUT WE HAVE TO WAIT FOR FURTHER DEVELOPING PROCESS :)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.UserProfile.save()




