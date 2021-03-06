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
from influxdb_client.domain.check_base import CheckBase


class ThresholdCheck(CheckBase):
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
        'thresholds': 'list[Threshold]',
        'id': 'str',
        'name': 'str',
        'org_id': 'str',
        'owner_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'query': 'DashboardQuery',
        'status': 'TaskStatusType',
        'every': 'str',
        'offset': 'str',
        'tags': 'list[CheckBaseTags]',
        'description': 'str',
        'status_message_template': 'str',
        'labels': 'list[Label]',
        'links': 'CheckBaseLinks'
    }

    attribute_map = {
        'type': 'type',
        'thresholds': 'thresholds',
        'id': 'id',
        'name': 'name',
        'org_id': 'orgID',
        'owner_id': 'ownerID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'query': 'query',
        'status': 'status',
        'every': 'every',
        'offset': 'offset',
        'tags': 'tags',
        'description': 'description',
        'status_message_template': 'statusMessageTemplate',
        'labels': 'labels',
        'links': 'links'
    }

    def __init__(self, type=None, thresholds=None, id=None, name=None, org_id=None, owner_id=None, created_at=None, updated_at=None, query=None, status=None, every=None, offset=None, tags=None, description=None, status_message_template=None, labels=None, links=None):  # noqa: E501
        """ThresholdCheck - a model defined in OpenAPI"""  # noqa: E501
        CheckBase.__init__(self, id=id, name=name, org_id=org_id, owner_id=owner_id, created_at=created_at, updated_at=updated_at, query=query, status=status, every=every, offset=offset, tags=tags, description=description, status_message_template=status_message_template, labels=labels, links=links)

        self._type = None
        self._thresholds = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if thresholds is not None:
            self.thresholds = thresholds

    @property
    def type(self):
        """Gets the type of this ThresholdCheck.  # noqa: E501


        :return: The type of this ThresholdCheck.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThresholdCheck.


        :param type: The type of this ThresholdCheck.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def thresholds(self):
        """Gets the thresholds of this ThresholdCheck.  # noqa: E501


        :return: The thresholds of this ThresholdCheck.  # noqa: E501
        :rtype: list[Threshold]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this ThresholdCheck.


        :param thresholds: The thresholds of this ThresholdCheck.  # noqa: E501
        :type: list[Threshold]
        """

        self._thresholds = thresholds

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
        if not isinstance(other, ThresholdCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
