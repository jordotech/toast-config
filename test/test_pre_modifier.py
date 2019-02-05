# coding: utf-8

"""
    Toast Configuration API

    ## Overview    You can use the Toast configuration API to retrieve information about   the configuration of a restaurant and its menus. This includes   menu items, menu groups, and alternate payment types, as well as   physical configuration such as cash drawers and restaurant   tables.    The configuration API does not return information about entities   that you have removed from your restaurant configuration or   archived. For example, if you remove a menu item or archive a   discount, the configuration API will not return the menu item or   discount in response data.    For more information about using this and other Toast APIs, see   the <cite>Toast API Developer's Guide.</cite> 

    OpenAPI spec version: 2.2.0
    Contact: integrations@toasttab.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.pre_modifier import PreModifier


class TestPreModifier(unittest.TestCase):
    """ PreModifier unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPreModifier(self):
        """
        Test PreModifier
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = swagger_client.models.pre_modifier.PreModifier()
        pass


if __name__ == '__main__':
    unittest.main()
