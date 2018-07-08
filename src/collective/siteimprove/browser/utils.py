from AccessControl.PermissionRole import rolesForPermissionOn
from AccessControl.Role import gather_permissions
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.SecurityInfo import ModuleSecurityInfo
from AccessControl.SecurityManagement import getSecurityManager
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.Five.browser import BrowserView


class AnonCanView(BrowserView):
    """Returns true if anonymous user can view content"""

    def __call__(self):
        """Can we see this"""
        return 'Anonymous' in rolesForPermissionOn('View', self.context)
class UseDomainView(BrowserView):
    """Returns true if the domain function is to be used in the siteimprove js header
       false implies that input function will be used instead"""

    def __call__(self):
        use_domain = False # use input function by default

        # figure out if domain function should be used instead
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        site = portal_state.portal() #site root
        site_path = site.getPhysicalPath();
        context_path = self.context.getPhysicalPath()

        # XXX This is not correct -- fix method to calculate when we are at root of site
        if context_path == site_path:
            use_domain == True
        if IPloneSiteRoot.providedBy(self.context):
            use_domain == True

        return use_domain