# Generated by Django 4.1.4 on 2023-01-01 15:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_like_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]