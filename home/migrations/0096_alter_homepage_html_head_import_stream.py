# Generated by Django 3.2.4 on 2021-07-06 18:33

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0095_alter_homepage_html_head_import_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='html_head_import_stream',
            field=wagtail.core.fields.StreamField([('html_head_link', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.RawHTMLBlock(help_text='Link a font, eg. from Google Fonts.', required=True))])))], blank=True, null=True),
        ),
    ]