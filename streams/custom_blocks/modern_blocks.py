from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.fields import StreamField
from wagtail_color_panel.blocks import NativeColorBlock

from .standard_blocks import *


################## Modern Site Template Blocks ##################


class Modern_Hero_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Hero Title", default="", required=False, help_text="")
    subtitle = blocks.CharBlock(label="Hero Subtitle", default="", required=False, help_text="")

    hero_image = DocumentChooserBlock(required=False, label="Full Hero Image", help_text="Upload your image here")

    class Meta:
        template = "streams/modern_template/modern_hero.html"
        icon = "image"
        label = "Modern - Site Hero"


class Modern_TextSection_Block(blocks.StructBlock):
    title1 = blocks.CharBlock(label="Section Header Part 1 (Optional)", default="", required=False, help_text="")
    title2 = blocks.CharBlock(label="Section Header Part 2 (Optional)", default="", required=False, help_text="")
    paragraph = blocks.CharBlock(label="Section Paragraph", default="", required=False)
    text_align = blocks.ChoiceBlock(label="Text Align", choices=[("text-start", "Left"), ("text-center", "Center"), ("text-end", "Right")], default="text-start", required=True)

    class Meta:
        template = "streams/modern_template/modern_text_section.html"
        icon = "edit"
        label = "Modern - Text Section"


class Modern_ServiceCards_Block(blocks.StructBlock):
    title1 = blocks.CharBlock(label="Section Header Part 1 (Optional)", default="", required=False, help_text="")
    title2 = blocks.CharBlock(label="Section Header Part 2 (Optional)", default="", required=False, help_text="")
    long_title_TRUE = blocks.BooleanBlock(label="Long title (Multiline)?", default=False, required=False)

    # show_card_body_on_hover = blocks.BooleanBlock(label="Show Card Body Text on Hover?", default=False, required=False)
    services_container = ServiceCardsStreamContainer_Block(required=True)

    class Meta:
        template = "streams/modern_template/modern_cards.html"
        icon = "list-ul"
        label = "Modern - Service Cards"


class Modern_Quote_Block(blocks.StructBlock):
    title1 = blocks.CharBlock(label="Section Header Part 1 (Optional)", default="", required=False, help_text="")
    title2 = blocks.CharBlock(label="Section Header Part 2 (Optional)", default="", required=False, help_text="")
    long_title_TRUE = blocks.BooleanBlock(label="Long title (Multiline)?", default=False, required=False)

    paragraph = blocks.CharBlock(label="Quote Paragraph", default="", required=True)
    text_align = blocks.ChoiceBlock(label="Text Align", choices=[("text-start", "Left"), ("text-center", "Center"), ("text-end", "Right")], default="text-start", required=True)
    # bg_color = blocks.ChoiceBlock(label="Text Section Background Colour", choices=[('1','Theme Colour 1'),('2','Theme Colour 2'),('3','Theme Colour 3'),('default','Theme Default Background')], default="default", required=True)

    btn_text = blocks.CharBlock(label="Button Text", default="", required=False, help_text="Optional button. Leave blank to hide button.")
    btn_link = blocks.CharBlock(label="Button Link", default="", required=False, help_text="")
    btn_align = blocks.ChoiceBlock(label="Button Align", choices=[("left", "Left"), ("right", "Right")], default="left", required=True)
    btn_color = blocks.ChoiceBlock(label="Button Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3")], default="2", required=True)

    # show_card_bg = blocks.BooleanBlock(label="Show Card Background?", default=True, required=False)
    # bg_color = blocks.ChoiceBlock(label="Section Background", choices=[('1','Theme Colour 1'),('2','Theme Colour 2'),('3','Theme Colour 3'),('default','Theme Default Background')], default="1", required=True)

    class Meta:
        template = "streams/modern_template/modern_quote.html"
        icon = "edit"
        label = "Modern - Quote Section"


class Modern_TextImg_Block(blocks.StructBlock):
    paragraph = blocks.CharBlock(label="Paragraph Text", default="", required=True)
    text_align = blocks.ChoiceBlock(label="Text Align", choices=[("text-start", "Left"), ("text-center", "Center"), ("text-end", "Right")], default="text-start", required=True)

    img = DocumentChooserBlock(label="Image Selector (Optional)", required=False, help_text="Upload an image here. Alternatively leave blank for a simple text block.")
    img_position = blocks.ChoiceBlock(label="Image Position", choices=[("left", "Left"), ("right", "Right")], default="left", required=True)
    img_max_width = blocks.IntegerBlock(label="Max Image Width (px)", default="450", required=True)

    # bg_color = blocks.ChoiceBlock(label="Section Background", choices=[('1','Theme Colour 1'),('2','Theme Colour 2'),('3','Theme Colour 3'),('default','Theme Default Background')], default="1", required=True)

    class Meta:
        template = "streams/modern_template/modern_text_img_block.html"
        icon = "edit"
        label = "Modern - Text and Image Block"


