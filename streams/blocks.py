from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.fields import StreamField
from wagtail_color_panel.blocks import NativeColorBlock

from django.db import models
from django.db.models.fields import CharField, IntegerField
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey

from .custom_blocks.standard_blocks import *

################## Footer ##################


class Footer_Block(blocks.StructBlock):
    footer_heading_1 = blocks.CharBlock(label="Footer Heading Left", required=False, default="")
    footer_text_1 = blocks.RichTextBlock(label="Additional Company Details", required=False, default="")
    footer_heading_2 = blocks.CharBlock(label="Footer Heading Center", required=True, default="Find Us")

    footer_text_2 = blocks.RichTextBlock(label="Footer Address", required=False, default="Ontario, Canada")
    social_links_stream_container = SocialLink_StreamContainer_Block(label="Social Media Links", required=False)

    footer_heading_3 = blocks.CharBlock(label="Footer Heading Right", required=True, default="Quick Links")
    page_links_stream_container = UrlLink_StreamContainer_Block(label="Page Quick Links", required=True, min_num=1, max_num=5)

    class Meta:
        icon = "edit"
        label = "Footer Design - Classic/Modern"


################## General/Global Blocks ##################


class HTML_Link_Block(blocks.StructBlock):
    link = blocks.RawHTMLBlock(required=True, help_text="Link a font, eg. from Google Fonts.")

    class Meta:
        template = "streams/head_link_block.html"
        icon = "code"
        label = "HTML Header Block"
