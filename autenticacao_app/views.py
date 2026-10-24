from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


class VRegistro(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'login/pagina_login.html',{'form':form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()

            login(request,usuario)
            return redirect('home')
        else:
            for mgs in form.error_messages:
                messages.error(request,form.error_messages[mgs])
            return render(request,'login/pagina_login.html',{'form':form})


def encerar_sessao(request):
    logout(request)
    return redirect('home')


def pagina_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nome_usuario = form.cleaned_data.get("username")
            senha = form.cleaned_data.get("password")

            usuario = authenticate(
                username=nome_usuario,
                password=senha
            )

            if usuario is not None:
                login(request, usuario)
                return redirect('home')

            else:
                messages.error(request,'esse usuario não e valido!.')
        else:
            messages.error(request,'informação incorreta.')


    form = AuthenticationForm()
    return render(request,'login_usuario/login_usuario.html',{'form':form})