class Modern_ImgBgParagraph_Block(blocks.StructBlock):
    title1 = blocks.CharBlock(label="Section Header Part 1 (Optional)", default="", required=False, help_text="")
    title2 = blocks.CharBlock(label="Section Header Part 2 (Optional)", default="", required=False, help_text="")
    long_title_TRUE = blocks.BooleanBlock(label="Long title (Multiline)?", default=False, required=False)

    paragraph = blocks.CharBlock(label="Paragraph", default="", required=True)
    text_align = blocks.ChoiceBlock(label="Text Align", choices=[("text-start", "Left"), ("text-center", "Center"), ("text-end", "Right")], default="text-start", required=True)
    bg_color = blocks.ChoiceBlock(label="Card Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="default", required=True)

    bg_img = DocumentChooserBlock(label="Background Image", required=True, help_text="")
    content_align = blocks.ChoiceBlock(label="Content Align", choices=[("left", "Left"), ("right", "Right")], default="left", required=True)

    btn_text = blocks.CharBlock(label="Button Text", default="", required=False, help_text="Optional button. Leave blank to hide button.")
    btn_link = blocks.CharBlock(label="Button Link", default="", required=False, help_text="")
    btn_color = blocks.ChoiceBlock(label="Button Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3")], default="2", required=True)

    class Meta:
        template = "streams/modern_template/modern_img_bg_section.html"
        icon = "edit"
        label = "Modern - Image Background Paragraph Section"


class Modern_ImgBgLinks_Block(blocks.StructBlock):
    title1 = blocks.CharBlock(label="Section Header Part 1 (Optional)", default="", required=False, help_text="")
    title2 = blocks.CharBlock(label="Section Header Part 2 (Optional)", default="", required=False, help_text="")
    long_title_TRUE = blocks.BooleanBlock(label="Long title (Multiline)?", default=False, required=False)

    # paragraph = blocks.CharBlock(label="Paragraph", default="", required=True)
    # text_align = blocks.ChoiceBlock(label="Text Align", choices=[('text-start','Left'),('text-center','Center'),('text-end','Right')], default="text-start", required=True)
    # bg_color = blocks.ChoiceBlock(label="Card Background Colour", choices=[('1','Theme Colour 1'),('2','Theme Colour 2'),('3','Theme Colour 3'),('default','Theme Default Background')], default="default", required=True)

    bg_img = DocumentChooserBlock(label="Background Image", required=True, help_text="")
    content_align = blocks.ChoiceBlock(label="Content Align", choices=[("left", "Left"), ("right", "Right")], default="left", required=True)

    btn_color = blocks.ChoiceBlock(label="Button Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3")], default="2", required=True)
    links_stream_container = UrlLink_StreamContainer_Block(label="Contact Links", required=True, min_num=1, max_num=5)

    class Meta:
        template = "streams/modern_template/modern_img_bg_links_section.html"
        icon = "edit"
        label = "Modern - Image Background Links Section"


class Modern_ContactForm_Block(blocks.StructBlock):
    title1 = blocks.CharBlock(label="Section Header Part 1 (Optional)", default="", required=False, help_text="")
    title2 = blocks.CharBlock(label="Section Header Part 2 (Optional)", default="", required=False, help_text="")
    long_title_TRUE = blocks.BooleanBlock(label="Long title (Multiline)?", default=False, required=False)

    bg_img = DocumentChooserBlock(label="Background Image", required=True, help_text="")

    btn_text = blocks.CharBlock(label="Form Submit Button Text", default="Submit", required=True, help_text="")
    btn_color = blocks.ChoiceBlock(label="Button Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3")], default="2", required=True)
    form_action = blocks.CharBlock(label="Form Action URL", default="", required=True, help_text="The action URL from your form provider.")
    show_form_bg = blocks.BooleanBlock(label="Show Form Section Background?", default=False, required=False)

    # streamfield for all form items
    formfields_stream_container = FormField_StreamContainer_Block(label="Form Fields", required=True, min_num=1)

    class Meta:
        template = "streams/modern_template/modern_form.html"
        icon = "form"
        label = "Modern - Contact Form"


class Modern_LeadGen_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Section Title", default="", required=True, help_text="")
    subtitle = blocks.CharBlock(label="Section Subtitle", default="", required=False, help_text="")

    btn_text = blocks.CharBlock(label="Button Text", default="Submit", required=True, help_text="")
    form_action = blocks.CharBlock(label="Form Action URL", default="", required=True, help_text="The action URL from your form provider.")

    placeholder_text = blocks.CharBlock(label="Placeholder Text", required=False, help_text="")

    class Meta:
        template = "streams/modern_template/modern_lead_gen.html"
        icon = "mail"
        label = "Modern - Lead Gen"
