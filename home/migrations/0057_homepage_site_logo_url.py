# Generated by Django 3.2.4 on 2021-06-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_fontimport'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='site_logo_url',
            field=models.CharField(blank=True, max_length=255, verbose_name='Site Logo URL (Optional)'),
        ),
    ]
