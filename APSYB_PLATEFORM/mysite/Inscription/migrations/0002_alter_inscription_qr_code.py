# Generated by Django 5.0 on 2024-08-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
    ]
