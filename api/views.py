from django.shortcuts import render , redirect 
from .forms import RegistartionForm
from django.contrib import messages , auth 
from django.contrib.auth import logout ,authenticate 
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

def home(request):
    return render(request,'chat/index.html')


def room(request, room_name):
    access_token = request.session.get('access_token')

    if not access_token:
        return redirect('login')

    try:
        jwt_auth = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(access_token)
        user = jwt_auth.get_user(validated_token)
    except AuthenticationFailed:
        return redirect('login')

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'access_token': access_token
    })



def register(request):
    if request.method == "POST":
        form = RegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            messages.error(request, form.errors)
    else:
        form = RegistartionForm()
        

    context={
        'form':form,
    }
    return render(request,'chat/register.html',context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Buscar el usuario por email
            user = User.objects.get(email=email)
            # Autenticar usando username y password
            user = authenticate(username=user.username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                request.session['access_token'] = access_token
                auth.login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, 'Credenciales incorrectas')
        except User.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')
        return redirect('login')

    return render(request, 'chat/login.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')