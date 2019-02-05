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
from swagger_client.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_alternate_payment_types_get(self):
        """
        Test case for alternate_payment_types_get

        Returns an array of alternative forms of payment configured for a restaurant. 
        """
        pass

    def test_alternate_payment_types_guid_get(self):
        """
        Test case for alternate_payment_types_guid_get

        Returns information about an alternative form of payment configured for a restaurant. 
        """
        pass

    def test_cash_drawers_get(self):
        """
        Test case for cash_drawers_get

        Returns an array of information about cash drawers configured for a restaurant. 
        """
        pass

    def test_cash_drawers_guid_get(self):
        """
        Test case for cash_drawers_guid_get

        Returns information about a specific cash drawer device. 
        """
        pass

    def test_dining_options_get(self):
        """
        Test case for dining_options_get

        Returns an array of information about types of service offered by a restaurant. 
        """
        pass

    def test_dining_options_guid_get(self):
        """
        Test case for dining_options_guid_get

        Returns information about a specific type of service offered by a restaurant. 
        """
        pass

    def test_discounts_get(self):
        """
        Test case for discounts_get

        Returns an array of information about price deductions configured for a restaurant. 
        """
        pass

    def test_discounts_guid_get(self):
        """
        Test case for discounts_guid_get

        Returns information about a price deduction configured for a restaurant. 
        """
        pass

    def test_menu_groups_get(self):
        """
        Test case for menu_groups_get

        Returns an array of information about the sections of menus configured for a restaurant. 
        """
        pass

    def test_menu_groups_guid_get(self):
        """
        Test case for menu_groups_guid_get

        Returns information about a section within a menu. 
        """
        pass

    def test_menu_items_get(self):
        """
        Test case for menu_items_get

        Returns information about the items and modifiers available from a restaurant. 
        """
        pass

    def test_menu_items_guid_get(self):
        """
        Test case for menu_items_guid_get

        Returns information about an item or modifier available from a restaurant. 
        """
        pass

    def test_menu_option_groups_get(self):
        """
        Test case for menu_option_groups_get

        Returns information about the groups of modifier menu items configured for a restaurant. 
        """
        pass

    def test_menu_option_groups_guid_get(self):
        """
        Test case for menu_option_groups_guid_get

        Returns information about a group of modifier menu items. 
        """
        pass

    def test_menus_get(self):
        """
        Test case for menus_get

        Returns information about the menus configured for a restaurant. 
        """
        pass

    def test_menus_guid_get(self):
        """
        Test case for menus_guid_get

        Returns information about a menu configured for a restaurant. 
        """
        pass

    def test_no_sale_reasons_get(self):
        """
        Test case for no_sale_reasons_get

        Returns information about no sale reasons configured for a restaurant. 
        """
        pass

    def test_no_sale_reasons_guid_get(self):
        """
        Test case for no_sale_reasons_guid_get

        Returns information about a no sale reason configured for a restaurant. 
        """
        pass

    def test_payout_reasons_get(self):
        """
        Test case for payout_reasons_get

        Returns information about recurring cash expenses configured for a restaurant. 
        """
        pass

    def test_payout_reasons_guid_get(self):
        """
        Test case for payout_reasons_guid_get

        Returns information about a recurring cash expense configured for a restaurant. 
        """
        pass

    def test_pre_modifier_groups_get(self):
        """
        Test case for pre_modifier_groups_get

        Returns information about pre modifier groups configured for a restaurant. 
        """
        pass

    def test_pre_modifier_groups_guid_get(self):
        """
        Test case for pre_modifier_groups_guid_get

        Returns information about a pre modifier group configured for a restaurant. 
        """
        pass

    def test_pre_modifiers_get(self):
        """
        Test case for pre_modifiers_get

        Returns information about pre modifiers configured for a restaurant. 
        """
        pass

    def test_pre_modifiers_guid_get(self):
        """
        Test case for pre_modifiers_guid_get

        Returns information about a pre modifier configured for a restaurant. 
        """
        pass

    def test_price_groups_get(self):
        """
        Test case for price_groups_get

        Returns information about the variable price levels configured for items at a restaurant. 
        """
        pass

    def test_price_groups_guid_get(self):
        """
        Test case for price_groups_guid_get

        Returns information about a variable price level configured for items at a restaurant. 
        """
        pass

    def test_printers_get(self):
        """
        Test case for printers_get

        Returns information about the printer devices configured for a restaurant. 
        """
        pass

    def test_printers_guid_get(self):
        """
        Test case for printers_guid_get

        Returns information about a printer device configured for a restaurant. 
        """
        pass

    def test_restaurant_services_get(self):
        """
        Test case for restaurant_services_get

        Returns information about the types of menu and dining offered by a restaurant. 
        """
        pass

    def test_restaurant_services_guid_get(self):
        """
        Test case for restaurant_services_guid_get

        Returns information about a type of menu and dining offered by a restaurant. 
        """
        pass

    def test_revenue_centers_get(self):
        """
        Test case for revenue_centers_get

        Returns information about segments of restaurant income, for reporting. 
        """
        pass

    def test_revenue_centers_guid_get(self):
        """
        Test case for revenue_centers_guid_get

        Returns information about a segment of restaurant income, for reporting. 
        """
        pass

    def test_sales_categories_get(self):
        """
        Test case for sales_categories_get

        Returns information about types of menu item used to analyze purchases at a restaurant. 
        """
        pass

    def test_sales_categories_guid_get(self):
        """
        Test case for sales_categories_guid_get

        Returns information about a type of menu item used to analyze purchases at a restaurant. 
        """
        pass

    def test_service_areas_get(self):
        """
        Test case for service_areas_get

        Returns information about the physical settings that a restaurant serves customers in. 
        """
        pass

    def test_service_areas_guid_get(self):
        """
        Test case for service_areas_guid_get

        Returns information about a physical setting that a restaurant serves customers in. 
        """
        pass

    def test_service_charges_get(self):
        """
        Test case for service_charges_get

        Returns information about the types of fees applied to restaurant sales. 
        """
        pass

    def test_service_charges_guid_get(self):
        """
        Test case for service_charges_guid_get

        Returns information about a type of fee applied to restaurant sales. 
        """
        pass

    def test_tables_get(self):
        """
        Test case for tables_get

        Returns information about the dining tables configured for a restaurant. 
        """
        pass

    def test_tables_guid_get(self):
        """
        Test case for tables_guid_get

        Returns information about a dining table configured for a restaurant. 
        """
        pass

    def test_tax_rates_get(self):
        """
        Test case for tax_rates_get

        Returns information about the forms of taxation applied to sales at a restaurant. 
        """
        pass

    def test_tax_rates_guid_get(self):
        """
        Test case for tax_rates_guid_get

        Returns information about a form of taxation applied to sales at a restaurant. 
        """
        pass

    def test_void_reasons_get(self):
        """
        Test case for void_reasons_get

        Returns information about the causes for making a sale invalid configured for a restaurant. 
        """
        pass


if __name__ == '__main__':
    unittest.main()