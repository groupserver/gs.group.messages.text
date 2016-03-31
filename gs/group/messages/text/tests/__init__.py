# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
#lint:disable
from .htmlbody import TestHTMLBody
from .matcher import TestMatcher
from .matcher import TestBoldMatcher
from .matcher import TestEmailMatcher
from .matcher import TestWWWMatcher
from .matcher import TestURIMatcher
from .splitmessage import TestSplitMessage
from .test_all import load_tests
#lint:enable
