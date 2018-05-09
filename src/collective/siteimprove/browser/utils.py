from AccessControl.PermissionRole import rolesForPermissionOn
from AccessControl.Role import gather_permissions
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.SecurityInfo import ModuleSecurityInfo
from AccessControl.SecurityManagement import getSecurityManager
from Products.Five.browser import BrowserView


class AnonCanView(BrowserView):
    """Returns true if anonymous user can view content"""

    def __call__(self):
        """Can we see this"""
        return 'Anonymous' in rolesForPermissionOn('View', self.context)
