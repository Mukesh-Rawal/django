# Generated by Django 5.0.1 on 2024-05-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news_pics/'),
        ),
    ]
