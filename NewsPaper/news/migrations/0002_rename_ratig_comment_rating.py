# Generated by Django 4.1.7 on 2023-02-16 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='ratig',
            new_name='rating',
        ),
    ]