# Generated by Django 3.2.23 on 2023-11-06 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('selectedPositionID', models.IntegerField()),
                ('experience', models.TextField()),
                ('dateSubmitted', models.DateTimeField(auto_now_add=True)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.student')),
            ],
        ),
    ]
