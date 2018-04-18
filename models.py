# -*- coding: UTF-8 -*-

from django.contrib.auth.admin import User
from django.db import models
from mamba.models import Site, ContentType

class UserSite(models.Model):
    user = models.ForeignKey(User)
    site = models.ForeignKey(Site, related_name='rel_sites')
    grupo = models.ManyToManyField('Grupo', related_name='rel_grupos_sites')

    class Meta:
        unique_together = (("user", "site"),)


class Grupo(models.Model):
    nome = models.CharField(max_length=60, unique=True)
    papeis = models.ManyToManyField('Papel', related_name='rel_papeis')

    def __unicode__(self):
        return self.nome


class GrupoPapel(models.Model):
    grupo = models.ForeignKey('Grupo', related_name='rel_grupos_papeis')
    papeis = models.ManyToManyField('Papel', related_name='rel_papeis_grupos')

    def __unicode__(self):
        return self.grupo.nome


class Papel(models.Model):
    nome = models.CharField(max_length=50)
    cod_name = models.SlugField(max_length=50, null=True)
    content_type = models.ForeignKey(ContentType, related_name='rel_contents', null=True)

    def __unicode__(self):
        return self.nome