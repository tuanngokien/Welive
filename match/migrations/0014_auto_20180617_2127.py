# Generated by Django 2.0.6 on 2018-06-17 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0013_auto_20180617_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='status',
            new_name='progress',
        ),
    ]