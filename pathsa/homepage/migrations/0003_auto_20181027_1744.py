# Generated by Django 2.1.2 on 2018-10-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20181027_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmodula2',
            name='Contact_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adminmodula2',
            name='Principal_Phone_NO',
            field=models.CharField(max_length=100),
        ),
    ]
