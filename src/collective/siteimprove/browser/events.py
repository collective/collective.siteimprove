from collective.siteimprove.interfaces import ICollectiveSiteimproveLayer
from zope.globalrequest import getRequest
from zope.component.hooks import getSite
import time
from email.Utils import formatdate


def triggerSiteimproveRecheck(obj, event):
    """ Sets cookie 'flag' to indicate that a publish workflow transition
        took place
    """
    if ICollectiveSiteimproveLayer.providedBy(getRequest()):
        if event.action == 'publish':
            # set cookie to indicate that a publish action took place
            request = getRequest()
            expiration_seconds = time.time() + (1*60*60) # 1 hour from now
            expires = formatdate(expiration_seconds, usegmt=True)
            request.response.setCookie("SI-Published", True, path='/', expires=expires)