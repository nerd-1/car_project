# Generated by Django 3.2.5 on 2021-07-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardata',
            name='back_left',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]