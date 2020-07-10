# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.statusmessages.interfaces import IStatusMessage
from logging import getLogger
from plone.app.registry.browser import controlpanel
from zope.i18nmessageid import MessageFactory
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

    canonical_site_url = schema.URI(
        title=_(u'Public Site URL'),
        description=_(u'Set this if your public site url is different, '
                      u'from the url used by content editors.'),
        required=False,
    )


class SiteimproveControlPanelForm(controlpanel.RegistryEditForm):

    id = "SiteimproveControlPanel"
    label = _(u"Siteimprove Settings")
    schema = ISiteimproveSchema
    formErrorsMessage = _('Error fetching token from siteimprove.')

    @button.buttonAndHandler(_(u"Save"), name='save')
    def handleSave(self, action):
        super(SiteimproveControlPanelForm, self).handleSave(self, action)

    @button.buttonAndHandler(_('Request new token'), name='token')
    def handleRequestNewToken(self, action):
        # get plone version
        core_versions = getToolByName(aq_inner(self.context),
                                      'portal_migration').coreVersions()
        version_string = 'Plone %s' % core_versions['Plone']

        # request new token
        try:
            response = requests.get("https://my2.siteimprove.com/auth/token",
                                    data={'cms': version_string})
            response_data = response.json()
            if response_data.get('token'):
                self.request.form['form.widgets.token'] = response_data['token']
        except (requests.exceptions.RequestException, ValueError):
            log.exception("Error fetching token from siteimprove.")

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(
            _(u"Token received."),
            "info"
        )
        self.request.response.redirect(self.request.getURL())

    @button.buttonAndHandler(_(u"Cancel"), name='cancel')
    def handleCancel(self, action):
        super(SiteimproveControlPanelForm, self).handleCancel(self, action)

    def updateActions(self):
        super(SiteimproveControlPanelForm, self).updateActions()
        self.actions['token'].addClass("context")


class SiteimproveControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SiteimproveControlPanelForm
