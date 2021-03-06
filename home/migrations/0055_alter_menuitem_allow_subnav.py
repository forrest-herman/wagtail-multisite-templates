# Generated by Django 3.2.4 on 2021-06-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_alter_menuitem_open_in_new_tab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='allow_subnav',
            field=models.BooleanField(default=False, help_text="NOTE: The sub-menu might not be displayed, even if checked. It depends on how the menu is used in this project's templates.", verbose_name='Allow sub-menu for this item'),
        ),
    ]
