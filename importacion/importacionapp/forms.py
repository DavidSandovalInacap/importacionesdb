# aqui estoy importando clases necesarias para definir formularios
from django import forms
from .models import Importacion

class ImportacionForm(forms.ModelForm):
    # aqui estoy definiendo un formulario basado en el modelo Importacion
    class Meta:
        model = Importacion
        fields = '__all__'