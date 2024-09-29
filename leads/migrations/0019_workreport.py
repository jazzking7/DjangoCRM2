# Generated by Django 4.2.11 on 2024-09-28 18:36

from django.db import migrations, models
import django.db.models.deletion
import leads.models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0018_rename_shared_commission_lead_co_commission'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='work_report', max_length=500)),
                ('file', models.FileField(blank=True, null=True, upload_to=leads.models.handle_upload_work_report)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile')),
            ],
        ),
    ]
