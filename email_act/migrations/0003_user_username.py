# Generated by Django 3.1.7 on 2021-04-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_act', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, verbose_name='username'),
        ),
    ]
