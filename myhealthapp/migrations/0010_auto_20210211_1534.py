# Generated by Django 3.1.5 on 2021-02-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhealthapp', '0009_auto_20210211_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='go_to_bed',
            field=models.TimeField(verbose_name='go_to_bed'),
        ),
        migrations.AlterField(
            model_name='list',
            name='wakeup',
            field=models.TimeField(verbose_name='wakeup'),
        ),
    ]