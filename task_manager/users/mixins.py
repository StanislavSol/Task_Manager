from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.db.models import ProtectedError


class RulesMixin(AccessMixin):
    def has_permission(self):
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                    self.request,
                    _('You are not authorized! Please log in.')
                    )
            return redirect('login')
        elif not self.has_permission():
            messages.error(
                    self.request,
                    _('You do not have permission to change another user.')
                    )
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
