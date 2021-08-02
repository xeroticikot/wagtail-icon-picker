from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail_icon_picker.validators import hex_triplet_validator


class IconField(models.CharField):
    default_validators = []
    description = _("Pick an icon from the list.")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 70)
        super().__init__(*args, **kwargs)
