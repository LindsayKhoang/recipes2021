from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.contrib import messages

from app.forms.app_authentication import AppAuthenticationForm


class AppLoginView(LoginView):
    form_class = AppAuthenticationForm
    template_name = "login.html"

    def form_valid(self, form):
        messages.success(self.request, "Connexion successful")
        return super().form_valid(form)


class AppLogoutView(LoginRequiredMixin, LogoutView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, _("You've benn logged out"))
        return super().dispatch(request, *args, **kwargs)
