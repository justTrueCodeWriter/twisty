# Generated by Django 4.2.3 on 2023-07-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_post_changed_post_created_post_karma_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes_count',
            field=models.IntegerField(default=0),
        ),
    ]