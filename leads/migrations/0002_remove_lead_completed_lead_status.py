# Generated by Django 4.2.11 on 2024-05-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='completed',
        ),
        migrations.AddField(
            model_name='lead',
            name='status',
            field=models.CharField(blank=True, choices=[('进行中', '进行中'), ('已完成', '已完成'), ('待跟进', '待跟进'), ('取消', '取消')], max_length=20, null=True),
        ),
    ]
