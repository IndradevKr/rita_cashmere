# Generated by Django 3.1.3 on 2023-01-19 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rita_cashmere', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
