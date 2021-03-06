# Generated by Django 3.2.4 on 2021-07-01 15:01

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_auto_20210701_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='nav_text_color',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='', max_length=7, verbose_name='Navbar Menu Item Colour'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='nav_text_color_hover',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='', max_length=7, verbose_name='Navbar Menu Item Hover Colour (Optional)'),
        ),
    ]
