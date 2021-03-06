# Generated by Django 2.0.1 on 2018-01-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_category_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.CharField(choices=[('M', 'Monthly'), ('W', 'Weekly'), ('D', 'Daily')], max_length=7),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=6),
        ),
    ]
