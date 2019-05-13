from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

DEFAULT_FIELD = "pk"


class ObjectValidator(object):

    def __init__(self, model, field=None):
        self.model = model
        self.field = field if field else DEFAULT_FIELD

    def __call__(self, value):
        if self.field == DEFAULT_FIELD:
            value = ObjectIdValidator().__call__(value)

        message = _("This object not exists")
        try:
            if self.model.objects.filter(**{self.field: value}).count():
                return value
        except ValidationError:
            message = _("Validation error")
        raise serializers.ValidationError(message)


class ObjectIdSerializer(serializers.Serializer):
    object_id = serializers.CharField(min_length=24, max_length=24, required=True)


class ObjectIdValidator(object):

    def __call__(self, value):
        serializer = ObjectIdSerializer(data={
            'object_id': value
        })
        if not serializer.is_valid():
            raise serializers.ValidationError(serializer.errors.get('object_id'))

        return value
