# Generated by Django 2.2.3 on 2019-07-17 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190717_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category'),
        ),
    ]