# Generated by Django 2.2 on 2022-01-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0005_auto_20220122_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='emp_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emp',
            name='occup',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
