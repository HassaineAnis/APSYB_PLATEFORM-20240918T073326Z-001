# Generated by Django 5.0 on 2024-08-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='invitation_image',
            field=models.ImageField(blank=True, null=True, upload_to='event_invitations/'),
        ),
    ]
