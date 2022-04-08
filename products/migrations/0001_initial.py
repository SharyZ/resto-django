# Generated by Django 4.0.3 on 2022-04-08 16:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product/images/%Y/%m/%d/')),
                ('small_description', models.TextField(help_text='Description length must not exceed 130', max_length=130)),
                ('price', models.IntegerField(help_text='Price in UZS :)')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category')),
            ],
        ),
    ]
