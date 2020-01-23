# Generated by Django 3.0.2 on 2020-01-23 16:48

import dashboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=240)),
                ('slug', models.SlugField(default='', unique=True)),
                ('question', dashboard.models.RichTextBleachField()),
                ('input_type', models.CharField(max_length=240)),
                ('data_answer', models.TextField(blank=True, null=True)),
                ('data_logic', models.TextField(blank=True, null=True)),
                ('new_node', models.BooleanField()),
                ('start_node', models.BooleanField()),
                ('end_node', models.BooleanField()),
                ('decision_tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.DecisionTree')),
            ],
        ),
    ]
