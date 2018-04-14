# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from mamba.models import Site
from manager.forms.site_forms import SiteForm
from manager.processadores import site_proc, user_proc


def index(request):
    template = 'index.html'
    sites = Site.objects.all()
    total_sites = sites.count()

    context = {
        'titulo': 'Gestor de Sites',
        'page_nane': 'Gerenciador',
        'detail_page_name': 'você esta na página de administração do site.',
        'total_sites': total_sites,
        'sites': sites,
    }
    return render(request, template, context)


def create_update_site(request, site_id=None):
    template = 'comum/forms.html'
    site = None
    total_sites = Site.objects.all().count()
    action = 'Você esta criando um novo site.'
    if site_id:
        site = get_object_or_404(Site, url=site_id)
        action = 'Você esta editando um site.'
    form = SiteForm(request.POST or None, request.FILES or None, instance=site)
    if form.is_valid():
        site = form.save(commit=False)
        site.save()
        return redirect('manager:open', site_id=site.url)

    context = {
        'titulo': 'Gestor de Sites',
        'page_nane': 'Gerenciador',
        'detail_page_name': 'você esta criando um novo site.',
        'form': form,
        'action': action,
        'site': site,
        'total_sites': total_sites,
    }

    return render(request, template, context)


def open_site(request, site_id):
    template = 'comum/open.html'
    total_sites = Site.objects.all().count()
    site = get_object_or_404(Site, url=site_id)

    action = request.GET.get('action', None)
    if action:
        return site_proc._view(request, action=action, site=site)

    context = {
        'titulo': 'Gestor de Sites',
        'page_nane': site.url.upper(),
        'detail_page_name': 'Você esta configurando o site %s .' % site.titulo.encode('UTF-8'),
        'form': None,
        'action': site.url.upper(),
        'site': site,
        'total_sites': total_sites,
    }

    return render(request, template, context)


def create_update_user(request, user_id=None):
    if user_id:
        action = request.GET.get('action', None)
        if not action:
            action = 'update'
        return user_proc.view(request, action=action, user_id=user_id)
    else:
        return user_proc.view(request, action='create')


def list_user(request):
    return user_proc.view(request, action='list')

