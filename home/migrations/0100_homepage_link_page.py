# Generated by Django 3.2.4 on 2021-07-06 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('home', '0099_auto_20210706_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page', verbose_name='Link to an internal page'),
        ),
    ]
