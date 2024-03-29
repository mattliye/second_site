# Generated by Django 2.2.3 on 2019-07-17 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190717_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_published',
            new_name='tutorial_publish',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category'),
        ),
    ]
