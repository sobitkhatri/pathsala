# Generated by Django 2.1.2 on 2018-10-29 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20181029_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]