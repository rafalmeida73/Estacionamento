from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa,
     Veiculo,
       MovRotativo,
        Mensalista,
         MovMensalista,
)

from .form import ( PessoaForm, VeiculoForm, MovRotForm, MensalistaForm,
     MovMesalForm
)

@login_required
def home(request):
    context = {'mensagem': 'ola mundo'}
    return render(request, 'core/index.html', context)

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas') 


@login_required
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form =  PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form    

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoas.html', data)


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id= id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})    

     
@login_required         
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)    

@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos') 

@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id= id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})

@login_required
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form =  VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form    

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)       

@login_required
def lista_movrotativos(request):
    form = MovRotForm()
    mov_rot = MovRotativo.objects.all()
    data = {'mov_rot': mov_rot, 'form': form}
    return render(
        request, 'core/lista_movrotativos.html', data )


@login_required
def movrot_novo(request):
    form = MovRotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos') 


@login_required
def movrotativos_update(request, id):
    data = {}
    mov_rot_up = MovRotativo.objects.get(id=id)
    form =  MovRotForm(request.POST or None, instance= mov_rot_up)
    data['mov_rot_up'] = mov_rot_up
    data['form'] = form    

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativos.html', data)


@login_required
def movrotativos_delete(request, id):
    mov_rotativo = MovRotativo.objects.get(id= id)
    if request.method == 'POST':
        mov_rotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_rotativo})


@login_required
def lista_mensalistas(request):
    form = MensalistaForm()
    mensalistas = Mensalista.objects.all()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(
        request, 'core/lista_mensalistas.html', data)


@login_required
def mensalistas_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id= id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})    

  
@login_required    
def mensalista_update(request, id):
    data = {}
    mensal_up = Mensalista.objects.get(id=id)
    form =  MensalistaForm(request.POST or None, instance= mensal_up)
    data['mensal_up'] = mensal_up
    data['form'] = form    

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
         return render(request, 'core/update_mensalista.html', data)  
               

@login_required
def lista_movmensalistas(request):
    form = MovMesalForm()
    mov_mensalista = MovMensalista.objects.all()
    data = {'mov_mensalista': mov_mensalista, 'form': form}
    return render(
        request, 'core/lista_movmensalista.html', data)


@login_required
def movmensal_novo(request):
    form = MovMesalForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


@login_required
def movmensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id= id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_mensalista})    


@login_required
def movmensalista_update(request, id):
    data = {}
    movmensal_up = MovMensalista.objects.get(id=id)
    form =  MovMesalForm(request.POST or None, instance= movmensal_up)
    data['movmensal_up'] = movmensal_up
    data['form'] = form    

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
         return render(request, 'core/update_movmensalista.html', data)