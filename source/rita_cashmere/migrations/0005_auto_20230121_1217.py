# Generated by Django 3.1.3 on 2023-01-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rita_cashmere', '0004_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_image_one', models.ImageField(upload_to='uploaded_about_image/')),
                ('about_text_one', models.TextField()),
                ('about_image_two', models.ImageField(blank=True, null=True, upload_to='uploaded_about_image/')),
                ('about_text_two', models.TextField()),
                ('about_image_three', models.ImageField(blank=True, null=True, upload_to='uploaded_about_image/')),
                ('about_text_three', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
    ]
