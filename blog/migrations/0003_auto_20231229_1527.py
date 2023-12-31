# Generated by Django 3.2.23 on 2023-12-29 15:27

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20231206_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memories',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memories_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='memories',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
