# Generated by Django 3.2.4 on 2021-06-24 00:33

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_homepage_nav_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='footer_text',
            field=wagtail.core.fields.RichTextField(default='DATE_VALUE Proudly Made With Wagtail', help_text='Footer text here. Use "DATE_VALUE" to insert current date.', verbose_name='Footer Text'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='nav_height',
            field=models.IntegerField(default=100, null=True, verbose_name='Navbar Height (px)'),
        ),
    ]
