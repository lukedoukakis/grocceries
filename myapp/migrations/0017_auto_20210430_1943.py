# Generated by Django 3.1.7 on 2021-04-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='driver',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='830 N Bruce Ave, Lialto, CA 92830', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0),
        ),
    ]