import time
try:
    from email.utils import formatdate
except ImportError:
    from email.Utils import formatdate
from AccessControl.PermissionRole import rolesForPermissionOn
from zope.lifecycleevent import IObjectModifiedEvent
from Products.CMFCore.interfaces import IActionSucceededEvent
from zope.globalrequest import getRequest
from collective.siteimprove.interfaces import ICollectiveSiteimproveLayer


def triggerSiteimproveRecheck(obj, event):
    """ Sets cookie 'flag' to indicate that a recheck needs to take place
    """
    if ICollectiveSiteimproveLayer.providedBy(getRequest()):
        recheck = False

        if IObjectModifiedEvent.providedBy(event) and \
                'Anonymous' in rolesForPermissionOn('View', event.object):
            # object saved and publically visible
            recheck = True
        elif IActionSucceededEvent.providedBy(event):
            # workflow transition
            recheck = True

        if recheck:
            request = getRequest()
            expiration_seconds = time.time() + (1 * 60 * 60)  # 1 hour from now
            expires = formatdate(expiration_seconds, usegmt=True)
            request.response.setCookie("SI-Published", 'True', path='/',
                                       expires=expires)
