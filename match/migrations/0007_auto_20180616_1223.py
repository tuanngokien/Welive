# Generated by Django 2.0.6 on 2018-06-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0006_auto_20180616_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='awayteam_score',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='match',
            name='hometeam_score',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('', 'Chưa bắt đầu'), ('FT', 'Hết giờ'), ('HT', 'Hết hiệp 1'), ('{}', 'Đang thi đấu')], max_length=3),
        ),
    ]