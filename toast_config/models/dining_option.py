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


class DiningOption(object):
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
        'guid': 'str',
        'entity_type': 'str',
        'external_id': 'str',
        'name': 'str',
        'behavior': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'entity_type': 'entityType',
        'external_id': 'externalId',
        'name': 'name',
        'behavior': 'behavior'
    }

    def __init__(self, guid=None, entity_type=None, external_id=None, name=None, behavior=None):
        """
        DiningOption - a model defined in Swagger
        """

        self._guid = None
        self._entity_type = None
        self._external_id = None
        self._name = None
        self._behavior = None

        self.guid = guid
        self.entity_type = entity_type
        if external_id is not None:
          self.external_id = external_id
        if name is not None:
          self.name = name
        if behavior is not None:
          self.behavior = behavior

    @property
    def guid(self):
        """
        Gets the guid of this DiningOption.
        The GUID maintained by the Toast POS.

        :return: The guid of this DiningOption.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this DiningOption.
        The GUID maintained by the Toast POS.

        :param guid: The guid of this DiningOption.
        :type: str
        """
        if guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")

        self._guid = guid

    @property
    def entity_type(self):
        """
        Gets the entity_type of this DiningOption.
        The type of object this is.

        :return: The entity_type of this DiningOption.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DiningOption.
        The type of object this is.

        :param entity_type: The entity_type of this DiningOption.
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")

        self._entity_type = entity_type

    @property
    def external_id(self):
        """
        Gets the external_id of this DiningOption.
        External identifier string, prefixed by the naming authority.

        :return: The external_id of this DiningOption.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this DiningOption.
        External identifier string, prefixed by the naming authority.

        :param external_id: The external_id of this DiningOption.
        :type: str
        """

        self._external_id = external_id

    @property
    def name(self):
        """
        Gets the name of this DiningOption.
        The name of the dining option.

        :return: The name of this DiningOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DiningOption.
        The name of the dining option.

        :param name: The name of this DiningOption.
        :type: str
        """

        self._name = name

    @property
    def behavior(self):
        """
        Gets the behavior of this DiningOption.
        The behavior of the dining option. `TAKE_OUT` and `DELIVERY` require a `customer` to be specified on the order, and `DELIVERY` requires a `deliveryInfo` value. 

        :return: The behavior of this DiningOption.
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """
        Sets the behavior of this DiningOption.
        The behavior of the dining option. `TAKE_OUT` and `DELIVERY` require a `customer` to be specified on the order, and `DELIVERY` requires a `deliveryInfo` value. 

        :param behavior: The behavior of this DiningOption.
        :type: str
        """
        allowed_values = ["DINE_IN", "TAKE_OUT", "DELIVERY"]
        if behavior not in allowed_values:
            raise ValueError(
                "Invalid value for `behavior` ({0}), must be one of {1}"
                .format(behavior, allowed_values)
            )

        self._behavior = behavior

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
        if not isinstance(other, DiningOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
