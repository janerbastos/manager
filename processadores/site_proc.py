# -*- coding: UTF-8 -*-

from django.shortcuts import redirect, render

from manager.forms.site_forms import SiteRedesSociaisForm, SiteDesenvolvedorForm


def _create(request, **kwargs):
    pass


def _update(request, **kwargs):
    template = 'comum/forms.html'
    site = kwargs.get('site', None)
    form = None
    action = kwargs.get('action', None)
    if action=='redes-sociais':
        form = SiteRedesSociaisForm(request.POST or None, instance=site)
        action = 'Redes Sociais'
    elif action=='desenvolvedor':
        form = SiteDesenvolvedorForm(request.POST or None, instance=site)
        action = 'Desenvolvedor'
    if form.is_valid():
        rede_social = form.save(commit=False)
        rede_social.save()
        return redirect('manager:open', site_id=site.url)

    context = {
        'titulo': 'Gestor de Sites',
        'page_nane': site.url.upper(),
        'detail_page_name': 'Você esta configurando o site %s .' % site.titulo.encode('UTF-8'),
        'form': form,
        'action': '%s - %s' % (site.url.upper(), action),
        'site': site,
        }

    return render(request, template, context)

def _view(request, **kwargs):
    action = kwargs.get('action', None)
    if action:
        return _update(request, **kwargs)
