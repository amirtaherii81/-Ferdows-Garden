# Generated by Django 5.0.4 on 2024-04-20 11:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=250, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=200, verbose_name=' عنوان پیام')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('is_seen', models.BooleanField(default=False, verbose_name='وضعیت مشاهده توسط مدیر')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ثبت پیام')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
                'db_table': 't_message',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100, verbose_name='نام مکان')),
                ('information', models.TextField(default='توضیحات', verbose_name='توضیحات')),
                ('place_image_name', models.ImageField(upload_to='images/places/', verbose_name='تصویر')),
                ('visiting_day', models.CharField(max_length=100, verbose_name='روزهای بازدید')),
                ('visiting_hour', models.CharField(max_length=100, verbose_name='ساعت بازدید')),
                ('rules', models.TextField(verbose_name='قوانین و مقررات')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ و زمان ثبت')),
            ],
            options={
                'verbose_name': 'مکان',
                'verbose_name_plural': 'مکانها',
                'db_table': 't_Places',
            },
        ),
        migrations.CreateModel(
            name='VisitorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, verbose_name='نام نوع بازدید کننده')),
            ],
            options={
                'verbose_name': 'نوع بازدید کننده',
                'verbose_name_plural': 'نوع بازدید کننده ها',
                'db_table': 't_visitor-type',
            },
        ),
        migrations.CreateModel(
            name='TicketPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='بهای بلیط')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='مکان مورد نظر')),
                ('visitor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.visitortype', verbose_name='نوع بازدید کننده')),
            ],
            options={
                'verbose_name': 'قیمت',
                'verbose_name_plural': 'قیمت ها',
                'db_table': 't_ticket_prices',
            },
        ),
    ]
