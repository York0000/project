# Generated by Django 3.2.4 on 2021-06-16 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210616_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
    ]
