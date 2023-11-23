# Generated by Django 4.2.7 on 2023-11-23 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_candidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField()),
                ('location', models.TextField()),
                ('feedback', models.TextField()),
                ('status', models.TextField()),
                ('candidateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.candidate')),
            ],
        ),
    ]
