# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2013, 2014, 2015, 2016 OnlineGroups.net and
# Contributors.
#
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
from re import compile as re_compile
from textwrap import TextWrapper

# this is currently the hard limit on the number of word's we will process.
# after this we insert a message. TODO: make this more flexible by using
# AJAX to incrementally fetch large emails
EMAIL_WORD_LIMIT = 5000


class Wrapper(object):
    #: What to break the words on. It is based on the one inside the
    #: :class:`textwrap.TextWrapper` class, but without the breaking on '-'.
    splitExp = re_compile(r'(\s+|(?<=[\w\!\"\'\&\.\,\?])-{2,}(?=\w))')

    #: How to identify quotes
    quoteExp = re_compile(r'(>+\ +)')

    def __init__(self, width):
        self.email_wrapper = TextWrapper(
            width=width, expand_tabs=False, replace_whitespace=False, break_on_hyphens=False,
            break_long_words=False)
        self.email_wrapper.wordsep_re = self.splitExp

        self.quote_wrapper = TextWrapper(
            expand_tabs=False, replace_whitespace=False, break_on_hyphens=False,
            break_long_words=False)
        self.quote_wrapper.wordsep_re = self.splitExp

    def wrap_line(self, l):
        m = self.quoteExp.match(l)
        if m:
            # Quotation wrap
            quoteChars = m.group(1)
            self.quote_wrapper.subsequent_indent = quoteChars
            retval = self.quote_wrapper.fill(l)
        else:
            # Normal wrap
            retval = self.email_wrapper.fill(l)
        return retval


def wrap_message(messageText, width=79):
    """Word-wrap the message

:param str messageText: The text to alter.
:param int width: The column-number which to wrap at.
:returns: The wrapped text.
:rtype: str

.. Note: Originally a stand-alone script in
         ``Presentation/Tofu/MailingListManager/lscripts``."""
    wrapper = Wrapper(width)
    filledLines = [wrapper.wrap_line(l) for l in messageText.split('\n')]
    retval = '\n'.join(filledLines)
    return retval
