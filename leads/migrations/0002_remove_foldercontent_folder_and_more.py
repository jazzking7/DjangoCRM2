# Generated by Django 4.2.11 on 2024-06-08 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foldercontent',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='foldercontent',
            name='organisation',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
        migrations.DeleteModel(
            name='FolderContent',
        ),
    ]
