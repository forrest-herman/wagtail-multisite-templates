# Generated by Django 3.2.4 on 2021-06-23 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210623_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='template',
            new_name='page_template',
        ),
    ]