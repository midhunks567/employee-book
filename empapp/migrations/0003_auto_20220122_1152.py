# Generated by Django 2.2 on 2022-01-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_auto_20220122_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
