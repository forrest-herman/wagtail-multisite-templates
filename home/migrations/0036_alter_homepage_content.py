# Generated by Django 3.2.4 on 2021-06-25 14:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20210625_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('hero_split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RichTextBlock(help_text='Add your hero title.', required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Add your hero subtitle.', required=False)), ('title_color', wagtail_color_panel.blocks.NativeColorBlock(label='Title Color', required=False)), ('subtitle_color', wagtail_color_panel.blocks.NativeColorBlock(label='Subtitle Color', required=False)), ('subtitle_class', wagtail.core.blocks.CharBlock(help_text='Add a hero subtitle CSS class.', required=False)), ('hero_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a hero image here', label='Hero Image', required=False)), ('circle_top_color', wagtail_color_panel.blocks.NativeColorBlock(help_text='Choose top circle color. Leave blank for no top circle.', label='Top Circle Color', required=False)), ('circle_bottom_color', wagtail_color_panel.blocks.NativeColorBlock(help_text='Choose bottom circle color. Leave blank for no bottom circle.', label='Bottom Circle Color', required=False)), ('button_1_text', wagtail.core.blocks.CharBlock(help_text='Add Button 1 text. Leave blank for no button.', label='Button 1 Text', required=False)), ('button_1_url', wagtail.core.blocks.URLBlock(help_text='Where will Button 1 go', label='Button 1 URL', required=False))])), ('testimonials_section', wagtail.core.blocks.StructBlock([('testimonials_settings', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', icon='user', label='Section Title', required=True)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='', required=False))])), ('testimonials_container', wagtail.core.blocks.StreamBlock([('testimonial', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add the testimonial.', required=True)), ('author', wagtail.core.blocks.CharBlock(help_text='Add the testimonial author.', required=True))]))]))])), ('services', wagtail.core.blocks.StructBlock([('services_settings', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', icon='user', label='Section Title', required=True)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='#ffffff')), ('card_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='#ffffff'))])), ('services_container', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Add the card icon.', required=False)), ('text', wagtail.core.blocks.CharBlock(help_text='Add the card text.', required=False)), ('ptext', wagtail.core.blocks.CharBlock(help_text='Add the card body text.', required=False))]))]))])), ('about_section', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(help_text='Add your 1st title.', required=False)), ('title_2', wagtail.core.blocks.CharBlock(help_text='Add your 2nd title.', required=False)), ('about_paragraph', wagtail.core.blocks.RichTextBlock(help_text='Add your paragraphs.', required=False)), ('about_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a picture of you here', label='About Image', required=False)), ('button_1_text', wagtail.core.blocks.CharBlock(help_text='Add Button 1 text.', label='Button 1 Text', required=False)), ('button_1_url', wagtail.core.blocks.CharBlock(help_text='Where will Button 1 go', label='Button 1 URL', required=False)), ('section_bg_color', wagtail.core.blocks.CharBlock(help_text='Choose a background color for the section.', required=False))])), ('contact_section', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', required=True)), ('section_subtitle', wagtail.core.blocks.CharBlock(help_text='Add your section subtitle.', required=False)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='#ffffff')), ('section_bg_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Choose a background image for the section.', label='Choose a background image.', required=False)), ('html_body', wagtail.core.blocks.RawHTMLBlock(help_text='Add the HTML for your contact form.', label='Body HTML', required=False))])), ('classic_hero', wagtail.core.blocks.StructBlock([('hero_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a hero image here', label='Hero Image', required=False))])), ('classic_sub_hero', wagtail.core.blocks.StructBlock([])), ('classic_site_intro', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(default='Section Title', help_text='Add your section title.', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(default='Section Paragraph', help_text='Add your section title.', required=True)), ('fit_below_sub_hero_TRUE', wagtail.core.blocks.BooleanBlock(default=False, label='Remove top padding to fit below hero?', required=False))])), ('classic_three_cards', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(default='3 Cards Section Title', help_text='Add your section title.', required=False))])), ('classic_text_and_btn', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(default='Questions?', help_text='Add your section title.', required=False))])), ('classic_img_text_split', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(default="Don't wait. Start saving!", help_text='Add your section title.', required=False)), ('half_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload an image here', label='Split Image', required=True)), ('img_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Image Position'))])), ('classic_newsletter_split', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(default='Title Here', help_text='Add your section title.', required=False)), ('section_paragraph', wagtail.core.blocks.CharBlock(default='Subtitle', help_text='Add your section title.', required=False)), ('half_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload an image here', label='Split Image', required=True)), ('img_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Image Position'))])), ('classic_contact_form', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(default='Get in touch', help_text='Add your section title.', required=False)), ('half_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload an image here', label='Split Image', required=True)), ('img_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Image Position'))])), ('classic_testimonials_carousel', wagtail.core.blocks.StructBlock([('testimonials_settings', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', icon='user', label='Section Title', required=True)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='', required=False))])), ('testimonials_container', wagtail.core.blocks.StreamBlock([('testimonial', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add the testimonial.', required=True)), ('author', wagtail.core.blocks.CharBlock(help_text='Add the testimonial author.', required=True))]))]))]))], blank=True, null=True),
        ),
    ]
