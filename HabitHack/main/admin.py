from django.contrib import admin
from .models import UserProfile, UserHabit, HabitHistory

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserHabit)
admin.site.register(HabitHistory)
