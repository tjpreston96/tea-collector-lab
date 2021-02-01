from django.forms import ModelForm
from .models import Sweetening


class SweeteningForm(ModelForm):
    class Meta:
        model = Sweetening
        fields = ["date", "style"]
