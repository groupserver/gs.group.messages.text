# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals, print_function
from unittest import TestCase
from gs.group.messages.text.postbody import wrap_message


class TestWrapMessage(TestCase):
    def test_empty(self):
        'Ensure an empty string is empty when wrapped'
        r = wrap_message('')

        self.assertEqual('', r)

    def test_whitespace(self):
        'Ensure whitespace is collapsed'
        r = wrap_message('\n ')

        self.assertEqual('', r)

    def test_url(self):
        'Ensure that a URL with dashes is not split'
        msg = ('This is a long string that ends with a URL that has dashes '
               '<https://manu.ninja/dominant-colors-for-lazy-loading-images>')
        r = wrap_message(msg)

        expected = ('This is a long string that ends with a URL that has dashes\n'
                    '<https://manu.ninja/dominant-colors-for-lazy-loading-images>')
        self.assertEqual(expected, r)
