# -*- coding: utf-8 -*-

from django.conf.urls import url

from manager.views import create_update_site, open_site, create_update_user, list_user
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^sites/create/$', create_update_site, name='create'),
    url(r'^sites/(?P<site_id>[-\w]+)/update/$', create_update_site, name='update'),
    url(r'^sites/(?P<site_id>[-\w]+)/$', open_site, name='open'),
    url(r'^usuarios/$', list_user, name='list_user'),
    url(r'^usuarios/create/$', create_update_user, name='create_user'),
    url(r'^usuarios/(?P<user_id>[\w.@+-]+)/update/$', create_update_user, name='update_user'),
    ]