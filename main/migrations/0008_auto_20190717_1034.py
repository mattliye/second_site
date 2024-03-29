# Generated by Django 2.2.3 on 2019-07-17 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190717_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.TutorialCategory', verbose_name='Category'),
        ),
    ]
