# Generated by Django 3.2.9 on 2021-12-30 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='blog',
            new_name='post',
        ),
    ]
