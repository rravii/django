# Generated by Django 3.0.5 on 2020-04-15 08:11

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salespost',
            name='contact',
            field=phone_field.models.PhoneField(blank=True, max_length=10),
        ),
    ]
