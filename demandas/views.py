from django.shortcuts import render, redirect
from .models import Demanda  # Certifique-se de que o modelo foi importado corretamente
from .forms import UsuarioCadastroForm

def cadastro_usuario(request):
    if request.method == "POST":
        form = UsuarioCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redireciona para a página de login após cadastro
    else:
        form = UsuarioCadastroForm()

    return render(request, "demandas/cadastro_usuario.html", {"form": form})

def formulario_demanda(request):
    if request.method == "POST":
        nome_cliente = request.POST.get("nome_cliente")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        
        itens = {
            "geladeira": int(request.POST.get("geladeira", 0)),
            "sofá": int(request.POST.get("sofá", 0)),
            "máquina de lavar": int(request.POST.get("máquina de lavar", 0)),
            "cama": int(request.POST.get("cama", 0)),
            "mesa": int(request.POST.get("mesa", 0)),
            "cadeira": int(request.POST.get("cadeira", 0)),
            "caixa_pequena": int(request.POST.get("caixa_pequena", 0)),
            "caixa_media": int(request.POST.get("caixa_media", 0)),
            "caixa_grande": int(request.POST.get("caixa_grande", 0)),
        }

        # Criar e salvar a demanda
        demanda = Demanda(
            nome_cliente=nome_cliente,
            email=email,
            telefone=telefone,
            itens=itens
        )
        demanda.save()

        return redirect("sucesso")  # Certifique-se de ter uma rota 'sucesso'

    return render(request, "demandas/formulario.html")
