# Generated by Django 4.1.5 on 2023-02-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apointment',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]