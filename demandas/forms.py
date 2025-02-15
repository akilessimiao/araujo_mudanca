from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class UsuarioCadastroForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=255, required=True)
    endereco = forms.CharField(widget=forms.Textarea, required=True)
    cpf = forms.CharField(max_length=14, required=True)
    telefone = forms.CharField(max_length=15, required=True)
    is_whatsapp = forms.BooleanField(required=False, label="Número é WhatsApp?")

    class Meta:
        model = UsuarioPersonalizado
        fields = ["username", "nome_completo", "endereco", "cpf", "telefone", "is_whatsapp", "password1", "password2"]
