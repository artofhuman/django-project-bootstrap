# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class ProjectDashboard(Dashboard):

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        current_site = Site.objects.get_current()

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        # ...

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Menu'),
            column=2,
            children=[
                {
                    'title': _('Go to site'),
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
