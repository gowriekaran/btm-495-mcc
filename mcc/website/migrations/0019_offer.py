# Generated by Django 3.2.23 on 2023-11-25 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_interview_requestmoreavailability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('candidateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.candidate')),
            ],
        ),
    ]