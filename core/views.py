from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
import csv
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


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', 
        params, 'relatorio_veiculos')


class PdfMensalista(View):

    def get(self, request):
        mensalistas = Mensalista.objects.all()
        params = {
            'mensalistas': mensalistas,
            'request': request,
        }
        return Render.render('core/relatorioMensalistas.html', 
        params, 'relatorio_mensalistas')


class PdfMovMensalista(View):

    def get(self, request):
        movmensalistas = MovMensalista.objects.all()
        params = {
            'movmensalistas': movmensalistas,
            'request': request,
        }
        return Render.render('core/relatorioMovMensalistas.html', 
        params, 'relatorio_movmensalistas')


class PdfMovRotativo(View):

    def get(self, request):
        movrotativo = MovRotativo.objects.all()
        params = {
            'movrotativo': movrotativo,
            'request': request,
        }
        return Render.render('core/relatorioMovRotativo.html', 
        params, 'relatorio_movrotativo')


class PdfPessoas(View):

    def get(self, request):
        pessoas = Pessoa.objects.all()
        params = {
            'pessoas': pessoas,
            'request': request,
        }
        return Render.render('core/relatorioPessoas.html', 
        params, 'relatorio_pessoas')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="veiculos.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response 


class CSVMensalista(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mensalistas.csv"'

        mensal = Mensalista.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'veiculo', 'Valor mes'])

        for mensalistas in mensal:
            writer.writerow(
                [mensalistas.id, mensalistas.veiculo, mensalistas.valor_mes])

        return response   


class CSVMovMensalista(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="movimento_mensalistas.csv"'

        movMensal = MovMensalista.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Mensalista', 'Data pgto', 'Total'])

        for mensalistas in movMensal:
            writer.writerow(
                [mensalistas.id, mensalistas.mensalista, mensalistas.dt_pgto, mensalistas.total])

        return response  


class CSVMovRotativo(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="movimento_rotativo.csv"'

        movRot = MovRotativo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Checkin', 'Checkout', 'Valor hora', 'Veiculo', 'Pago'])

        for rotativo in movRot:
            writer.writerow(
                [rotativo.id, rotativo.checkin, rotativo.checkout, rotativo.valor_hora, rotativo.veiculo, rotativo.Pago])

        return response   
  

class CSVPessoas(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pessoas.csv"'

        pessoa = Pessoa.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Nome', 'Endereço', 'Telefone'])

        for pessoas in pessoa:
            writer.writerow(
                [pessoas.id, pessoas.nome, pessoas.endereco, pessoas.telefone])

        return response   
  
