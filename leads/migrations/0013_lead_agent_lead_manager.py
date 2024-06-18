# Generated by Django 4.2.11 on 2024-06-18 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_userrelation_remove_manager_organisation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_leads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lead',
            name='manager',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager_leads', to=settings.AUTH_USER_MODEL),
        ),
    ]
