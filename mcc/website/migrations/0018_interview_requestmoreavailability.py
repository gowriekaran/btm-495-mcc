# Generated by Django 4.2.7 on 2023-11-25 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_remove_interview_datetime_alter_interview_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='requestMoreAvailability',
            field=models.BooleanField(default=False),
        ),
    ]
