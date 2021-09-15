from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.fields import StreamField
from wagtail_color_panel.blocks import NativeColorBlock

# Begin Testimonial Section Items

class TestimonialItem_Block(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Add the testimonial.")
    author = blocks.CharBlock(required=True, help_text="Add the testimonial author.")

    class Meta:
        icon = "openquote"
        label = "Testimonial Item"


class TestimonialStreamContainer_Block(blocks.StreamBlock):
    """Testimonial Container Carousel"""
    testimonial = TestimonialItem_Block()

    class Meta:
        icon = "openquote"
        label = "Testimonial Carousel"


class TestimonialSettings_Block(blocks.StructBlock):
    title = blocks.CharBlock(required=True, label="Section Title", help_text="Add your section title.", icon = "user")
    section_bg_color = NativeColorBlock(default="", required=False)

    class Meta:
        label = " "