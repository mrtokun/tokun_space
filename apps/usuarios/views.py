from django.shortcuts import render, redirect

from apps.usuarios.forms import LogonForms, CadastrarForms
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib import messages

def logon(request):

    form = LogonForms()
    if request.method == 'POST':
        form = LogonForms(request.POST)

        if form.is_valid():
            nome = form['nome_logon'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
        else:
            messages.error(request, "Usuário ou senha inválida!")
            return redirect('logon')                

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"Usuário {nome} autenticado com sucesso!")
            return redirect('index2')
        else:
            messages.error(request, "Usuário ou senha inválida!")
            return redirect('logon')


    return render(request, 'usuarios/logon.html', {"form": form})

def cadastrar(request):
    form = CadastrarForms()
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")        
        return redirect('logon')
    if request.method == 'POST':
        form = CadastrarForms(request.POST)
        # print(f'passou aqui 6')
        if form.is_valid():


            nome = form['nome'].value()
            email = form['email'].value()
            senha = form['senha_nova'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já cadastrado!")
                return redirect('cadastrar')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f"Usuário {nome} cadastrado com sucesso!")
            return redirect('logon')

    return render(request, 'usuarios/cadastrar.html', {"form": form})

def logoff(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")        
        return redirect('logon')    
    auth.logout(request)
    messages.success(request, "Logoff realizado com sucesso!")    
    return redirect('logon')