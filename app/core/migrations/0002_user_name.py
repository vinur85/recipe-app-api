# Generated by Django 4.0.10 on 2024-01-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='AB CD', max_length=255),
        ),
    ]