# Generated by Django 4.1.7 on 2023-02-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_features_image_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='features_image',
            field=models.ImageField(blank=True, default='static/src/images/placeholder-image.png', upload_to='static/src/images'),
        ),
    ]
