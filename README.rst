.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

======================
collective.siteimprove
======================

This product provides integration with siteimprove.com

Features
--------

- Control panel for requesting and saving siteimprove.com token
- Register domain with siteimprove.com and show toolbar
- Siteimprove recheck action in plone toolbar for authorized users

This is a work in progress.


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
(or paste in an existing one), and save. The toobar and action should be
available to Site Administrators and Managers (the permission can be
delegated to other roles), on any content that is publicly visible.


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.siteimprove/issues
- Source Code: https://github.com/collective/collective.siteimprove


License
-------

The project is licensed under the GPLv2.