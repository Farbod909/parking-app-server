# Generated by Django 2.1 on 2018-09-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180902_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='phone number'),
        ),
    ]
