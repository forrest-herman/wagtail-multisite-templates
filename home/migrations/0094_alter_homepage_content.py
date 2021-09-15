# Generated by Django 3.2.4 on 2021-07-06 18:11

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0093_auto_20210706_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('hero_split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your hero title.', required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Add your hero subtitle.', required=False)), ('title_color', wagtail_color_panel.blocks.NativeColorBlock(label='Title Color', required=False)), ('subtitle_color', wagtail_color_panel.blocks.NativeColorBlock(label='Subtitle Color', required=False)), ('hero_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a hero image here', label='Hero Image', required=False)), ('circle_top_color', wagtail_color_panel.blocks.NativeColorBlock(help_text='Choose top circle color. Leave blank for no top circle.', label='Top Circle Color', required=False)), ('circle_bottom_color', wagtail_color_panel.blocks.NativeColorBlock(help_text='Choose bottom circle color. Leave blank for no bottom circle.', label='Bottom Circle Color', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(help_text='Add Button 1 text. Leave blank for no button.', label='Button 1 Text', required=False)), ('btn_link', wagtail.core.blocks.URLBlock(help_text='Where will Button 1 go', label='Button 1 URL', required=False))])), ('testimonials_section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', icon='user', label='Section Title', required=True)), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background Colour')), ('testimonials_container', wagtail.core.blocks.StreamBlock([('testimonial', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add the testimonial.', required=True)), ('author', wagtail.core.blocks.CharBlock(help_text='Add the testimonial author.', required=True))]))]))])), ('services', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', icon='user', label='Section Title', required=True)), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background Colour')), ('services_settings', wagtail.core.blocks.StructBlock([('show_card_bg', wagtail.core.blocks.BooleanBlock(default=False, label='Show Card Background?', required=False)), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Card Background Colour'))])), ('services_container', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Add the card icon class (eg far fa-user).', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add the card text.', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(help_text='Add the card body text.', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='', label='Button Text (Optional)', required=False))]))]))])), ('about_section', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(help_text='', label='Section Title 1', required=False)), ('title_2', wagtail.core.blocks.CharBlock(help_text='', label='Section Title 2', required=False)), ('about_paragraph', wagtail.core.blocks.RichTextBlock(help_text='', required=False)), ('about_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a profile picture here.', label='About Image', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(help_text='', label='Button Text', required=False)), ('btn_link', wagtail.core.blocks.CharBlock(help_text='', label='Button Target URL', required=False)), ('btn_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3')], label='Button Colour')), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background Colour'))])), ('contact_section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', required=True)), ('section_subtitle', wagtail.core.blocks.CharBlock(help_text='Add your section subtitle.', required=False)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='#ffffff')), ('section_bg_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Choose a background image for the section.', label='Choose a background image.', required=False)), ('html_body', wagtail.core.blocks.RawHTMLBlock(help_text='Add the HTML for your contact form.', label='Body HTML', required=False))]))], blank=True, null=True),
        ),
    ]
