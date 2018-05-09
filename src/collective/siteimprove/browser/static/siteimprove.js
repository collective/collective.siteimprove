/**
 * Contains the Siteimprove integration methods.
 */
define([
    'jquery'
  ], function ($) {
    'use strict';
    var Siteimprove = {
      input: function () {
        this.url = $('body').data('base-url');
        this.method = 'input';
        this.call();
      },
      domain: function () {
        this.url = $('body').data('portal-url');
        this.method = 'domain';
        this.call();
      },
      recheck: function () {
        this.url = $('body').data('base-url');
        this.method = 'recheck';
        this.call();
      },
      recrawl: function () {
        this.url = $('body').data('portal-url');
        this.method = 'recrawl';
        this.call();
      },
      call: function () {
        if (window._siteimprove_token) {
            var _si = window._si || [];
            _si.push([this.method, this.url, window._siteimprove_token]);
        }
      },
    };
    return Siteimprove;
  });
