# Generated by Django 4.2.7 on 2023-11-05 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_position_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='status',
            field=models.CharField(choices=[('Vacant', 'Vacant'), ('Open', 'Open'), ('Shortlist', 'Shortlist'), ('Interview', 'Interview'), ('Offered', 'Offered'), ('Filled', 'Filled')], default='Vacant', max_length=255),
        ),
    ]