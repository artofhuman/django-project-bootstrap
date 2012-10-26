# -*- coding: utf-8 -*-
#author: Semen Pupkov (semen.pupkov@gmail.com)

"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'youcanbuy.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class ProjectDashboard(Dashboard):
    """
    Custom index dashboard for {{ project_name }}
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        current_site = Site.objects.get_current()

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            u'Приложения',
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            u'Администрирование',
            column=1,
            collapsible=False,
            models=('django.contrib.*', 'youcanbuy.apps.account.models.YoucanbuyUser'),
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            u'Меню',
            column=2,
            children=[
                {
                    'title': 'Перейти на сайт',
                    'url': 'http://' + current_site.domain,
                    'external': True,
                }
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))
