# -*- coding:UTF-8 -*-

from django import template
from django.contrib.auth.models import User
from django.utils.html import format_html

from mamba.models import Site
from manager.models import Grupo

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