# Generated by Django 2.1.2 on 2018-10-29 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20181030_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL),
        ),
    ]