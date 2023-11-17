from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class UserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            print('Работает!!!!!! Миксин!!!!!')
            return self.handle_no_permission()
        if request.user.is_authenticated:
            print('Работает Миксин!!!!!')
            if request.user != self.get_object().user or request.user.is_staff:
                messages.info(request, _('You do not have permission to change another user.'))
                return redirect('index')
        print('Работает Миксин!!!!!')
        return super().dispatch(request, *args, **kwargs)
