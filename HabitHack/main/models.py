from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)
    # -- Do we really need them? --
    birth_date = models.DateField(blank=True, null=True)
    gender_choice = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=6, choices=gender_choice, blank=True)
    # -----------------------------
    profile_photo = models.ImageField(upload_to='profile_images', default='profile_images/default_profile_photo.jpg')
    description = models.CharField(max_length=500, default='', blank=True)

    def __str__(self):
        return self.user.username


class UserHabit(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', blank=False)
    description = models.CharField(max_length=500, default='', blank=True)
    weekdays = models.CharField(max_length=30, default='', blank=False)
    num_repeats = models.PositiveIntegerField(default=1, blank=False)

    def __str__(self):
        return str(self.user) + ': ' + self.name

class HabitHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user_habit = models.ForeignKey(UserHabit, on_delete=models.CASCADE)
    datehash = models.CharField(max_length=10, default='1970-01-01', blank=False)
    counter = models.PositiveIntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.user_habit) + ' - ' + self.datehash

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])




