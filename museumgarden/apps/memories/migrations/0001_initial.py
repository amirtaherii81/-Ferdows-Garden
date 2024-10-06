# Generated by Django 5.0.4 on 2024-05-14 13:58

import apps.memories.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory_title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('memory_text', models.TextField(verbose_name='متن')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('user_registered', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'خاطره',
                'verbose_name_plural': 'خاطرات',
                'db_table': 't_memory',
            },
        ),
        migrations.CreateModel(
            name='MemoryGalery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory_image_name', models.ImageField(upload_to=apps.memories.models.upload_galery_image, verbose_name='تصویر خاطره')),
                ('memory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='memories.memory')),
            ],
            options={
                'verbose_name': 'تصویر خاطره',
                'verbose_name_plural': 'تصاویر خاطره',
                'db_table': 't_memory_galery',
            },
        ),
        migrations.CreateModel(
            name='MemoryLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='memories.memory')),
                ('user_like', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
