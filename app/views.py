from tempfile import template
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from app.forms import HojaCargoForm, InformePCRForm
from app.models import HojaCargo, InformePCR



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="login")
    else:
        return HttpResponseRedirect(redirect_to="principal")


class LoginFormView(LoginView):
    form_class = LoginView.form_class
    template_name = "sign-in/login.html"
    success_url = reverse_lazy('principal')


class PrincipalTemplateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "index.html"
    permission_required = 'app.view_user'

class HojadeCargoView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = HojaCargo
    form_class = HojaCargoForm
    template_name= "hoja_de_cargo.html"
    success_url = reverse_lazy('Mostrar')
    permission_required = 'app.view_user'


class InformePCRView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = InformePCR
    template_name= "informe_PCR.html"    
    success_url = reverse_lazy('mostrarpcr')
    form_class = InformePCRForm
    permission_required = 'app.view_user'

class GestionView(TemplateView, PermissionRequiredMixin):
    template_name = "gestionaruser.html"
    permission_required = 'app.view_user'

class AboutUsView(TemplateView,PermissionRequiredMixin):
    template_name = "aboutus.html"
    permission_required = 'app.view_user'

class HojaDeCargoListarView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    template_name = "mostrar.html"
    model = HojaCargo
    permission_required = 'app.view_user'

class InformePCRListarView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = InformePCR
    template_name = "mostrarpcr.html"
    permission_required = 'app.view_user'

