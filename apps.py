# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class SheradConfig(AppConfig):
    name = 'manager'

    def ready(self):
        import shared.signals.database
