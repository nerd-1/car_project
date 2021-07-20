# Generated by Django 3.2.5 on 2021-07-12 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20210712_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardata',
            old_name='id',
            new_name='car_id',
        ),
        migrations.RenameField(
            model_name='cardatarecord',
            old_name='id',
            new_name='car_id',
        ),
        migrations.AddField(
            model_name='cardatarecord',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]