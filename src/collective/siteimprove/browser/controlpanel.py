# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.statusmessages.interfaces import IStatusMessage
from logging import getLogger
from plone.app.registry.browser import controlpanel
from zope.interface import Interface
from zope import schema
from z3c.form import button
import requests

log = getLogger(__name__)


class ISiteimproveSchema(Interface):

    token = schema.TextLine(
        title=_(u'Token'),
        description=_(u'Configure Siteimprove Plugin token.'),
        required=True
    )


class SiteimproveControlPanelForm(controlpanel.RegistryEditForm):

    id = "SiteimproveControlPanel"
    label = _(u"Siteimprove Settings")
    schema = ISiteimproveSchema
    formErrorsMessage = _('Error fetching token from siteimprove.')

    buttons = controlpanel.RegistryEditForm.buttons.copy()

    @button.buttonAndHandler(_('Request new token'), name=None)
    def handleRequestNewToken(self, action):

        errors = {}
        data = {}

        # get plone version
        core_versions = getToolByName(aq_inner(self.context), 'portal_migration').coreVersions()
        version_string = 'Plone %s' % core_versions['Plone']

        # request new token
        try:
            response = requests.get("https://my2.siteimprove.com/auth/token", data={'cms': version_string })
            data = response.json()
        except (requests.exceptions.RequestException, ValueError):
            log.exception("Error fetching token from siteimprove.")

        if errors:
            self.status = self.formErrorsMessage
            return
        self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(
            _(u"Token received."),
            "info")
        self.request.response.redirect(self.request.getURL())


class SiteimproveControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SiteimproveControlPanelForm
