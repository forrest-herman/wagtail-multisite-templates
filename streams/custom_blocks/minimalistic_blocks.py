from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.fields import StreamField
from wagtail_color_panel.blocks import NativeColorBlock

from .standard_blocks import *


################## Minimalistic Blocks ##################


class HeroSplit_Block(blocks.StructBlock):
    """Hero Section - H1 text on left, image on right"""

    title = blocks.CharBlock(required=True, help_text="Add your hero title.")
    subtitle = blocks.CharBlock(required=False, help_text="Add your hero subtitle.")
    title_color = NativeColorBlock(required=False, label="Title Color Override")
    subtitle_color = NativeColorBlock(required=False, label="Subtitle Color Override")
    hero_image = DocumentChooserBlock(required=False, label="Hero Image", help_text="Upload a hero image here")
    circle_top_color = NativeColorBlock(required=False, label="Top Circle Color", help_text="Choose top circle color. Leave blank for no top circle.")
    circle_bottom_color = NativeColorBlock(required=False, label="Bottom Circle Color", help_text="Choose bottom circle color. Leave blank for no bottom circle.")
    btn_text = blocks.CharBlock(required=False, label="Button Text (Optional)", help_text="Add Button 1 text. Leave blank for no button.")
    btn_link = blocks.URLBlock(required=False, label="Button URL", help_text="Target URL for hero button.")
    btn_color = blocks.ChoiceBlock(label="Button Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3")], default="2", required=True)

    class Meta:
        template = "streams/minimalistic_template/minimalistic_hero_split.html"
        icon = "image"
        label = "Minimalistic - Hero - Split"


class Testimonial_Section_Block(blocks.StructBlock):
    title = blocks.CharBlock(required=True, label="Section Title", help_text="Add your section title.", icon="user")
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)

    testimonials_container = TestimonialStreamContainer_Block()

    class Meta:
        template = "streams/minimalistic_template/minimalistic_testimonials.html"
        icon = "group"
        label = "Minimalistic - Testimonials Carousel"


class ServiceCards_Block(blocks.StructBlock):
    title = blocks.CharBlock(required=True, label="Section Title", help_text="Add your section title.", icon="user")
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)
    btn_color = blocks.ChoiceBlock(label="Button Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3")], default="2", required=True)

    services_settings = ServiceCards_Settings_Block()
    services_container = ServiceCardsStreamContainer_Block()

    class Meta:
        template = "streams/minimalistic_template/minimalistic_services.html"
        icon = "list-ul"
        label = "Minimalistic - Services Cards"


class About_Block(blocks.StructBlock):
    """About Section"""

    title_1 = blocks.CharBlock(label="Section Title 1", required=False, help_text="")
    title_2 = blocks.CharBlock(label="Section Title 2", required=False, help_text="")
    about_paragraph = blocks.RichTextBlock(required=False, help_text="")

    about_image = DocumentChooserBlock(required=False, label="About Image", help_text="Upload a profile picture here.")

    btn_text = blocks.CharBlock(label="Button Text", required=False, help_text="")
    btn_link = blocks.CharBlock(label="Button Target URL", required=False, help_text="")
    btn_color = blocks.ChoiceBlock(label="Button Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3")], default="2", required=True)
    btn_icon = blocks.CharBlock(label="Button Icon (Optional)", required=False, help_text="Add an icon class (eg far fa-comments).")

    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)

    class Meta:
        template = "streams/minimalistic_template/minimalistic_about.html"
        icon = "user"
        label = "Minimalistic - About"


class Contact_Block(blocks.StructBlock):
    """Contact Section"""

    title = blocks.CharBlock(required=True, help_text="Add your section title.")
    section_subtitle = blocks.CharBlock(required=False, help_text="Add your section subtitle.")
    bg_color = blocks.ChoiceBlock(label="Section Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="1", required=True)
    font_color_override = NativeColorBlock(required=False, label="Font Colour Override (Optional)", default="#000000", help_text="")
    section_bg_image = DocumentChooserBlock(required=False, label="Choose a background image.", help_text="")
    html_body = blocks.RawHTMLBlock(required=False, label="Body HTML", help_text="Add the HTML for your contact form.")

    class Meta:
        template = "streams/minimalistic_template/minimalistic_contact.html"
        icon = "date"
        label = "Minimalistic - Contact Section"
