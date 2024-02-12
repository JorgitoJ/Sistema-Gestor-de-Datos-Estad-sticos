from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from app.views import InformePCRListarView, index, PrincipalTemplateView, LoginFormView, HojadeCargoView, InformePCRView,GestionView,AboutUsView, HojaDeCargoListarView

urlpatterns = [path('', index),
               path('login/', LoginFormView.as_view(), name='login'),
               path('logout/', LogoutView.as_view(), name='logout'),
               path('principal/', PrincipalTemplateView.as_view(), name='principal'),
               path("hojadecargo/",HojadeCargoView.as_view(), name="hojadecargo"),
               path("informepcr/", InformePCRView.as_view(), name="informepcr"),
               path("GestionarUser/", GestionView.as_view(), name="GestionarUser"),
               path("AboutUs/", AboutUsView.as_view(), name="AboutUs"),
               path("Mostrar/", HojaDeCargoListarView.as_view(), name="Mostrar"),
               path("mostrarpcr/", InformePCRListarView.as_view(), name="mostrarpcr"),
               
               
            ]    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
            