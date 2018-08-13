from AccessControl.PermissionRole import rolesForPermissionOn
from Products.Five.browser import BrowserView


class AnonCanView(BrowserView):
    """Returns true if anonymous user can view content"""

    def __call__(self):
        """Can we see this"""
        return 'Anonymous' in rolesForPermissionOn('View', self.context)


class UseDomainView(BrowserView):
    """  Returns true if the domain function is to be used in the
         siteimprove js header false implies that input function will
         be used instead
    """

    def __call__(self):
        # figure out if domain or input function should be used

        # if the view is an add or edit form use input
        # 'edit' covers: 'edit', 'base_edit','atct_edit','@@edit',
        #                adding archetype objects
        #                editing archetype and dexterity objects
        # 'add' covers:  adding dexterity objects
        filter_strings = ['edit', 'add']
        for x in filter_strings:
            if x in self.request.URL:
                return False  # use input

        # otherwise use domain
        return True
