from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class UserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authorized! Please log in.'))
            return redirect('users_login')
        if request.user.is_authenticated:
            if request.user != self.user_id:
                messages.error(request, _('You do not have permission to change another user.'))
                return redirect('users_index')
        print(request.user.is_authenticated)
        return super().dispatch(request, *args, **kwargs)
