from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from users.forms import UserRegisterForm, UserEditForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import UserEditForm, AvatarForm
from .models import Avatar


# Create your views here.
def login_request (request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "app/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})



def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"app/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})



@login_required
def editar_perfil(request):
    avatar, created = Avatar.objects.get_or_create(user=request.user)  # Asegura que cada usuario tenga un avatar

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)

        if form.is_valid():
            form.save()

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)

        if avatar_form.is_valid():
            avatar_form.save()

        return redirect('Inicio')  # Cambia 'Inicio' según el nombre de tu vista de inicio

    else:
        form = UserEditForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
        avatar_form = AvatarForm(instance=avatar)

    return render(request, 'users/editar_perfil.html', {
        'form': form,
        'password_form': password_form,
        'avatar_form': avatar_form,
    })
