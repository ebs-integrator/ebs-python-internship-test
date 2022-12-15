import logging
import traceback

from django.http import JsonResponse
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)


# Create your middleware here.


class ApiMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        request.LANGUAGE_CODE = translation.get_language()

    @staticmethod
    def process_exception(request, response):
        logger.error(traceback.format_exc())

        return JsonResponse(
            {
                "exception": str(response),
                "detail": _("Something Went Wrong. Please contact support"),
            },
            status=500,
        )
