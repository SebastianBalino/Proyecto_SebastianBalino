from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}
        
        
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Correo Electrónico", required=True)
    first_name = forms.CharField(label="Nombre", max_length=30, required=False)
    last_name = forms.CharField(label="Apellido", max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
        
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['avatar']