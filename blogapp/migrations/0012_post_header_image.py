# Generated by Django 5.0 on 2023-12-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_alter_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
