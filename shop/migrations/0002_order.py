# Generated by Django 4.2.1 on 2023-07-02 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='تعداد')),
                ('status', models.CharField(choices=[('ثبت شد', 'ثبت شد'), ('آماده ارسال', 'آماده ارسال')], default='ثبت شد', max_length=20, verbose_name='وضعیت')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.storeproduct', verbose_name='محصول')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='سفارش دهنده')),
            ],
        ),
    ]
