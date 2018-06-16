# Generated by Django 2.0.6 on 2018-06-15 16:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('league', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('hometeam_score', models.PositiveIntegerField()),
                ('awayteam_score', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('', 'Chưa bắt đầu'), ('FT', 'Hết giờ'), ('HT', 'Hết hiệp'), ('{}', 'Đang thi đấu')], max_length=3)),
                ('awayteam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='team.Team')),
                ('hometeam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='team.Team')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.League')),
            ],
        ),
        migrations.CreateModel(
            name='MatchEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=15)),
                ('time', models.PositiveIntegerField()),
                ('player_name', models.TextField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.Match')),
            ],
        ),
        migrations.CreateModel(
            name='MatchStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=2)),
                ('value', models.FloatField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.Match')),
            ],
        ),
    ]