from django.conf.urls import url, include

from saap.cerimonial.reports import ImpressoEnderecamentoContatoView,\
    RelatorioContatoAgrupadoPorProcessoView,\
    RelatorioContatoAgrupadoPorGrupoView
from saap.cerimonial.views import ContatoCrud, TelefoneCrud, EmailCrud,\
    DependenteCrud, LocalTrabalhoCrud, EnderecoCrud, FiliacaoPartidariaCrud,\
    EnderecoPerfilCrud, LocalTrabalhoPerfilCrud, EmailPerfilCrud,\
    TelefonePerfilCrud, DependentePerfilCrud, PerfilCrud, \
    TipoTelefoneCrud,\
    TipoEnderecoCrud, TipoEmailCrud, ParentescoCrud, EstadoCivilCrud,\
    TipoAutoridadeCrud, TipoLocalTrabalhoCrud, OperadoraTelefoniaCrud,\
    NivelInstrucaoCrud, PronomeTratamentoCrud, \
    ContatoFragmentFormPronomesView, StatusProcessoCrud, TopicoProcessoCrud,\
    ClassificacaoProcessoCrud, ProcessoMasterCrud, AssuntoProcessoCrud,\
    ContatoFragmentFormSearchView, ProcessoContatoCrud,\
    GrupoDeContatosMasterCrud

from .apps import AppConfig


app_name = AppConfig.name


urlpatterns = [

    url(r'^contatos/', include(
        ContatoCrud.get_urls() + TelefoneCrud.get_urls() +
        EmailCrud.get_urls() + DependenteCrud.get_urls() +
        LocalTrabalhoCrud.get_urls() + EnderecoCrud.get_urls() +
        FiliacaoPartidariaCrud.get_urls() + ProcessoContatoCrud.get_urls()
    )),

    url(r'^contato/ajax_search_radio_list',
        ContatoFragmentFormSearchView.as_view(),
        name='ajax_search_contatos'),


    url(r'^perfil/', include(
        EnderecoPerfilCrud.get_urls() +
        LocalTrabalhoPerfilCrud.get_urls() +
        EmailPerfilCrud.get_urls() +
        TelefonePerfilCrud.get_urls() +
        DependentePerfilCrud.get_urls() +
        PerfilCrud.get_urls()
    )),

    url(r'^grupos/', include(
        GrupoDeContatosMasterCrud.get_urls()
    )),

    url(r'^processos/', include(
        ProcessoMasterCrud.get_urls()
    )),
    

    url(r'^relatorios/enderecamentos',
        ImpressoEnderecamentoContatoView.as_view(),
        name='print_impressoenderecamento'),

    url(r'^relatorios/contatos_por_processo',
        RelatorioContatoAgrupadoPorProcessoView.as_view(),
        name='print_rel_contato_agrupado_por_processo'),

    url(r'^relatorios/contatos',
        RelatorioContatoAgrupadoPorGrupoView.as_view(),
        name='print_rel_contato_agrupado_por_grupo'),

    url(r'^sistema/tipoautoridade/(?P<pk>\d+)/pronomes_form',
        ContatoFragmentFormPronomesView.as_view(), name='list_pronomes'),

    url(r'^sistema/assuntoprocesso/',
        include(AssuntoProcessoCrud.get_urls())),

    url(r'^sistema/statusprocesso/',
        include(StatusProcessoCrud.get_urls())),
    url(r'^sistema/classificacaoprocesso/',
        include(ClassificacaoProcessoCrud.get_urls())),
    url(r'^sistema/topicoprocesso/',
        include(TopicoProcessoCrud.get_urls())),
    url(r'^sistema/tipotelefone/',
        include(TipoTelefoneCrud.get_urls())),
    url(r'^sistema/tipoendereco/',
        include(TipoEnderecoCrud.get_urls())),
    url(r'^sistema/tipoemail/',
        include(TipoEmailCrud.get_urls())),
    url(r'^sistema/parentesco/',
        include(ParentescoCrud.get_urls())),
    url(r'^sistema/estadocivil/',
        include(EstadoCivilCrud.get_urls())),
    url(r'^sistema/tipoautoridade/',
        include(TipoAutoridadeCrud.get_urls())),
    url(r'^sistema/tipolocaltrabalho/',
        include(TipoLocalTrabalhoCrud.get_urls())),
    url(r'^sistema/operadoratelefonia/',
        include(OperadoraTelefoniaCrud.get_urls())),
    url(r'^sistema/nivelinstrucao/',
        include(NivelInstrucaoCrud.get_urls())),
    url(r'^sistema/pronometratamento/',
        include(PronomeTratamentoCrud.get_urls())),

]
