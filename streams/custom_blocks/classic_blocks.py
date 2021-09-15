from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.fields import StreamField
from wagtail_color_panel.blocks import NativeColorBlock

from .standard_blocks import *

################## Classic Site Template Blocks ##################


class Classic_Hero_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Hero Title", default="", required=True, help_text="")
    subtitle = blocks.CharBlock(label="Hero Subtitle", default="", required=True, help_text="")
    btn_text = blocks.CharBlock(label="Hero Button (Optional)", default="Contact me", required=False)
    btn_link = blocks.CharBlock(label="Button URL", default="", required=False, help_text="")

    hero_image = DocumentChooserBlock(required=False, label="Full Hero Image", help_text="Upload your image here")

    class Meta:
        template = "streams/classic_template/classic_hero.html"
        icon = "image"
        label = "Classic - Site Hero"


class Classic_SubHero_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Section Header", default="Section Title", required=True, help_text="")
    paragraph = blocks.CharBlock(label="Section Paragraph", default="", required=False)
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="2", required=True)

    services_container = ServiceCardsStreamContainer_Block(label="Add a few cards here (optional)", required=False)

    class Meta:
        template = "streams/classic_template/classic_sub_hero.html"
        icon = "edit"
        label = "Classic - Sub-Hero Section"


class Classic_TextSection_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Section Header", default="Section Title", required=False, help_text="")
    paragraph = blocks.CharBlock(label="Section Paragraph", default="", required=True)

    fit_below_sub_hero_TRUE = blocks.BooleanBlock(label="Remove top padding to fit below hero?", default=False, required=False)

    class Meta:
        template = "streams/classic_template/classic_text_section.html"
        icon = "edit"
        label = "Classic - Text Section"


class Classic_TextButton_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Section Header", default="Questions?", required=True, help_text="Add your section title.")
    paragraph = blocks.CharBlock(label="Section Paragraph", default="", required=False)
    btn_text = blocks.CharBlock(label="Button Text (Optional)", default="", required=False)
    btn_link = blocks.CharBlock(label="Button URL", default="", required=False, help_text="")

    class Meta:
        template = "streams/classic_template/classic_text_and_btn.html"
        icon = "edit"
        label = "Classic - Text and Button"


class Classic_ServiceCards_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Section Header", default="Section Title", required=False, help_text="")

    services_settings = ServiceCards_Settings_Block()
    services_container = ServiceCardsStreamContainer_Block(required=True)

    class Meta:
        template = "streams/classic_template/classic_cards.html"
        icon = "list-ul"
        label = "Classic - Service Cards"


class Classic_ImgTextSplit_Block(blocks.StructBlock):
    title = blocks.CharBlock(default="Don't wait. Start saving!", required=False, help_text="Add your section title.")
    paragraph = blocks.CharBlock(label="Section Paragraph", default="", required=False)
    btn_text = blocks.CharBlock(label="Button Text", default="Learn more", required=False)
    btn_link = blocks.CharBlock(label="Button URL", default="", required=False, help_text="")

    half_img = DocumentChooserBlock(required=True, label="Split Image", help_text="Upload an image here")
    img_position = blocks.ChoiceBlock(label="Image Position", choices=[("left", "Left"), ("right", "Right")], default="left", required=True)
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)

    class Meta:
        template = "streams/classic_template/classic_img_text_split.html"
        icon = "edit"
        label = "Classic - Img and Text Split"


class Classic_TestimonialCarousel_Block(blocks.StructBlock):
    title = blocks.CharBlock(required=True, label="Section Title", help_text="Add your section title.")
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)
    btn_text = blocks.CharBlock(label="Button Text", default="Read all testimonials", required=False, help_text="Button display text. Leave blank for no button.")
    btn_link = blocks.CharBlock(label="Button URL", default="", required=False, help_text="")

    testimonials_container = TestimonialStreamContainer_Block()

    class Meta:
        template = "streams/classic_template/classic_testimonials_carousel.html"
        icon = "group"
        label = "Classic - Testimonials Carousel"


class Classic_NewsletterSplit_Block(blocks.StructBlock):
    title = blocks.CharBlock(default="Title Here", required=False, help_text="Add your section title.")
    section_paragraph = blocks.CharBlock(default="", required=False, help_text="Add your section subtitle.")

    half_img = DocumentChooserBlock(required=True, label="Split Image", help_text="Upload an image here")
    img_position = blocks.ChoiceBlock(label="Image Position", choices=[("left", "Left"), ("right", "Right")], default="left", required=True)
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)

    btn_text = blocks.CharBlock(label="Form Submit Button Text", default="Submit", required=True, help_text="")
    form_action = blocks.CharBlock(label="Form Action URL", default="", required=True, help_text="The action URL from your form provider.")
    show_form_bg = blocks.BooleanBlock(label="Show Form Box Outline?", default=False, required=False)

    class Meta:
        template = "streams/classic_template/classic_newsletter_split.html"
        icon = "mail"
        label = "Classic - Newsletter Split"


class Classic_ContactFormSplit_Block(blocks.StructBlock):
    title = blocks.CharBlock(default="Get in touch", required=False, help_text="Add your section title.")
    section_paragraph = blocks.CharBlock(default="", required=False, help_text="Add your section subtitle.")

    half_img = DocumentChooserBlock(required=True, label="Split Image", help_text="Upload an image here")
    img_position = blocks.ChoiceBlock(label="Image Position", choices=[("left", "Left"), ("right", "Right")], default="right", required=True)
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)

    btn_text = blocks.CharBlock(label="Form Submit Button Text", default="Submit", required=True, help_text="")
    form_action = blocks.CharBlock(label="Form Action URL", default="", required=True, help_text="The action URL from your form provider.")
    show_form_bg = blocks.BooleanBlock(label="Show Form Box Outline?", default=False, required=False)

    # streamfield for all form items
    formfields_stream_container = FormField_StreamContainer_Block(label="Form Fields", required=True, min_num=1)

    class Meta:
        template = "streams/classic_template/classic_contact_form.html"
        icon = "form"
        label = "Classic - Contact Form"


class Classic_PageBanner_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Page Banner Title", default="", required=False, help_text="The page banner tite. Leave blank to use page name.")
    subtitle = blocks.CharBlock(label="Page Banner Subtitle", default="", required=False)
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="2", required=True)

    class Meta:
        template = "streams/classic_template/classic_child_banner.html"
        icon = "edit"
        label = "Classic - Page Banner Section"


class Classic_TestimonialCards_Block(blocks.StructBlock):
    title = blocks.CharBlock(label="Section Title", default="Section Title", required=False, help_text="")

    card_bg_color = blocks.ChoiceBlock(label="Card Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="2", required=True)
    quote_bg_color = blocks.ChoiceBlock(label="Quote Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)

    testimonials_container = TestimonialStreamContainer_Block()

    class Meta:
        template = "streams/classic_template/classic_testimonial_cards.html"
        icon = "edit"
        label = "Classic - Testimonial Cards"
