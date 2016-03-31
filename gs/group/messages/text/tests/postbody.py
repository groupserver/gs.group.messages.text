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
from gs.group.messages.text.postbody import wrap_message
from .testmessage import TestCaseMessage


class TestWrapMessage(TestCaseMessage):
    def test_empty(self):
        'Ensure an empty string is empty when wrapped'
        r = wrap_message('')

        self.assertEqual('', r)

    def test_whitespace(self):
        'Ensure whitespace is collapsed'
        r = wrap_message('\n ')

        self.assertEqual('\n', r)

    def test_url(self):
        'Ensure that a URL with dashes is not split'
        msg = ('This is a long string that ends with a URL that has dashes '
               '<https://manu.ninja/dominant-colors-for-lazy-loading-images>')
        r = wrap_message(msg)

        expected = ('This is a long string that ends with a URL that has dashes\n'  # Note the \n
                    '<https://manu.ninja/dominant-colors-for-lazy-loading-images>')
        self.assertEqual(expected, r)

    def test_quote_simple(self):
        'Ensure that short-lines with quotes are left as is.'
        msg = ('Their nextdoor neighbor was Mrs April Simbol:\n'
               '> Kipling road was a sort of a typical East End street. People\n'
               '> were in and out of each other\'s houses with each other\'s\n'
               '> property all day long.')
        r = wrap_message(msg)

        self.assertEqual(msg, r)

    def test_wrap_simple_quoted(self):
        'Ensure simple bottom quoting is fine'
        self.maxDiff = None
        with self.open_test_file('short.txt') as testIn:
            msg = testIn.read()
        r = wrap_message(msg)

        with self.open_test_file('short-expected.txt') as expectedIn:
            expected = expectedIn.read()
        self.assertEqual(expected, r)

    def test_wrap_tricky(self):
        'Ensure we handle tricky messages from Mozilla Tunderbird'
        # --=mpj17=-- It seems as if Mozilla Thunderbird uses the HTML version of the message
        # for the bottom quoting, rather than the plain-text, and this causes no end of issues
        # with the splitting, and trying to find the bottom of the message.
