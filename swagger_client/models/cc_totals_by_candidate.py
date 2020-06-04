# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CCTotalsByCandidate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'candidate_id': 'str',
        'cycle': 'int',
        'support_oppose_indicator': 'str',
        'total': 'float'
    }

    attribute_map = {
        'candidate_id': 'candidate_id',
        'cycle': 'cycle',
        'support_oppose_indicator': 'support_oppose_indicator',
        'total': 'total'
    }

    def __init__(self, candidate_id=None, cycle=None, support_oppose_indicator=None, total=None):  # noqa: E501
        """CCTotalsByCandidate - a model defined in Swagger"""  # noqa: E501

        self._candidate_id = None
        self._cycle = None
        self._support_oppose_indicator = None
        self._total = None
        self.discriminator = None

        if candidate_id is not None:
            self.candidate_id = candidate_id
        if cycle is not None:
            self.cycle = cycle
        if support_oppose_indicator is not None:
            self.support_oppose_indicator = support_oppose_indicator
        if total is not None:
            self.total = total

    @property
    def candidate_id(self):
        """Gets the candidate_id of this CCTotalsByCandidate.  # noqa: E501


        :return: The candidate_id of this CCTotalsByCandidate.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this CCTotalsByCandidate.


        :param candidate_id: The candidate_id of this CCTotalsByCandidate.  # noqa: E501
        :type: str
        """

        self._candidate_id = candidate_id

    @property
    def cycle(self):
        """Gets the cycle of this CCTotalsByCandidate.  # noqa: E501


        :return: The cycle of this CCTotalsByCandidate.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this CCTotalsByCandidate.


        :param cycle: The cycle of this CCTotalsByCandidate.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def support_oppose_indicator(self):
        """Gets the support_oppose_indicator of this CCTotalsByCandidate.  # noqa: E501


        :return: The support_oppose_indicator of this CCTotalsByCandidate.  # noqa: E501
        :rtype: str
        """
        return self._support_oppose_indicator

    @support_oppose_indicator.setter
    def support_oppose_indicator(self, support_oppose_indicator):
        """Sets the support_oppose_indicator of this CCTotalsByCandidate.


        :param support_oppose_indicator: The support_oppose_indicator of this CCTotalsByCandidate.  # noqa: E501
        :type: str
        """

        self._support_oppose_indicator = support_oppose_indicator

    @property
    def total(self):
        """Gets the total of this CCTotalsByCandidate.  # noqa: E501


        :return: The total of this CCTotalsByCandidate.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CCTotalsByCandidate.


        :param total: The total of this CCTotalsByCandidate.  # noqa: E501
        :type: float
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CCTotalsByCandidate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CCTotalsByCandidate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
