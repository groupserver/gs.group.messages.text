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
from gs.group.messages.text.postbody import (wrap_message, Wrapper, )
from .testmessage import (TestCaseMessage, )


class TestWrapper(TestCase):
    'Test the ``Wrapper`` class'
    def test_short_line(self):
        w = Wrapper(70)
        msg = 'Tonight on Ethel the Frog we look at violence.'
        r = w.wrap_line('Tonight on Ethel the Frog we look at violence.')

        self.assertEqual(msg, r)

    def test_empty(self):
        'Ensure an empty string is empty when wrapped'
        w = Wrapper(70)
        r = w.wrap_line('')

        self.assertEqual('', r)

    def test_whitespace(self):
        'Ensure whitespace is collapsed'
        w = Wrapper(70)
        r = w.wrap_line(' ')

        self.assertEqual('', r)

    def test_quote(self):
        'Ensure quoted text is wrapped with its quotation'
        w = Wrapper(70)
        l = ("> Kipling road was a sort of a typical East End street. People "
             "were in and out of each other's houses with each other's "
             "property all day long.")
        r = w.wrap_line(l)

        expected = ("> Kipling road was a sort of a typical East End street. People were in\n"
                    "> and out of each other's houses with each other's property all day\n"
                    "> long.")
        self.assertEqual(expected, r)

    def test_multi(self):
        'Ensure that multiple-quotes are wrapped correctly'
        'Ensure quoted text is wrapped with its quotation'
        w = Wrapper(70)
        l = (">>> Kipling road was a sort of a typical East End street. People "
             "were in and out of each other's houses with each other's "
             "property all day long.")
        r = w.wrap_line(l)

        expected = (">>> Kipling road was a sort of a typical East End street. People were\n"
                    ">>> in and out of each other's houses with each other's property all\n"
                    ">>> day long.")
        self.assertEqual(expected, r)


class TestWrapMessage(TestCaseMessage):
    'Test the ``wrap_message`` function.'

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
        with self.open_test_file('short.txt') as testIn:
            msg = testIn.read()
        r = wrap_message(msg)

        with self.open_test_file('short-expected.txt') as expectedIn:
            expected = expectedIn.read()
        self.assertEqual(expected, r)

    def _test_wrap_tricky(self):
        'Ensure we handle tricky messages from Mozilla Tunderbird'
        # --=mpj17=-- It seems as if Mozilla Thunderbird uses the HTML version of the message
        # for the bottom quoting, rather than the plain-text, and this causes no end of issues
        # with the splitting, and trying to find the bottom of the message.
        self.maxDiff = None
        with self.open_test_file('tricky.txt') as testIn:
            msg = testIn.read()
        r = wrap_message(msg)

        with self.open_test_file('tricky-expected.txt') as expectedIn:
            expected = expectedIn.read()
        self.assertEqual(expected, r)
