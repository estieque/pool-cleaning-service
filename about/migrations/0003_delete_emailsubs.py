# Generated by Django 4.1.5 on 2023-02-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_email_emailsubs_n_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailSubs',
        ),
    ]