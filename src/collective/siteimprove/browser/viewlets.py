from collective.siteimprove.browser.controlpanel import ISiteimproveSchema
from plone.app.layout.viewlets import common as base
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class SiteimproveJavascriptViewlet(base.ViewletBase):
    """ This will render Siteimprove JavaScript load in <head>.
        <head> section is retrofitted only if the viewlet is enabled.
    """

    def update(self):
        super(SiteimproveJavascriptViewlet, self).update()

        self.token = None
        self.recheck = False

        # lookup token
        registry = getUtility(IRegistry)
        siteimprove_registry = registry.forInterface(ISiteimproveSchema, False)
        if siteimprove_registry and siteimprove_registry.token:
            self.token = siteimprove_registry.token

        # check if a publish event proceeded this, if yes, inject site improve recheck js code
        cookie = self.request.cookies.get("SI-Published", None)
        if cookie:
            self.recheck = True
            # clear the cookie
            self.request.response.expireCookie("SI-Published", path='/')