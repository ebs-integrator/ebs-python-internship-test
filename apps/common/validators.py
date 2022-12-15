from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


# Create your validators here.


@deconstructible
class CustomNumericValidator:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, value: str):
        invalid_symbols = not value.isdigit()
        if invalid_symbols:
            raise ValidationError(_("This field must contains only numbers!"))
        return value
