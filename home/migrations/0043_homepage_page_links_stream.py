# Generated by Django 3.2.4 on 2021-06-25 22:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_alter_homepage_social_links_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='page_links_stream',
            field=wagtail.core.fields.StreamField([('url_link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock(help_text='Destination URL', label='Link URL', required=True)), ('link_text', wagtail.core.blocks.CharBlock(help_text='', label='Display Text', required=True))]))], blank=True, null=True, verbose_name='Page Quick Links'),
        ),
    ]
