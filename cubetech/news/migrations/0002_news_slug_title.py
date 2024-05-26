# Generated by Django 5.0.1 on 2024-05-24 10:37

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug_title',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='news_title', unique=True),
        ),
    ]
