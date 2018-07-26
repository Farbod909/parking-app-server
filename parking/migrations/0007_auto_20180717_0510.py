# Generated by Django 2.0.7 on 2018-07-17 05:10

from django.db import migrations, models
import parking.fields


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0006_auto_20180717_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='features',
            field=parking.fields.ChoiceArrayField(base_field=models.CharField(choices=[('EV Charging', 'EV Charging'), ('Illuminated', 'Illuminated'), ('Covered', 'Covered'), ('Guarded', 'Guarded'), ('Surveillance', 'Surveillance'), ('Gated', 'Gated')], max_length=50), blank=True, help_text='A list of features e.g. EV charging, Illuminated, etc.', size=None),
        ),
    ]