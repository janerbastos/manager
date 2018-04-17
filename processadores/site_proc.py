# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from manager.forms.site_forms import SiteRedesSociaisForm, SiteDesenvolvedorForm
from manager.models import UserSite


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


def _vincular_usuario_site(request, **kwargs):
    template = 'modal/ajax/forms.html'
    site = kwargs.get('site', None)
    usuarios_site = UserSite.objects.filter(site=site).values_list('user__id', flat=True).distinct()
    users = User.objects.filter(is_active=True).exclude(id__in=usuarios_site)
    if request.method == 'POST':
        list = request.POST.getlist('usuarios')
        for uid in list:
            user = User.objects.get(id=uid)
            user_site = UserSite(user=user, site=site)
            user_site.save()
        return redirect('manager:index')

    result = render_to_string(template, {'users': users, 'option': 'vincular-usuario-site'})

    data = {
        'result': result,
    }
    return JsonResponse(data)


def _desvincular_usuario_site(request, **kwargs):
    template = 'modal/ajax/forms.html'
    site = kwargs.get('site', None)
    users = UserSite.objects.filter(site=site)
    if request.method == 'POST':
        list = request.POST.getlist('usuarios')
        for uid in list:
            user = UserSite.objects.filter(site=site, user__id=uid)
            user.delete()
        return redirect('manager:index')

    result = render_to_string(template, {'users': users, 'option': 'desvincular-usuario-site'})

    data = {
        'result': result,
    }
    return JsonResponse(data)


def _view(request, **kwargs):
    action = kwargs.get('action', None)
    if action:
        if action == 'vincular-usuario-site':
            return _vincular_usuario_site(request, **kwargs)
        if action == 'desvincular-usuario-site':
            return _desvincular_usuario_site(request, **kwargs)
        return _update(request, **kwargs)
