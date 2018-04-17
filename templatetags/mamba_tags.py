# -*- coding:UTF-8 -*-

from django import template
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import format_html

from mamba.models import Site
from manager.models import Grupo, UserSite

register = template.Library()


@register.assignment_tag()
def has_total_sites():
    return Site.objects.all().count()

@register.assignment_tag()
def has_total_usuarios():
    return User.objects.all().count()

@register.assignment_tag()
def has_total_grupos():
    return Grupo.objects.all().count()

@register.assignment_tag()
def has_usuarios_deste_site(site):
    users = UserSite.objects.filter(site=site)
    html = render_to_string('comum/include/conteudo_aux.html', {'users': users, 'option': 'user-site'})
    return format_html(html)