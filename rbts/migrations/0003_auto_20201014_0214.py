# Generated by Django 3.1.2 on 2020-10-14 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbts', '0002_redditcredential_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditcredential',
            name='date_added',
            field=models.DateTimeField(auto_created=True, verbose_name='Date added'),
        ),
    ]
