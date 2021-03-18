# Generated by Django 3.1.7 on 2021-03-18 04:30

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]