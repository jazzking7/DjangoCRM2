# Generated by Django 4.2.11 on 2024-09-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0016_teammember_unique_team_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='shared_commission',
            field=models.IntegerField(default=0),
        ),
    ]
