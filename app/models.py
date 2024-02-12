from datetime import datetime
import modulefinder
from msilib.schema import Class
from operator import length_hint
from xml.parsers.expat import model
from django.contrib.auth.models import  AbstractUser, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


SEXO_CHOICES = (
    ('F','Femenino'),
    ('M','Masculino'),
)    

class HojaCargo(models.Model):

    nombre=models.CharField(_("Nombre"), max_length=50)
    apellido=models.CharField(_("Apellidos"), max_length=50)
    edad=models.IntegerField(_("Edad"),max_length=3)
    sexo=models.CharField(_("Sexo"), max_length=1, choices=SEXO_CHOICES)
    direccion=models.CharField(_("Direccion"), max_length=50)
    padecimientos=models.CharField(_("Padecimientos"), max_length=50)
    fecha=models.DateField(_("FechaActual"), auto_now=True )

    class Meta:
        verbose_name = _("hoja de cargo")
        verbose_name_plural = _("hojas de cargo")

    def __str__(self):
        return self.nombre +' '+ self.apellido

    def get_absolute_url(self):
        return reverse("hojacargo_detail", kwargs={"pk": self.pk})

RESULTADO_CHOICE=(('P','Positivo'),
                  ('N','Negativo'),
) 

class InformePCR(models.Model):

    nombre=models.CharField(_("Nombre"), max_length=50)
    apellido=models.CharField(_("Apellidos"), max_length=50)
    fechais=models.DateField(_("FechaIS"), auto_now=False)
    fechatm=models.DateField(_("FechaTM"), auto_now=False)
    consultorio=models.IntegerField(_("Consultorio"))
    resultado=models.CharField(_("Resultado"), max_length=1, choices=RESULTADO_CHOICE)
    fecha=models.DateField(_("FechaActual"), auto_now=True )

    class Meta:
        verbose_name = _("Informe PCR")
        verbose_name_plural = _("Informes PCR")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("InformePCR_detail", kwargs={"pk": self.pk})
