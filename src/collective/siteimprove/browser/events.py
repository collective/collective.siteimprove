from collective.siteimprove.interfaces import ICollectiveSiteimproveLayer
from zope.globalrequest import getRequest
from zope.component.hooks import getSite

def triggerSiteimproveRecheck(obj, event):
    """ Sets session 'flag' to indicate that a publish workflow transition
        took place
    """
    if ICollectiveSiteimproveLayer.providedBy(getRequest()):
        session_manager = getSite().session_data_manager
        session = session_manager.getSessionData()
        if event.action == 'publish':
            # set flag in the session
            session['SI-Published'] = True