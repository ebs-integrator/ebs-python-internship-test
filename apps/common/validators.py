from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


@deconstructible
class CustomNumericValidator:
    """
    This is example of custom validator.

    Validate that the input is a valid numeric value.

    Usage example:
    from apps.common.validators import CustomNumericValidator
    from django.db import models

    class MyModel(models.Model):
        my_field = models.CharField(max_length=255, validators=[CustomNumericValidator()])
    """

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, value: str):
        invalid_symbols = not value.isdigit()
        if invalid_symbols:
            raise ValidationError(_("This field must contains only numbers!"))
        return value
