# Generated by Django 3.2.4 on 2021-07-16 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0121_auto_20210716_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='show_hamburger_active_color',
        ),
    ]
