from django.db import models
from django.db.models.fields import CharField, IntegerField, DecimalField

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel, StreamFieldPanel, ObjectList, TabbedInterface
from wagtail.core import blocks
from wagtail.core.blocks.field_block import RawHTMLBlock
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from django import template

register = template.Library()
from django.shortcuts import redirect
from django.core.validators import MinValueValidator, MaxValueValidator

from streams import blocks as custom_blocks

# custom block imports
from streams.custom_blocks import classic_blocks
from streams.custom_blocks import minimalistic_blocks
from streams.custom_blocks import modern_blocks


temp = "3"


class HomePage(Page):
    template = "home/home_page.html"
    subpage_types = ["home.ChildPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["parent"] = HomePage.objects.get(slug=self.slug)
        return context

    def type(self):
        return "HomePage"

    ################## Content ##################
    if temp == "minimalistic":
        content = StreamField(
            [
                # Minimalistic
                ("hero_split", minimalistic_blocks.HeroSplit_Block()),
                ("testimonials_section", minimalistic_blocks.Testimonial_Section_Block()),
                ("services", minimalistic_blocks.ServiceCards_Block()),
                ("about_section", minimalistic_blocks.About_Block()),
                ("contact_section", minimalistic_blocks.Contact_Block()),
            ],
            null=True,
            blank=True,
        )
    elif temp == "classic":
        content = StreamField(
            [
                # Classic
                ("classic_hero", classic_blocks.Classic_Hero_Block()),
                ("classic_sub_hero", classic_blocks.Classic_SubHero_Block()),
                ("classic_site_intro", classic_blocks.Classic_TextSection_Block()),
                ("classic_three_cards", classic_blocks.Classic_ServiceCards_Block()),
                ("classic_text_and_btn", classic_blocks.Classic_TextButton_Block()),
                ("classic_img_text_split", classic_blocks.Classic_ImgTextSplit_Block()),
                ("classic_newsletter_split", classic_blocks.Classic_NewsletterSplit_Block()),
                ("classic_contact_form", classic_blocks.Classic_ContactFormSplit_Block()),
                ("classic_testimonials_carousel", classic_blocks.Classic_TestimonialCarousel_Block()),
            ],
            null=True,
            blank=True,
        )
    else:
        content = StreamField(
            [
                # Minimalistic
                ("hero_split", minimalistic_blocks.HeroSplit_Block()),
                ("testimonials_section", minimalistic_blocks.Testimonial_Section_Block()),
                ("services", minimalistic_blocks.ServiceCards_Block()),
                ("about_section", minimalistic_blocks.About_Block()),
                ("contact_section", minimalistic_blocks.Contact_Block()),
                # Classic
                ("classic_hero", classic_blocks.Classic_Hero_Block()),
                ("classic_sub_hero", classic_blocks.Classic_SubHero_Block()),
                ("classic_site_intro", classic_blocks.Classic_TextSection_Block()),
                ("classic_three_cards", classic_blocks.Classic_ServiceCards_Block()),
                ("classic_text_and_btn", classic_blocks.Classic_TextButton_Block()),
                ("classic_img_text_split", classic_blocks.Classic_ImgTextSplit_Block()),
                ("classic_newsletter_split", classic_blocks.Classic_NewsletterSplit_Block()),
                ("classic_contact_form", classic_blocks.Classic_ContactFormSplit_Block()),
                ("classic_testimonials_carousel", classic_blocks.Classic_TestimonialCarousel_Block()),
                # Modern
                ("modern_hero", modern_blocks.Modern_Hero_Block()),
                ("modern_text_section", modern_blocks.Modern_TextSection_Block()),
                ("modern_cards", modern_blocks.Modern_ServiceCards_Block()),
                ("modern_quote", modern_blocks.Modern_Quote_Block()),
                ("modern_text_img_block", modern_blocks.Modern_TextImg_Block()),
                ("modern_img_bg_section", modern_blocks.Modern_ImgBgParagraph_Block()),
                ("modern_img_bg_links_section", modern_blocks.Modern_ImgBgLinks_Block()),
                ("modern_form", modern_blocks.Modern_ContactForm_Block()),
                ("modern_lead_gen", modern_blocks.Modern_LeadGen_Block()),
            ],
            null=True,
            blank=True,
        )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    ################## Site Settings ##################

    # Site Page Design Template
    page_template = models.CharField(max_length=20, choices=[("classic", "Classic"), ("minimalistic", "Minimalistic"), ("modern", "Modern")], default="classic")

    # Site Specific Brand Settings

    # Site Colors
    bg_color = ColorField("Background Colour", default="#ffffff")
    color1 = ColorField("Color 1", default="#008037")
    color2 = ColorField("Color 2", default="#006580")
    color3 = ColorField("Color 3", default="#ffffff")
    nav_text_color = ColorField("Navbar Menu Item Colour", default="", blank=True)
    nav_text_color_hover = ColorField("Navbar Menu Item Hover Colour (Optional)", default="", blank=True)
    nav_bg_color = ColorField("Navbar Color", default="#ffffff")
    # nav_bg_transparent = DecimalField("Navbar Background Opacity", decimal_places=2, max_digits=3, default=1.0, validators=[MinValueValidator(0), MaxValueValidator(1)], help_text="Enter a value between 0.0 and 1.0")
    nav_bg_transparent = models.BooleanField(verbose_name="Navbar Transparent Background?", blank=True, default=False)

    # Site Navbar Logo and title
    site_logo = models.ForeignKey("wagtaildocs.Document", verbose_name="Site Logo", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Add a logo for your site.")
    site_logo_link_page = models.ForeignKey(
        "wagtailcore.Page",
        on_delete=models.SET_NULL,
        verbose_name="Site Logo Link to an internal page",
        null=True,
        blank=True,
        related_name="+",
    )
    site_logo_url = models.CharField(verbose_name="Site Logo Target URL (Optional)", max_length=255, blank=True, help_text="")
    site_title = models.CharField(verbose_name="Site Title", max_length=255, blank=True, help_text="Enter a title for your site, or leave blank to use a logo instead.")

    site_favicon = models.ForeignKey("wagtaildocs.Document", verbose_name="Favicon", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Add a favicon for your site.")

    nav_height = models.IntegerField(verbose_name="Navbar Height (px)", default=100, blank=False, null=True)
    nav_logo_max_size = models.IntegerField(verbose_name="Navbar Logo Max Width (px)", default=200, blank=False, null=True)
    nav_font_size = models.CharField(verbose_name="Navbar Font Size (rem or px)", max_length=20, blank=False, default="20px")
    navbar_fixed = models.BooleanField(verbose_name="Fix Navbar to top of page during scroll?", blank=True, default=True)
    shrink_navbar_scroll = models.BooleanField(verbose_name="Shrink Navbar on Scroll?", blank=True, default=True)

    # Site Footer
    footer_enabled = models.BooleanField(verbose_name="Enable Site Footer?", blank=True, default=True)
    footer_bg_color = models.CharField("Footer Background Colour", max_length=20, choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="default")
    footer_text_copyright = RichTextField("Footer Text", help_text='Footer text here. Use "DATE_VALUE" to insert current date.', default="Copyright DATE_VALUE Website Created by Atomic Inc.", null=True, blank=True)
    footer_image = models.ForeignKey("wagtaildocs.Document", verbose_name="Footer Logo", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Add a logo for your site's footer.")
    footer_logo_max_size = models.IntegerField(verbose_name="Footer Logo Max Width (px)", default=200, blank=True, null=True)

    # Misc Site Items
    site_loader_image = models.ForeignKey("wagtaildocs.Document", verbose_name="Site Loader Gif", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Add an optional loader gif for your site.")
    site_loader_bg_color = ColorField("Site Loader Background Colour", default="#ffffff", null=True, blank=True)

    footer_design_stream = StreamField(
        [
            ("footer_design_classic", custom_blocks.Footer_Block()),
            # ("footer_design_minimalistic", custom_blocks.Minimalistic_Footer_Block()),
        ],
        null=True,
        blank=True,
        verbose_name="Footer Design",
        min_num=0,
        max_num=1,
    )

    brand_settings_panels = [
        FieldPanel("page_template", heading="Page Design Template"),
        MultiFieldPanel(
            [
                FieldPanel("site_title"),
                DocumentChooserPanel("site_logo"),
                PageChooserPanel("site_logo_link_page"),
                FieldPanel("site_logo_url"),
                FieldPanel("nav_height"),
                FieldPanel("nav_logo_max_size"),
                FieldPanel("navbar_fixed"),
                FieldPanel("shrink_navbar_scroll"),
                FieldPanel("nav_bg_transparent"),
            ],
            heading="Site Navbar Settings",
        ),
        MultiFieldPanel(
            [
                NativeColorPanel("bg_color"),
                NativeColorPanel("color1"),
                NativeColorPanel("color2"),
                NativeColorPanel("color3"),
                NativeColorPanel("nav_bg_color"),
            ],
            heading="Site Colours",
        ),
        MultiFieldPanel(
            [
                FieldPanel("footer_enabled"),
                FieldPanel("footer_bg_color"),
                FieldPanel("footer_text_copyright"),
                DocumentChooserPanel("footer_image"),
                FieldPanel("footer_logo_max_size"),
                StreamFieldPanel("footer_design_stream"),
            ],
            heading="Footer Settings",
        ),
        MultiFieldPanel(
            [
                DocumentChooserPanel("site_favicon"),
                # NativeColorPanel("site_loader_bg_color"),
                # DocumentChooserPanel("site_loader_image"),
            ],
            heading="Misc Site Items",
        ),
    ]

    ############ Site Font Settings

    # Font colors
    default_font_color = ColorField("Default Font Colour", default="#000000", blank=False, null=True)
    bg_1_font_color = ColorField("Font Colour for Background Colour 1 (Optional)", default="", blank=True, null=True)
    bg_2_font_color = ColorField("Font Colour for Background Colour 2 (Optional)", default="", blank=True, null=True)
    bg_3_font_color = ColorField("Font Colour for Background Colour 3 (Optional)", default="", blank=True, null=True)

    default_hero_font_color = ColorField("Hero Font Colour", blank=True, null=True)

    default_font = models.CharField(verbose_name="Default Font-Family", max_length=255, blank=True)
    root_font_size = models.IntegerField(verbose_name="Root Font Size (px)", default=18, blank=False, null=True)

    # Font weight
    font_weight_heavy = models.IntegerField(verbose_name="Heavy Weight", default=800, blank=False, null=True)
    font_weight_medium = models.IntegerField(verbose_name="Medium Weight", default=600, blank=False, null=True)
    font_weight_light = models.IntegerField(verbose_name="Light Weight", default=400, blank=False, null=True)

    ############ Site HTML Links

    # Fonts

    html_head_import_stream = StreamField(
        [
            ("html_head_link", custom_blocks.HTML_Link_Block()),
            # ("html_head_link", blocks.ListBlock(blocks.CharBlock(label="Ingredient"))),
        ],
        null=True,
        blank=True,
    )

    font_settings_panels = [
        MultiFieldPanel(
            [
                FieldPanel("default_font"),
                FieldPanel("root_font_size"),
                FieldPanel("nav_font_size"),
                NativeColorPanel("default_font_color"),
                NativeColorPanel("bg_1_font_color"),
                NativeColorPanel("bg_2_font_color"),
                NativeColorPanel("bg_3_font_color"),
                NativeColorPanel("default_hero_font_color"),
                NativeColorPanel("nav_text_color"),
                NativeColorPanel("nav_text_color_hover"),
            ],
            heading="Default Font",
        ),
        MultiFieldPanel(
            [
                FieldPanel("font_weight_heavy"),
                FieldPanel("font_weight_medium"),
                FieldPanel("font_weight_light"),
            ],
            heading="Font Weight",
        ),
        StreamFieldPanel(("html_head_import_stream"), heading="Font Imports"),
    ]

    ############ Site Menu

    menu_settings_panels = [
        InlinePanel("menu_items", heading="Menu Items", label="Menu Item"),
    ]

    ################## Tab Settings Final Output ##################

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(Page.settings_panels, heading="Settings"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(brand_settings_panels, heading="Brand Settings"),
            ObjectList(font_settings_panels, heading="Font Settings"),
            ObjectList(menu_settings_panels, heading="Site Menu"),
        ]
    )

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


################## Orderables ##################


# class FontImport(Orderable):
#     font_import_link = CharField("Font Import Link", blank=False, null=True, max_length=500, help_text="Link a font, eg. from Google Fonts.")

#     page = ParentalKey("HomePage", related_name="font_imports")

#     panels = [
#         FieldPanel("font_import_link"),
#     ]


############ Site Menu Items


class MenuItem(Orderable):
    link_text = models.CharField("Link Text", blank=False, null=True, max_length=50)
    link_url = models.CharField("Link URL", blank=True, max_length=500)
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name="Link to an internal page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(verbose_name="Open in new tab?", blank=True, default=False)
    allow_subnav = models.BooleanField(verbose_name=("Allow sub-menu for this item"), default=False, help_text=("NOTE: The sub-menu might not be displayed, even if checked. " "It depends on how the menu is used in this project's templates."))
    make_button = models.BooleanField(verbose_name=("Make menu item a button?"), default=False, help_text=(""))

    nav_button_color = models.CharField("Button Colour", max_length=20, choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], blank=False, default="2")

    page = ParentalKey("HomePage", related_name="menu_items")

    panels = [
        PageChooserPanel("link_page", ["home.HomePage", "home.ChildPage"]),
        FieldPanel("link_url"),
        FieldPanel("link_text"),
        FieldPanel("open_in_new_tab"),
        FieldPanel("allow_subnav"),
        FieldPanel("make_button"),
        FieldPanel("nav_button_color"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"

    @property
    def text(self):
        if self.link_page and not self.link_text:
            return self.link_page.text
        elif self.link_text:
            return self.link_text
        return "Missing Title"


#######################################################################
############################## Child Page #############################
#######################################################################


class ChildPage(Page):
    template = "home/home_page.html"
    subpage_types = []
    parent_page_types = ["home.HomePage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        parent_name = self.get_parent().slug
        context["parent"] = HomePage.objects.get(slug=parent_name)
        return context

    def template_type(self):
        return self.get_parent().page_template

    def type(self):
        return "ChildPage"

    ################## Content ##################
    if template_type == "minimalistic":
        content = StreamField(
            [
                # Minimalistic
                ("hero_split", minimalistic_blocks.HeroSplit_Block()),
                ("testimonials_section", minimalistic_blocks.Testimonial_Section_Block()),
                ("services", minimalistic_blocks.ServiceCards_Block()),
                ("about_section", minimalistic_blocks.About_Block()),
                ("contact_section", minimalistic_blocks.Contact_Block()),
            ],
            null=True,
            blank=True,
        )
    elif template_type == "classic":
        content = StreamField(
            [
                # Classic
                ("classic_hero", classic_blocks.Classic_Hero_Block()),
                ("classic_sub_hero", classic_blocks.Classic_SubHero_Block()),
                ("classic_site_intro", classic_blocks.Classic_TextSection_Block()),
                ("classic_three_cards", classic_blocks.Classic_ServiceCards_Block()),
                ("classic_text_and_btn", classic_blocks.Classic_TextButton_Block()),
                ("classic_img_text_split", classic_blocks.Classic_ImgTextSplit_Block()),
                ("classic_newsletter_split", classic_blocks.Classic_NewsletterSplit_Block()),
                ("classic_contact_form", classic_blocks.Classic_ContactFormSplit_Block()),
                ("classic_testimonials_carousel", classic_blocks.Classic_TestimonialCarousel_Block()),
            ],
            null=True,
            blank=True,
        )
    else:
        content = StreamField(
            [
                # Classic
                ("classic_page_banner", classic_blocks.Classic_PageBanner_Block()),
                ("classic_hero", classic_blocks.Classic_Hero_Block()),
                ("classic_sub_hero", classic_blocks.Classic_SubHero_Block()),
                ("classic_site_intro", classic_blocks.Classic_TextSection_Block()),
                ("classic_three_cards", classic_blocks.Classic_ServiceCards_Block()),
                ("classic_text_and_btn", classic_blocks.Classic_TextButton_Block()),
                ("classic_img_text_split", classic_blocks.Classic_ImgTextSplit_Block()),
                ("classic_newsletter_split", classic_blocks.Classic_NewsletterSplit_Block()),
                ("classic_contact_form", classic_blocks.Classic_ContactFormSplit_Block()),
                ("classic_testimonials_carousel", classic_blocks.Classic_TestimonialCarousel_Block()),
                ("classic_testimonial_cards", classic_blocks.Classic_TestimonialCards_Block()),
                # Modern
                ("modern_hero", modern_blocks.Modern_Hero_Block()),
                ("modern_text_section", modern_blocks.Modern_TextSection_Block()),
                ("modern_cards", modern_blocks.Modern_ServiceCards_Block()),
                ("modern_quote", modern_blocks.Modern_Quote_Block()),
                ("modern_text_img_block", modern_blocks.Modern_TextImg_Block()),
                ("modern_img_bg_section", modern_blocks.Modern_ImgBgParagraph_Block()),
                ("modern_img_bg_links_section", modern_blocks.Modern_ImgBgLinks_Block()),
                ("modern_form", modern_blocks.Modern_ContactForm_Block()),
                ("modern_lead_gen", modern_blocks.Modern_LeadGen_Block()),
            ],
            null=True,
            blank=True,
        )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Child Page"
        verbose_name_plural = "Child Pages"
