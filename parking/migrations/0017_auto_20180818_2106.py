# Generated by Django 2.1 on 2018-08-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0016_auto_20180818_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='host_income',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='payment_method_info',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]