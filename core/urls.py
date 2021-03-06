from django.urls import path, include
from django.urls import include, re_path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrot_novo,
    mensalistas_novo,
    movmensal_novo,
    pessoa_update,
    veiculo_update,
    movrotativos_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativos_delete,
    mensalista_delete,
    movmensalista_delete,
    Pdf,
    PdfMensalista,
    PdfMovMensalista,
    PdfMovRotativo,
    PdfPessoas,
    ExportarParaCSV,
    CSVMensalista,
    CSVMovMensalista,
    CSVMovRotativo,
    CSVPessoas
)


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo', pessoa_novo, name='core_lista_pessoa_novo'),
    re_path(r'pessoa-update/(?P<id>\d+)/$', pessoa_update,
         name='core_pessoa_update'),
    re_path(r'pessoa-delete/(?P<id>\d+)/$', pessoa_delete,
         name='core_pessoa_delete'),


    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo', veiculo_novo, name='core_lista_veiculo_novo'),
    re_path(r'veiculo-update/(?P<id>\d+)/$', veiculo_update,
         name='core_veiculo_update'),
    re_path(r'veiculo-delete/(?P<id>\d+)/$', veiculo_delete,
         name='core_veiculo_delete'),


    path('mov_rot', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov_rot_novo', movrot_novo, name='core_lista_movrotativos_novo'),
    re_path(r'mov-rot-update/(?P<id>\d+)/$', movrotativos_update, 
        name='core_movrotativos_update'),
    re_path(r'mov-rot-delete/(?P<id>\d+)/$', movrotativos_delete,
         name='core_movrotativos_delete'),


    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalistas_novo', mensalistas_novo, name='core_lista_mensalistas_novo'),
    re_path(r'mensalista-update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    re_path(r'mensalista-delete/(?P<id>\d+)/$', mensalista_delete,
         name='core_mensalista_delete'),


    path('mov_mensalista', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('mov_mensal_novo', movmensal_novo, name='core_lista_movmensalista_novo'),
    re_path(r'mov-mensalista-update/(?P<id>\d+)/$', movmensalista_update, 
        name='core_movmensalista_update'),
    re_path(r'mov-mensalista-delete/(?P<id>\d+)/$', movmensalista_delete,
         name='core_movmensalista_delete'),


     path('relatorio', Pdf.as_view(), name='relatorio_pdf'),
     path('relatorio_mensalista', PdfMensalista.as_view(), name='relatorioMensalista_pdf'),
     path('relatorio_movmensalista', PdfMovMensalista.as_view(), name='relatorioMovMensalista_pdf'),
     path('relatorio_movrotativo', PdfMovRotativo.as_view(), name='relatorioMovRotativo_pdf'),
     path('relatorio_pessoas', PdfPessoas.as_view(), name='relatorioPessoas_pdf'),


     path('relatorio-csv', ExportarParaCSV.as_view(), name='relatorio_csv'),
     path('relatoriomensalista-csv', CSVMensalista.as_view(), name='relatorioMensalista_csv'),
     path('relatoriomovmensalista-csv', CSVMovMensalista.as_view(), name='relatorioMovMensalista_csv'),
     path('relatoriomovrotativo-csv', CSVMovRotativo.as_view(), name='relatorioMovRotativo_csv'),
     path('relatopessoas-csv', CSVPessoas.as_view(), name='relatorioPessoas_csv'),
     
]