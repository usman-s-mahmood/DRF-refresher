# Generated by Django 5.1.6 on 2025-03-03 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color_detail', to='home.color'),
        ),
    ]
