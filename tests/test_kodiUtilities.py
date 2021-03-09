# -*- coding: utf-8 -*-
#

from resources.lib import kodiUtilities
import pytest
import mock
import sys

xbmc_mock = mock.Mock()
sys.modules['xbmc'] = xbmc_mock
xbmcgui_mock = mock.Mock()
sys.modules['xbmcgui'] = xbmcgui_mock
xbmcaddon_mock = mock.Mock()
sys.modules['xbmcaddon'] = xbmcaddon_mock


def test_notification():
    assert not xbmcgui_mock.Dialog().notification.called
    kodiUtilities.notification('header', 'message')
    assert xbmcgui_mock.Dialog().notification.called


def test_showSettings():
    assert not xbmcaddon_mock.Addon().openSettings.called
    kodiUtilities.showSettings()
    assert xbmcaddon_mock.Addon().openSettings.called
