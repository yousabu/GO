# Generated by Django 3.1.2 on 2020-10-31 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_post',
            new_name='date_posted',
        ),
    ]
