# Generated by Django 3.2.4 on 2021-07-05 21:20

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0083_menuitem_nav_button_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('hero_split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your hero title.', required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Add your hero subtitle.', required=False)), ('title_color', wagtail_color_panel.blocks.NativeColorBlock(label='Title Color', required=False)), ('subtitle_color', wagtail_color_panel.blocks.NativeColorBlock(label='Subtitle Color', required=False)), ('hero_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a hero image here', label='Hero Image', required=False)), ('circle_top_color', wagtail_color_panel.blocks.NativeColorBlock(help_text='Choose top circle color. Leave blank for no top circle.', label='Top Circle Color', required=False)), ('circle_bottom_color', wagtail_color_panel.blocks.NativeColorBlock(help_text='Choose bottom circle color. Leave blank for no bottom circle.', label='Bottom Circle Color', required=False)), ('button_1_text', wagtail.core.blocks.CharBlock(help_text='Add Button 1 text. Leave blank for no button.', label='Button 1 Text', required=False)), ('button_1_url', wagtail.core.blocks.URLBlock(help_text='Where will Button 1 go', label='Button 1 URL', required=False))])), ('testimonials_section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', icon='user', label='Section Title', required=True)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='', required=False)), ('testimonials_container', wagtail.core.blocks.StreamBlock([('testimonial', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add the testimonial.', required=True)), ('author', wagtail.core.blocks.CharBlock(help_text='Add the testimonial author.', required=True))]))]))])), ('services', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', icon='user', label='Section Title', required=True)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='#ffffff')), ('card_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='#ffffff')), ('services_container', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Add the card icon class (eg far fa-user).', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add the card text.', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(help_text='Add the card body text.', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='', label='Button Text (Optional)', required=False))]))]))])), ('about_section', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(help_text='Add your 1st title.', required=False)), ('title_2', wagtail.core.blocks.CharBlock(help_text='Add your 2nd title.', required=False)), ('about_paragraph', wagtail.core.blocks.RichTextBlock(help_text='Add your paragraphs.', required=False)), ('about_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a picture of you here', label='About Image', required=False)), ('button_1_text', wagtail.core.blocks.CharBlock(help_text='Add Button 1 text.', label='Button 1 Text', required=False)), ('button_1_url', wagtail.core.blocks.CharBlock(help_text='Where will Button 1 go', label='Button 1 URL', required=False)), ('section_bg_color', wagtail.core.blocks.CharBlock(help_text='Choose a background color for the section.', required=False))])), ('contact_section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', required=True)), ('section_subtitle', wagtail.core.blocks.CharBlock(help_text='Add your section subtitle.', required=False)), ('section_bg_color', wagtail_color_panel.blocks.NativeColorBlock(default='#ffffff')), ('section_bg_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Choose a background image for the section.', label='Choose a background image.', required=False)), ('html_body', wagtail.core.blocks.RawHTMLBlock(help_text='Add the HTML for your contact form.', label='Body HTML', required=False))])), ('classic_hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='', help_text='', label='Hero Title', required=True)), ('subtitle', wagtail.core.blocks.CharBlock(default='', help_text='', label='Hero Subtitle', required=True)), ('btn_text', wagtail.core.blocks.CharBlock(default='Contact me', label='Hero Button (Optional)', required=False)), ('hero_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload your image here', label='Full Hero Image', required=False))])), ('classic_sub_hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Section Title', help_text='', label='Section Header', required=True)), ('paragraph', wagtail.core.blocks.CharBlock(default='', label='Section Paragraph', required=False)), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background')), ('services_container', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Add the card icon class (eg far fa-user).', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add the card text.', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(help_text='Add the card body text.', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='', label='Button Text (Optional)', required=False))]))], label='Add a few cards here (optional)', required=False))])), ('classic_site_intro', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Section Title', help_text='', label='Section Header', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(default='', label='Section Paragraph', required=True)), ('fit_below_sub_hero_TRUE', wagtail.core.blocks.BooleanBlock(default=False, label='Remove top padding to fit below hero?', required=False))])), ('classic_three_cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Section Title', help_text='', label='Section Header', required=False)), ('services_container', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Add the card icon class (eg far fa-user).', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add the card text.', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(help_text='Add the card body text.', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='', label='Button Text (Optional)', required=False))]))], required=True)), ('show_card_bg', wagtail.core.blocks.BooleanBlock(default=True, label='Show Card Background?', required=False)), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background'))])), ('classic_text_and_btn', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Questions?', help_text='Add your section title.', label='Section Header', required=True)), ('paragraph', wagtail.core.blocks.CharBlock(default='', label='Section Paragraph', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='', label='Button Text (Optional)', required=True))])), ('classic_img_text_split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default="Don't wait. Start saving!", help_text='Add your section title.', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='Contact me', label='Button Text', required=False)), ('half_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload an image here', label='Split Image', required=True)), ('img_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Image Position')), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background'))])), ('classic_newsletter_split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Title Here', help_text='Add your section title.', required=False)), ('section_paragraph', wagtail.core.blocks.CharBlock(default='Subtitle', help_text='Add your section title.', required=False)), ('half_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload an image here', label='Split Image', required=True)), ('img_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Image Position')), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background'))])), ('classic_contact_form', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Get in touch', help_text='Add your section title.', required=False)), ('half_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload an image here', label='Split Image', required=True)), ('img_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Image Position')), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background'))])), ('classic_testimonials_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your section title.', label='Section Title', required=True)), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Section Background')), ('testimonials_container', wagtail.core.blocks.StreamBlock([('testimonial', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add the testimonial.', required=True)), ('author', wagtail.core.blocks.CharBlock(help_text='Add the testimonial author.', required=True))]))]))])), ('modern_hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='', help_text='', label='Hero Title', required=False)), ('subtitle', wagtail.core.blocks.CharBlock(default='', help_text='', label='Hero Subtitle', required=False)), ('hero_image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload your image here', label='Full Hero Image', required=False))])), ('modern_text_section', wagtail.core.blocks.StructBlock([('title1', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 1 (Optional)', required=False)), ('title2', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 2 (Optional)', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(default='', label='Section Paragraph', required=False)), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('text-start', 'Left'), ('text-center', 'Center'), ('text-end', 'Right')], label='Text Align'))])), ('modern_cards', wagtail.core.blocks.StructBlock([('title1', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 1 (Optional)', required=False)), ('title2', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 2 (Optional)', required=False)), ('long_title_TRUE', wagtail.core.blocks.BooleanBlock(default=False, label='Long title (Multiline)?', required=False)), ('services_container', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Add the card icon class (eg far fa-user).', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add the card text.', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(help_text='Add the card body text.', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='', label='Button Text (Optional)', required=False))]))], required=True))])), ('modern_quote', wagtail.core.blocks.StructBlock([('title1', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 1 (Optional)', required=False)), ('title2', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 2 (Optional)', required=False)), ('long_title_TRUE', wagtail.core.blocks.BooleanBlock(default=False, label='Long title (Multiline)?', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(default='', label='Quote Paragraph', required=True)), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('text-start', 'Left'), ('text-center', 'Center'), ('text-end', 'Right')], label='Text Align')), ('btn_text', wagtail.core.blocks.CharBlock(default='', help_text='Optional button. Leave blank to hide button.', label='Button Text', required=False)), ('btn_link', wagtail.core.blocks.CharBlock(default='', help_text='', label='Button Link', required=False)), ('btn_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Button Align')), ('btn_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3')], label='Button Colour'))])), ('modern_text_img_block', wagtail.core.blocks.StructBlock([('paragraph', wagtail.core.blocks.CharBlock(default='', label='Paragraph Text', required=True)), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('text-start', 'Left'), ('text-center', 'Center'), ('text-end', 'Right')], label='Text Align')), ('img', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload an image here. Alternatively leave blank for a simple text block.', label='Image Selector (Optional)', required=False)), ('img_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Image Position')), ('img_max_width', wagtail.core.blocks.IntegerBlock(default='450', label='Max Image Width (px)', required=True))])), ('modern_img_bg_section', wagtail.core.blocks.StructBlock([('title1', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 1 (Optional)', required=False)), ('title2', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 2 (Optional)', required=False)), ('long_title_TRUE', wagtail.core.blocks.BooleanBlock(default=False, label='Long title (Multiline)?', required=False)), ('paragraph', wagtail.core.blocks.CharBlock(default='', label='Paragraph', required=True)), ('text_align', wagtail.core.blocks.ChoiceBlock(choices=[('text-start', 'Left'), ('text-center', 'Center'), ('text-end', 'Right')], label='Text Align')), ('bg_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3'), ('default', 'Theme Default Background')], label='Card Background Colour')), ('bg_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='', label='Background Image', required=True)), ('content_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Content Align')), ('btn_text', wagtail.core.blocks.CharBlock(default='', help_text='Optional button. Leave blank to hide button.', label='Button Text', required=False)), ('btn_link', wagtail.core.blocks.CharBlock(default='', help_text='', label='Button Link', required=False)), ('btn_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3')], label='Button Colour'))])), ('modern_img_bg_links_section', wagtail.core.blocks.StructBlock([('title1', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 1 (Optional)', required=False)), ('title2', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 2 (Optional)', required=False)), ('long_title_TRUE', wagtail.core.blocks.BooleanBlock(default=False, label='Long title (Multiline)?', required=False)), ('bg_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='', label='Background Image', required=True)), ('content_align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], label='Content Align')), ('btn_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3')], label='Button Colour')), ('links_stream_container', wagtail.core.blocks.StreamBlock([('url_link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock(help_text='Destination URL', label='Link URL', required=True)), ('text', wagtail.core.blocks.CharBlock(help_text='', label='Display Text', required=True))]))], label='Contact Links', max_num=5, min_num=1, required=True))])), ('modern_form', wagtail.core.blocks.StructBlock([('title1', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 1 (Optional)', required=False)), ('title2', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Header Part 2 (Optional)', required=False)), ('long_title_TRUE', wagtail.core.blocks.BooleanBlock(default=False, label='Long title (Multiline)?', required=False)), ('bg_img', wagtail.documents.blocks.DocumentChooserBlock(help_text='', label='Background Image', required=True)), ('btn_text', wagtail.core.blocks.CharBlock(default='Submit', help_text='', label='Form Submit Button Text', required=True)), ('btn_color', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'Theme Colour 1'), ('2', 'Theme Colour 2'), ('3', 'Theme Colour 3')], label='Button Colour')), ('form_action', wagtail.core.blocks.CharBlock(default='', help_text='The action URL from your form provider.', label='Form Action URL', required=True)), ('show_form_bg', wagtail.core.blocks.BooleanBlock(default=False, label='Show Form Section Background?', required=False)), ('formfields_stream_container', wagtail.core.blocks.StreamBlock([('form_field', wagtail.core.blocks.StructBlock([('field_name_id', wagtail.core.blocks.CharBlock(help_text='Specify a unique name/id. Only letters, numbers, and underscores are allowed. (No spaces)', label='Field Name/ID', required=True)), ('field_type', wagtail.core.blocks.ChoiceBlock(choices=[('text', 'Text'), ('subject', 'Subject'), ('email', 'Email'), ('telephone', 'Phone'), ('message', 'Message')], label='Field Type')), ('label', wagtail.core.blocks.CharBlock(help_text='', label='Field Label (Optional)', required=False)), ('placeholder_text', wagtail.core.blocks.CharBlock(help_text='', label='Placeholder Text', required=False)), ('is_required', wagtail.core.blocks.BooleanBlock(default=False, label='Make Required Field?', required=False))]))], label='Form Fields', min_num=1, required=True))])), ('modern_lead_gen', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Title', required=True)), ('subtitle', wagtail.core.blocks.CharBlock(default='', help_text='', label='Section Subtitle', required=False)), ('btn_text', wagtail.core.blocks.CharBlock(default='Submit', help_text='', label='Button Text', required=True)), ('form_action', wagtail.core.blocks.CharBlock(default='', help_text='The action URL from your form provider.', label='Form Action URL', required=True)), ('placeholder_text', wagtail.core.blocks.CharBlock(help_text='', label='Placeholder Text', required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='site_logo_url',
            field=models.CharField(blank=True, max_length=255, verbose_name='Site Logo Target URL (Optional)'),
        ),
    ]
