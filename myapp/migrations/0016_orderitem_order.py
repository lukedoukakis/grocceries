# Generated by Django 3.1.7 on 2021-04-30 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order'),
        ),
    ]
