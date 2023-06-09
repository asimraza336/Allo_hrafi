# Generated by Django 3.2 on 2023-05-01 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_service_serviceimage'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_phone_verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
