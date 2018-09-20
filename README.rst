.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

======================
collective.siteimprove
======================

This package is a Plone add-on that provides integration with
`siteimprove.com <http://siteimprove.com>`_, a service for maintaining and improving website
content. Siteimprove provides customers with automated scans of their websites
which check for content quality, accessibility compliance, SEO, and
performance.  The add-on gives content editors immediate feedback on
the quality of pages that they publish, with a summary report provided
in a page overlay and links to more details. This lets Siteimprove
customers see problems while they are in the process of editing a page
on their Plone site, instead of getting emailed a report after the
fact and needing to click through links to fix things.

collective.siteimprove provides the integration with Siteimprove's
`CMS plugin <https://siteimprove.com/en-us/core-platform/integrations/cms-plugin/>`_
API that is required to provide these features. The only thing Plone
admins need to do is install the add-on and configure a Siteimprove
token.

For more information on using Siteimprove within Plone, 
see `How to navigate the Siteimprove CMS Plugin
<https://support.siteimprove.com/hc/en-gb/articles/115000075451-How-to-navigate-the-Siteimprove-CMS-Plugin>`_.

Features
--------

- Control panel for requesting and saving a siteimprove.com token
- Siteimprove overlay button shows for authorized users on all default views
- Overlay button provides link to login/logoout to Siteimprove account
- Overlay button can show summary info for the domain or info for the page
  you are on, for publicly visible content
- Overlay button provides link to manually trigger page recheck action 
- Overlay button provides link to re-crawl site 
- Publishing or saving a published page triggers recheck action

Installation
------------

Install collective.siteimprove by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.siteimprove


and then running ``bin/buildout``.

Install the Add-on from the Plone Add-ons control panel under Site Setup.
Then go to the Siteimprove control panel and request a new token
(or paste in an existing one), and save.


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.siteimprove/issues
- Source Code: https://github.com/collective/collective.siteimprove


License
-------

The project is licensed under the GPLv2.
