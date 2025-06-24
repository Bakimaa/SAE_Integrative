from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class DataForm(ModelForm):
    class Meta:
        model = models.Data
        fields = ('date', 'heure')
        labels = {
            'date' : _('Date'),
            'heure' : _('Heure'),
        }

class CapteurForm(ModelForm):
    class Meta:
        model = models.Capteur
        fields = ('nom', 'lieu', 'emplacement')
        labels = {
            'nom' : _('Nom'),
            'lieu' : _('Lieu'),
            'emplacement' : _('Emplacement')
        }
