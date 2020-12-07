#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2018  Diego Torres Milano
Created on 2020-12-03 by Culebra v15.7.0
                      __    __    __    __
                     /  \  /  \  /  \  /  \ 
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \ 
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
"""


import re
import sys
import os


import unittest

from com.dtmilano.android.viewclient import ViewClient, CulebraTestCase

TAG = 'CULEBRA'


class CulebraTests(CulebraTestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'debug': {}, 'startviewserver': True, 'compresseddump': True}
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.3, 'find-views-with-content-description': True, 'window': -1, 'orientation-locked': None, 'concertina-config': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': True, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'install-apk': None, 'drop-shadow': False, 'output': 'result', 'unit-test-method': None, 'interactive': False}
        cls.sleep = 5

    def setUp(self):
        super(CulebraTests, self).setUp()

    def tearDown(self):
        super(CulebraTests, self).tearDown()

    def preconditions(self):
        if not super(CulebraTests, self).preconditions():
            return False
        return True

    def testSomething(self):
        if not self.preconditions():
            self.fail('Preconditions failed')

        _s = CulebraTests.sleep
        _v = CulebraTests.verbose

        self.vc.dump(window=-1)
        self.vc.findViewWithContentDescriptionOrRaise(u'''More options''').touch("{u'index': u'3', u'selected': u'false', u'checked': u'false', u'clickable': u'true', u'package': u'de.azapps.mirakelandroid', u'text': u'', u'long-clickable': u'false', u'enabled': u'true', u'bounds': ((969, 77), (1080, 209)), u'content-desc': u'More options', u'focusable': u'true', u'focused': u'false', 'uniqueId': 'id/no_id/5', u'checkable': u'false', u'resource-id': u'', u'password': u'false', u'class': u'android.widget.ImageView', u'scrollable': u'false'}")
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.device.touchDip(258.18, 149.09, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.device.touchDip(25.45, 50.91, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.vc.findViewWithContentDescriptionOrRaise(u'''Search''').touch("{u'index': u'2', u'selected': u'false', u'checked': u'false', u'clickable': u'true', u'package': u'de.azapps.mirakelandroid', u'text': u'', u'long-clickable': u'true', u'enabled': u'true', u'bounds': ((837, 77), (969, 209)), u'content-desc': u'Search', u'focusable': u'true', u'focused': u'false', 'uniqueId': 'id/no_id/4', u'checkable': u'false', u'resource-id': u'de.azapps.mirakelandroid:id/menu_search', u'password': u'false', u'class': u'android.widget.TextView', u'scrollable': u'false'}")
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.vc.findViewByIdOrRaise("de.azapps.mirakelandroid:id/search_text").setText(u"abcd", "{u'index': u'0', u'selected': u'false', u'NAF': u'true', u'clickable': u'true', u'package': u'de.azapps.mirakelandroid', u'text': u'', u'long-clickable': u'true', u'enabled': u'true', u'bounds': ((154, 81), (948, 205)), u'content-desc': u'', u'focusable': u'true', u'focused': u'true', 'uniqueId': 'id/no_id/16', u'checkable': u'false', u'resource-id': u'de.azapps.mirakelandroid:id/search_text', u'password': u'false', u'class': u'android.widget.EditText', u'checked': u'false', u'scrollable': u'false'}")
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.vc.findViewByIdOrRaise("de.azapps.mirakelandroid:id/search_clear").touch("{u'index': u'1', u'selected': u'false', u'NAF': u'true', u'clickable': u'true', u'package': u'de.azapps.mirakelandroid', u'text': u'', u'long-clickable': u'false', u'enabled': u'true', u'bounds': ((870, 118), (920, 168)), u'content-desc': u'', u'focusable': u'true', u'focused': u'false', 'uniqueId': 'id/no_id/17', u'checkable': u'false', u'resource-id': u'de.azapps.mirakelandroid:id/search_clear', u'password': u'false', u'class': u'android.widget.Button', u'checked': u'false', u'scrollable': u'false'}")
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.device.touchDip(86.06, 783.03, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.vc.uiDevice.openQuickSettings()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.device.touchDip(86.06, 783.03, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.device.touchDip(200.0, 667.88, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)
        self.device.dragDip((80.0, 546.55), (287.27, 574.55), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)


if __name__ == '__main__':
    CulebraTests.main()

