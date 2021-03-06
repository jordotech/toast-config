# coding: utf-8

"""
    Toast Configuration API

    ## Overview    You can use the Toast configuration API to retrieve information about   the configuration of a restaurant and its menus. This includes   menu items, menu groups, and alternate payment types, as well as   physical configuration such as cash drawers and restaurant   tables.    The configuration API does not return information about entities   that you have removed from your restaurant configuration or   archived. For example, if you remove a menu item or archive a   discount, the configuration API will not return the menu item or   discount in response data.    For more information about using this and other Toast APIs, see   the <cite>Toast API Developer's Guide.</cite> 

    OpenAPI spec version: 2.2.0
    Contact: integrations@toasttab.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ServiceChargeCriteria(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'min_check_amount': 'float',
        'delivery': 'bool',
        'max_check_amount': 'float',
        'min_delivery_distance': 'float'
    }

    attribute_map = {
        'min_check_amount': 'minCheckAmount',
        'delivery': 'delivery',
        'max_check_amount': 'maxCheckAmount',
        'min_delivery_distance': 'minDeliveryDistance'
    }

    def __init__(self, min_check_amount=None, delivery=None, max_check_amount=None, min_delivery_distance=None):
        """
        ServiceChargeCriteria - a model defined in Swagger
        """

        self._min_check_amount = None
        self._delivery = None
        self._max_check_amount = None
        self._min_delivery_distance = None

        if min_check_amount is not None:
          self.min_check_amount = min_check_amount
        if delivery is not None:
          self.delivery = delivery
        if max_check_amount is not None:
          self.max_check_amount = max_check_amount
        if min_delivery_distance is not None:
          self.min_delivery_distance = min_delivery_distance

    @property
    def min_check_amount(self):
        """
        Gets the min_check_amount of this ServiceChargeCriteria.
        The service charge is only applicable if the pre-discount check is at least this amount.

        :return: The min_check_amount of this ServiceChargeCriteria.
        :rtype: float
        """
        return self._min_check_amount

    @min_check_amount.setter
    def min_check_amount(self, min_check_amount):
        """
        Sets the min_check_amount of this ServiceChargeCriteria.
        The service charge is only applicable if the pre-discount check is at least this amount.

        :param min_check_amount: The min_check_amount of this ServiceChargeCriteria.
        :type: float
        """

        self._min_check_amount = min_check_amount

    @property
    def delivery(self):
        """
        Gets the delivery of this ServiceChargeCriteria.
        True if the service charge is only applicable for deliveries.

        :return: The delivery of this ServiceChargeCriteria.
        :rtype: bool
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """
        Sets the delivery of this ServiceChargeCriteria.
        True if the service charge is only applicable for deliveries.

        :param delivery: The delivery of this ServiceChargeCriteria.
        :type: bool
        """

        self._delivery = delivery

    @property
    def max_check_amount(self):
        """
        Gets the max_check_amount of this ServiceChargeCriteria.
        The service charge is waived if the pre-discount check amount is more than this amount. A `null` value means this criteria is inapplicable.

        :return: The max_check_amount of this ServiceChargeCriteria.
        :rtype: float
        """
        return self._max_check_amount

    @max_check_amount.setter
    def max_check_amount(self, max_check_amount):
        """
        Sets the max_check_amount of this ServiceChargeCriteria.
        The service charge is waived if the pre-discount check amount is more than this amount. A `null` value means this criteria is inapplicable.

        :param max_check_amount: The max_check_amount of this ServiceChargeCriteria.
        :type: float
        """

        self._max_check_amount = max_check_amount

    @property
    def min_delivery_distance(self):
        """
        Gets the min_delivery_distance of this ServiceChargeCriteria.
        The service charge is only applicable to deliveries that are at least this distance. A `null` value means this criteria is inapplicable.

        :return: The min_delivery_distance of this ServiceChargeCriteria.
        :rtype: float
        """
        return self._min_delivery_distance

    @min_delivery_distance.setter
    def min_delivery_distance(self, min_delivery_distance):
        """
        Sets the min_delivery_distance of this ServiceChargeCriteria.
        The service charge is only applicable to deliveries that are at least this distance. A `null` value means this criteria is inapplicable.

        :param min_delivery_distance: The min_delivery_distance of this ServiceChargeCriteria.
        :type: float
        """

        self._min_delivery_distance = min_delivery_distance

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ServiceChargeCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
