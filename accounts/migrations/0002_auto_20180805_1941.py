# Generated by Django 2.1 on 2018-08-06 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer'),
        ),
        migrations.AddField(
            model_name='host',
            name='venmo_email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='host',
            name='venmo_phone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
