# Generated by Django 2.2.3 on 2019-07-17 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190717_1143'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TutorialCategory',
        ),
        migrations.DeleteModel(
            name='TutorialSeries',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_slug',
        ),
    ]