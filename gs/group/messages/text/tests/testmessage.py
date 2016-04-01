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
import codecs
from contextlib import contextmanager
import os
from pkg_resources import resource_filename


class TestMessage(object):
    'A mixin class that allows test-files to be opened easily'

    @staticmethod
    @contextmanager
    def open_test_file(filename):
        '''Open a test-file

:param str filename: The file name to open
:returns: The file, opened as a UTF-8 text-file.'''
        testname = os.path.join('tests', 'data', filename)
        fullname = resource_filename('gs.group.messages.text', testname)
        with codecs.open(fullname, 'r', encoding='utf-8') as infile:
            yield infile
