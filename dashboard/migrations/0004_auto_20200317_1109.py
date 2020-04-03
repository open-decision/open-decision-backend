# Generated by Django 3.0.3 on 2020-03-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_node_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='text',
            new_name='question',
        ),
        migrations.AddField(
            model_name='node',
            name='extra_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]