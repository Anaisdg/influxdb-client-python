# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb2.domain.threshold_base import ThresholdBase


class RangeThreshold(ThresholdBase):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'min': 'float',
        'max': 'float',
        'within': 'bool',
        'level': 'CheckStatusLevel',
        'all_values': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'min': 'min',
        'max': 'max',
        'within': 'within',
        'level': 'level',
        'all_values': 'allValues'
    }

    def __init__(self, type=None, min=None, max=None, within=None, level=None, all_values=None):  # noqa: E501
        """RangeThreshold - a model defined in OpenAPI"""  # noqa: E501
        ThresholdBase.__init__(self, level=level, all_values=all_values)

        self._type = None
        self._min = None
        self._max = None
        self._within = None
        self.discriminator = None

        self.type = type
        self.min = min
        self.max = max
        self.within = within

    @property
    def type(self):
        """Gets the type of this RangeThreshold.  # noqa: E501


        :return: The type of this RangeThreshold.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RangeThreshold.


        :param type: The type of this RangeThreshold.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["range"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def min(self):
        """Gets the min of this RangeThreshold.  # noqa: E501


        :return: The min of this RangeThreshold.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this RangeThreshold.


        :param min: The min of this RangeThreshold.  # noqa: E501
        :type: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def max(self):
        """Gets the max of this RangeThreshold.  # noqa: E501


        :return: The max of this RangeThreshold.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this RangeThreshold.


        :param max: The max of this RangeThreshold.  # noqa: E501
        :type: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def within(self):
        """Gets the within of this RangeThreshold.  # noqa: E501


        :return: The within of this RangeThreshold.  # noqa: E501
        :rtype: bool
        """
        return self._within

    @within.setter
    def within(self, within):
        """Sets the within of this RangeThreshold.


        :param within: The within of this RangeThreshold.  # noqa: E501
        :type: bool
        """
        if within is None:
            raise ValueError("Invalid value for `within`, must not be `None`")  # noqa: E501

        self._within = within

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RangeThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
