# Generated by Django 5.0.4 on 2024-05-16 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0002_rename_memorygalery_memorygallery'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='memorylike',
            table='t_MemoryLike',
        ),
    ]
