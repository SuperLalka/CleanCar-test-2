
from django import forms

from app.utils.admin_forms_fields import SVGAndImageFormField
from app.ws.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = []
        field_classes = {
            'file': SVGAndImageFormField,
        }
