from wagtail.core import blocks
from wagtail.core.blocks.struct_block import StructValue
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
    """Testimonial Container"""

    testimonial = TestimonialItem_Block()

    class Meta:
        icon = "openquote"
        label = "Testimonial Items"


# Service Cards


class ServiceCard_Block(blocks.StructBlock):
    icon = blocks.CharBlock(required=False, help_text="Add the card icon class (eg far fa-user).")
    title = blocks.CharBlock(required=False, help_text="Add the card text.")
    paragraph = blocks.CharBlock(required=False, help_text="Add the card body text.")
    btn_text = blocks.CharBlock(label="Button Text (Optional)", default="", required=False)
    btn_link = blocks.CharBlock(label="Button URL", required=False, help_text="")

    class Meta:
        icon = "placeholder"
        label = "Service Card"


class ServiceCardsStreamContainer_Block(blocks.StreamBlock):
    card = ServiceCard_Block()

    class Meta:
        label = "Service Cards Container"


class ServiceCards_Settings_Block(blocks.StructBlock):
    show_card_bg = blocks.BooleanBlock(label="Show Card Background?", default=False, required=False)
    bg_color = blocks.ChoiceBlock(label="Card Background Colour", choices=[("1", "Theme Colour 1"), ("2", "Theme Colour 2"), ("3", "Theme Colour 3"), ("default", "Theme Default Background")], default="default", required=True)

    class Meta:
        label = " "


# Standard Blocks


class SocialLink_Block(blocks.StructBlock):
    link = blocks.URLBlock(label="Link URL", required=True, help_text="Destination URL")
    icon = blocks.CharBlock(label="Display Icon", required=True, help_text="Add the card icon class (eg fab fa-facebook-f).")

    class Meta:
        icon = "site"
        label = "Social Account URL"


class SocialLink_StreamContainer_Block(blocks.StreamBlock):
    social_link = SocialLink_Block()

    class Meta:
        label = ""


# Links


class UrlLink_Block(blocks.StructBlock):
    link = blocks.CharBlock(label="Link URL", required=True, help_text="Destination URL")
    text = blocks.CharBlock(label="Display Text", required=True, help_text="")

    class Meta:
        icon = "site"
        label = "General Link/URL"


class UrlLink_StreamContainer_Block(blocks.StreamBlock):
    url_link = UrlLink_Block()

    class Meta:
        label = ""


# Form Blocks


class FormFields_StructValue(StructValue):
    def field_name(self):
        if self.get("field_type") == "subject":
            return "subject"
        elif self.get("field_type") == "email":
            return "_replyto"
        else:
            return self.get("field_name_id").strip().replace(" ", "_")

    def field_id(self):
        return self.get("field_name_id").strip().replace(" ", "_")

    def placeholder(self):
        if self.get("placeholder_text") or self.get("label"):
            return self.get("placeholder_text")
        else:
            if self.get("field_type") == "subject":
                return "Subject"
            elif self.get("field_type") == "email":
                return "email@domain.com"
            elif self.get("field_type") == "telephone":
                return "123-456-7890"
            else:
                return "Type here"


class FormField_Block(blocks.StructBlock):
    field_name_id = blocks.CharBlock(label="Field Name/ID", required=True, help_text="Specify a unique name/id. Only letters, numbers, and underscores are allowed. (No spaces)")
    field_type = blocks.ChoiceBlock(label="Field Type", choices=[("text", "Text"), ("subject", "Subject"), ("email", "Email"), ("telephone", "Phone"), ("message", "Message")], default="text", required=True)
    label = blocks.CharBlock(label="Field Label (Optional)", required=False, help_text="")
    placeholder_text = blocks.CharBlock(label="Placeholder Text", required=False, help_text="")
    is_required = blocks.BooleanBlock(label="Make Required Field?", default=False, required=False)

    class Meta:
        icon = "form"
        label = "Form Field"
        value_class = FormFields_StructValue


class FormField_StreamContainer_Block(blocks.StreamBlock):
    form_field = FormField_Block()

    class Meta:
        label = ""
