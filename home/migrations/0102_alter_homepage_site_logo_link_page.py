# Generated by Django 3.2.4 on 2021-07-06 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('home', '0101_rename_link_page_homepage_site_logo_link_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='site_logo_link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page', verbose_name='Site Logo Link to an internal page'),
        ),
    ]
