# Generated by Django 3.2.4 on 2021-07-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0110_homepage_show_hamburger_active_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='footer_logo_max_size',
            field=models.IntegerField(blank=True, default=200, null=True, verbose_name='Footer Logo Max Width (px)'),
        ),
    ]
