# Generated by Django 2.0.6 on 2018-06-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0009_auto_20180616_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ('date', 'time')},
        ),
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='matchevent',
            name='time',
            field=models.CharField(max_length=8),
        ),
    ]
