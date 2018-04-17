# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm

from mamba.models import Site


class SiteForm(ModelForm):
    url = forms.CharField(required=False, max_length=150, label='URL')

    class Meta:
        model = Site
        fields = (
            'url', 'titulo', 'descricao', 'email', 'telefone', 'workflow', 'status', 'favicon', 'logo', 'banner_topo'
        )
        labels = {
            'url': 'URL',
            'titulo': 'Título do Site',
            'descricao': 'Descrição do Site',
            'email': 'Emial de contato',
            'telefone': 'Telefone de contato',
            'workflow': 'Categoria do site',
            'status': 'Status do site',
            'favicon': 'Favicon do site',
            'logo': 'Brazão',
            'banner_topo': 'Banner de Destaque',
        }


class SiteRedesSociaisForm(ModelForm):
    class Meta:
        model = Site
        fields=('facebook_link', 'twitter_link', 'youtube_link', 'google_link', 'flicker_link', 'rss_link')
        labels = {
            'facebook_link': 'Facebook',
            'twitter_link': 'Twitter',
            'youtube_link': 'YouTube',
            'google_link': 'Google+',
            'flicker_link': 'Flicker',
            'rss_link': 'RSS',
        }

class SiteDesenvolvedorForm(ModelForm):
    class Meta:
        model = Site
        fields = ('texto_rodape', 'facebook_cod', 'twitter_cod', 'youtube_cod', 'google_cod', 'flicker_cod', 'analytic_cod',
                  'analytic_cod', 'html_cod')
        labels = {
            'facebook_cod': 'Facebook',
            'twitter_cod': 'Twitter',
            'youtube_cod': 'YouTube',
            'google_cod': 'Google+',
            'flicker_cod': 'Flicker',
            'analytic_cod': 'Estatisticas do site',
            'html_cod': 'Conteúdo estático html',
            'texto_rodape': 'Texto estático rodapé',
        }

        widgets = {
            'texto_rodape': forms.Textarea(attrs={'class':'ckeditor'})
        }