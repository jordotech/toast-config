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


class Table(object):
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
        'service_area': 'ToastReference'
    }

    attribute_map = {
        'guid': 'guid',
        'entity_type': 'entityType',
        'name': 'name',
        'service_area': 'serviceArea'
    }

    def __init__(self, guid=None, entity_type=None, name=None, service_area=None):
        """
        Table - a model defined in Swagger
        """

        self._guid = None
        self._entity_type = None
        self._name = None
        self._service_area = None

        self.guid = guid
        self.entity_type = entity_type
        if name is not None:
          self.name = name
        if service_area is not None:
          self.service_area = service_area

    @property
    def guid(self):
        """
        Gets the guid of this Table.
        The GUID maintained by the Toast POS.

        :return: The guid of this Table.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this Table.
        The GUID maintained by the Toast POS.

        :param guid: The guid of this Table.
        :type: str
        """
        if guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")

        self._guid = guid

    @property
    def entity_type(self):
        """
        Gets the entity_type of this Table.
        The type of object this is.

        :return: The entity_type of this Table.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this Table.
        The type of object this is.

        :param entity_type: The entity_type of this Table.
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this Table.
        The human-readable name of this table as it appears in the POS.

        :return: The name of this Table.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Table.
        The human-readable name of this table as it appears in the POS.

        :param name: The name of this Table.
        :type: str
        """

        self._name = name

    @property
    def service_area(self):
        """
        Gets the service_area of this Table.
        The service area the table belongs to.

        :return: The service_area of this Table.
        :rtype: ToastReference
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """
        Sets the service_area of this Table.
        The service area the table belongs to.

        :param service_area: The service_area of this Table.
        :type: ToastReference
        """

        self._service_area = service_area

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
        if not isinstance(other, Table):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
