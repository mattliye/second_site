# Generated by Django 2.2.3 on 2019-07-17 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190717_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
    ]