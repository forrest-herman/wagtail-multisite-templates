# Generated by Django 3.2.4 on 2021-07-07 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0109_alter_childpage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='show_hamburger_active_color',
            field=models.BooleanField(blank=True, default=True, verbose_name='Show Hamburger Icon Colour When Active?'),
        ),
    ]
