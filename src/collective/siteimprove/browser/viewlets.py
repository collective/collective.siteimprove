from collective.siteimprove.browser.controlpanel import ISiteimproveSchema
from plone.app.layout.viewlets import common as base
from plone.registry.interfaces import IRegistry
from zope.component import queryMultiAdapter, getUtility


class SIViewletCommon:

    def update_common(self):
        self.token = None
        self.recheck = False

        context_state = queryMultiAdapter((self.context, self.request),
                                          name=u'plone_context_state')
        self.canonical_url = context_state.canonical_object_url()

        # lookup token
        registry = getUtility(IRegistry)
        siteimprove_registry = registry.forInterface(ISiteimproveSchema, False)
        if siteimprove_registry:
            if getattr(siteimprove_registry, 'token', None):
                self.token = siteimprove_registry.token

            if getattr(siteimprove_registry, 'canonical_site_url', None):
                portal_state = queryMultiAdapter((self.context, self.request),
                                                 name=u'plone_portal_state')
                self.canonical_url = self.canonical_url.replace(
                    portal_state.portal_url().rstrip('/'),
                    siteimprove_registry.canonical_site_url.rstrip('/')
                )

        # check if a publish event proceeded this, if yes, inject site improve
        # recheck js code
        cookie = self.request.cookies.get("SI-Published", None)
        if cookie:
            self.recheck = True
            # clear the cookie
            self.request.response.expireCookie("SI-Published", path='/')


class SiteimproveJavascriptViewOnlyViewlet(base.ViewletBase, SIViewletCommon):
    """ This will render Siteimprove JavaScript load in <head>.
        <head> section is retrofitted only if the viewlet is enabled.
    """

    def update(self):
        super(SiteimproveJavascriptViewOnlyViewlet, self).update()
        self.view_only = True
        self.update_common()


class SiteimproveJavascriptViewlet(base.ViewletBase, SIViewletCommon):
    """ This will render Siteimprove JavaScript load in <head>.
        <head> section is retrofitted only if the viewlet is enabled.
    """

    def update(self):
        super(SiteimproveJavascriptViewlet, self).update()
        self.view_only = False
        self.update_common()
