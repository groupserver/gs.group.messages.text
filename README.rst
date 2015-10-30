==========================
``gs.group.messages.text``
==========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Support for displaying the plain-text version of a post
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-10-30
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This product provides the utilities and functions that supports
the displaying of these posts, particularly the conversion of the
plain-text post to HTML.

The **actual** **rendering** of the messages is carried out in
either:

#.  `gs.group.messages.post.text.base`_ for the plain-text
    version of the post shown on the web, or
#.  `gs.group.list.email.html`_ for the HTML version of the
    plain-text message (the *pseudo* *HTML*) that is used in
    email messages.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.messages.text/
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

.. _gs.group.messages.post.text.base:
   https://github.com/groupserver/gs.group.messages.post.text.base
.. _gs.group.list.email.html:
   https://github.com/groupserver/gs.group.list.email.html
