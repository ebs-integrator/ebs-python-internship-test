import traceback

import logging

logger = logging.getLogger(__name__)

from django.conf.urls.i18n import is_language_prefix_patterns_used
from django.utils import translation
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


class ApiMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        urlconf = getattr(request, 'urlconf', settings.ROOT_URLCONF)
        i18n_patterns_used, prefixed_default_language = is_language_prefix_patterns_used(urlconf)
        language = translation.get_language_from_request(request, check_path=i18n_patterns_used)
        language_from_path = translation.get_language_from_path(request.path_info)
        if not language_from_path and i18n_patterns_used and not prefixed_default_language:
            language = settings.LANGUAGE_CODE
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

    @staticmethod
    def process_exception(request, response):
        logger.error(traceback.format_exc())

        return JsonResponse({
            'exception': str(response),
            'detail': 'Something Went Wrong. Please contact support',
            'data': response.__cause__
        }, status=500)
