# Generated by Django 3.2 on 2023-10-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_rename_cover_writer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
