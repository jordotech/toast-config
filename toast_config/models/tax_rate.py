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


class TaxRate(object):
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
        'name': 'str',
        'is_default': 'bool',
        'rate': 'float',
        'type': 'str',
        'rounding_type': 'str',
        'tax_table': 'list[TaxTableRow]'
    }

    attribute_map = {
        'guid': 'guid',
        'entity_type': 'entityType',
        'name': 'name',
        'is_default': 'isDefault',
        'rate': 'rate',
        'type': 'type',
        'rounding_type': 'roundingType',
        'tax_table': 'taxTable'
    }

    def __init__(self, guid=None, entity_type=None, name=None, is_default=None, rate=None, type=None, rounding_type=None, tax_table=None):
        """
        TaxRate - a model defined in Swagger
        """

        self._guid = None
        self._entity_type = None
        self._name = None
        self._is_default = None
        self._rate = None
        self._type = None
        self._rounding_type = None
        self._tax_table = None

        self.guid = guid
        self.entity_type = entity_type
        if name is not None:
          self.name = name
        if is_default is not None:
          self.is_default = is_default
        if rate is not None:
          self.rate = rate
        if type is not None:
          self.type = type
        if rounding_type is not None:
          self.rounding_type = rounding_type
        if tax_table is not None:
          self.tax_table = tax_table

    @property
    def guid(self):
        """
        Gets the guid of this TaxRate.
        The GUID maintained by the Toast POS.

        :return: The guid of this TaxRate.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this TaxRate.
        The GUID maintained by the Toast POS.

        :param guid: The guid of this TaxRate.
        :type: str
        """
        if guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")

        self._guid = guid

    @property
    def entity_type(self):
        """
        Gets the entity_type of this TaxRate.
        The type of object this is.

        :return: The entity_type of this TaxRate.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this TaxRate.
        The type of object this is.

        :param entity_type: The entity_type of this TaxRate.
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this TaxRate.
        The name of this tax rate.

        :return: The name of this TaxRate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaxRate.
        The name of this tax rate.

        :param name: The name of this TaxRate.
        :type: str
        """

        self._name = name

    @property
    def is_default(self):
        """
        Gets the is_default of this TaxRate.
        True if this tax rate is the default tax rate.

        :return: The is_default of this TaxRate.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this TaxRate.
        True if this tax rate is the default tax rate.

        :param is_default: The is_default of this TaxRate.
        :type: bool
        """

        self._is_default = is_default

    @property
    def rate(self):
        """
        Gets the rate of this TaxRate.
        The tax rate, which could be a fixed amount, a percentage, or null if the tax rate type is `NONE`.

        :return: The rate of this TaxRate.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this TaxRate.
        The tax rate, which could be a fixed amount, a percentage, or null if the tax rate type is `NONE`.

        :param rate: The rate of this TaxRate.
        :type: float
        """

        self._rate = rate

    @property
    def type(self):
        """
        Gets the type of this TaxRate.
        The type of the tax rate.

        :return: The type of this TaxRate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TaxRate.
        The type of the tax rate.

        :param type: The type of this TaxRate.
        :type: str
        """
        allowed_values = ["PERCENT", "FIXED", "TABLE", "NONE"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def rounding_type(self):
        """
        Gets the rounding_type of this TaxRate.
        The method used to round fractional currency amounts to non-fractional currency amounts. If a tax rate is not a `PERCENT` type, this value is null.

        :return: The rounding_type of this TaxRate.
        :rtype: str
        """
        return self._rounding_type

    @rounding_type.setter
    def rounding_type(self, rounding_type):
        """
        Sets the rounding_type of this TaxRate.
        The method used to round fractional currency amounts to non-fractional currency amounts. If a tax rate is not a `PERCENT` type, this value is null.

        :param rounding_type: The rounding_type of this TaxRate.
        :type: str
        """
        allowed_values = ["HALF_UP", "HALF_EVEN", "ALWAYS_UP", "ALWAYS_DOWN"]
        if rounding_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rounding_type` ({0}), must be one of {1}"
                .format(rounding_type, allowed_values)
            )

        self._rounding_type = rounding_type

    @property
    def tax_table(self):
        """
        Gets the tax_table of this TaxRate.
        An array of `TaxTableRow` objects that define a set of tax amounts that apply to specific sale amount ranges.

        :return: The tax_table of this TaxRate.
        :rtype: list[TaxTableRow]
        """
        return self._tax_table

    @tax_table.setter
    def tax_table(self, tax_table):
        """
        Sets the tax_table of this TaxRate.
        An array of `TaxTableRow` objects that define a set of tax amounts that apply to specific sale amount ranges.

        :param tax_table: The tax_table of this TaxRate.
        :type: list[TaxTableRow]
        """

        self._tax_table = tax_table

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
        if not isinstance(other, TaxRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
