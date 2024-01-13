# Generated by Django 3.2.23 on 2024-01-10 11:56

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('church', 'Church'), ('town_hall', 'Town Hall'), ('venue', 'Venue'), ('other', 'Other')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Memories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memories_posts', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.locations')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
