from django.utils.translation import gettext_lazy as _
from django.views import View
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request


class ReadOnly(BasePermission):
    """
    This is an example of a custom permission class. This permission only allows read-only access to a view.
    """

    message = _("You do not have permission to perform this action.")

    def has_permission(self, request: Request, view: View) -> bool:
        return request.method in SAFE_METHODS
