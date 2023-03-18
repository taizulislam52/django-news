# Generated by Django 4.1.7 on 2023-03-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_post_features_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.CharField(blank=True, choices=[('Popular', 'Popular'), ('Trending', 'Trending'), ('Most View', 'Most View')], max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='features_image',
            field=models.ImageField(blank=True, upload_to='news'),
        ),
    ]
