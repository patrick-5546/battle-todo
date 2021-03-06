# Generated by Django 3.1.1 on 2021-01-10 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='damage_dealt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='has_attacked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='todo_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='physical_attack',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='physical_defense',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='special_attack',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='special_defense',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='speed',
            field=models.IntegerField(default=1),
        ),
    ]
