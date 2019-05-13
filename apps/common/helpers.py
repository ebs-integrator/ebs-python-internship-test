from collections import OrderedDict

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

from collections.abc import Iterable
from typing import Dict, List

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import traceback

DICTIONARY_TYPES = [dict, OrderedDict, ReturnDict]
LIST_TYPES = [list, ReturnList]

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Enjoy",
    ),
    validators=['ssv'],
    public=True,
    permission_classes=(AllowAny,)
)


def send_html_message(emails: List, title: str, template_path: str, context: Dict) -> None:
    """
    Send email by text template
    :param title: title message
    :param emails: list of receivers
    :param template_path: path to template, from templates/emails folder
    :param context: some context for template
    :return: boolean value
    Example : send_html_message(
                                ["iurii.ebs@gmail.com", ],
                                "Title test",
                                "emails/template_message.html",
                                {"test_text": "test test test"}
                                )
    """
    if isinstance(emails, str) or not isinstance(emails, Iterable):
        emails = [emails]
    html = render_to_string(template_path, context)

    msg = EmailMessage(
        title,
        html,
        to=emails,
        from_email='Tribes <%s>' % settings.EMAIL_HOST_USER
    )
    msg.content_subtype = 'html'
    try:
        msg.send()
    except Exception:
        traceback.print_exc()


def elastic_text_search(field: str, value: str):
    return {
        'bool': {
            "should": [
                {
                    'match': {
                        field: {
                            'query': value,
                            'operator': 'or'
                        }
                    }
                },
                {
                    'bool': {
                        'must': [
                            {'prefix': {
                                field: item
                            }} for item in value.lower().split(' ')
                        ]
                    }
                },
                {
                    "fuzzy": {
                        field: {
                            "value": value,
                            "boost": 1.0,
                            "fuzziness": 2,
                            "prefix_length": 0,
                            "max_expansions": 100
                        }
                    }
                }
            ]
        }
    }
