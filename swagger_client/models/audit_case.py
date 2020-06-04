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


class AuditCase(object):
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
        'audit_case_id': 'str',
        'audit_id': 'int',
        'candidate_id': 'str',
        'candidate_name': 'str',
        'committee_description': 'str',
        'committee_designation': 'str',
        'committee_id': 'str',
        'committee_name': 'str',
        'committee_type': 'str',
        'cycle': 'int',
        'far_release_date': 'date',
        'link_to_report': 'str',
        'primary_category_list': 'list[AuditCaseCategoryRelation]'
    }

    attribute_map = {
        'audit_case_id': 'audit_case_id',
        'audit_id': 'audit_id',
        'candidate_id': 'candidate_id',
        'candidate_name': 'candidate_name',
        'committee_description': 'committee_description',
        'committee_designation': 'committee_designation',
        'committee_id': 'committee_id',
        'committee_name': 'committee_name',
        'committee_type': 'committee_type',
        'cycle': 'cycle',
        'far_release_date': 'far_release_date',
        'link_to_report': 'link_to_report',
        'primary_category_list': 'primary_category_list'
    }

    def __init__(self, audit_case_id=None, audit_id=None, candidate_id=None, candidate_name=None, committee_description=None, committee_designation=None, committee_id=None, committee_name=None, committee_type=None, cycle=None, far_release_date=None, link_to_report=None, primary_category_list=None):  # noqa: E501
        """AuditCase - a model defined in Swagger"""  # noqa: E501

        self._audit_case_id = None
        self._audit_id = None
        self._candidate_id = None
        self._candidate_name = None
        self._committee_description = None
        self._committee_designation = None
        self._committee_id = None
        self._committee_name = None
        self._committee_type = None
        self._cycle = None
        self._far_release_date = None
        self._link_to_report = None
        self._primary_category_list = None
        self.discriminator = None

        if audit_case_id is not None:
            self.audit_case_id = audit_case_id
        if audit_id is not None:
            self.audit_id = audit_id
        if candidate_id is not None:
            self.candidate_id = candidate_id
        if candidate_name is not None:
            self.candidate_name = candidate_name
        if committee_description is not None:
            self.committee_description = committee_description
        if committee_designation is not None:
            self.committee_designation = committee_designation
        if committee_id is not None:
            self.committee_id = committee_id
        if committee_name is not None:
            self.committee_name = committee_name
        if committee_type is not None:
            self.committee_type = committee_type
        if cycle is not None:
            self.cycle = cycle
        if far_release_date is not None:
            self.far_release_date = far_release_date
        if link_to_report is not None:
            self.link_to_report = link_to_report
        if primary_category_list is not None:
            self.primary_category_list = primary_category_list

    @property
    def audit_case_id(self):
        """Gets the audit_case_id of this AuditCase.  # noqa: E501


        :return: The audit_case_id of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._audit_case_id

    @audit_case_id.setter
    def audit_case_id(self, audit_case_id):
        """Sets the audit_case_id of this AuditCase.


        :param audit_case_id: The audit_case_id of this AuditCase.  # noqa: E501
        :type: str
        """

        self._audit_case_id = audit_case_id

    @property
    def audit_id(self):
        """Gets the audit_id of this AuditCase.  # noqa: E501


        :return: The audit_id of this AuditCase.  # noqa: E501
        :rtype: int
        """
        return self._audit_id

    @audit_id.setter
    def audit_id(self, audit_id):
        """Sets the audit_id of this AuditCase.


        :param audit_id: The audit_id of this AuditCase.  # noqa: E501
        :type: int
        """

        self._audit_id = audit_id

    @property
    def candidate_id(self):
        """Gets the candidate_id of this AuditCase.  # noqa: E501


        :return: The candidate_id of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this AuditCase.


        :param candidate_id: The candidate_id of this AuditCase.  # noqa: E501
        :type: str
        """

        self._candidate_id = candidate_id

    @property
    def candidate_name(self):
        """Gets the candidate_name of this AuditCase.  # noqa: E501


        :return: The candidate_name of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, candidate_name):
        """Sets the candidate_name of this AuditCase.


        :param candidate_name: The candidate_name of this AuditCase.  # noqa: E501
        :type: str
        """

        self._candidate_name = candidate_name

    @property
    def committee_description(self):
        """Gets the committee_description of this AuditCase.  # noqa: E501


        :return: The committee_description of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._committee_description

    @committee_description.setter
    def committee_description(self, committee_description):
        """Sets the committee_description of this AuditCase.


        :param committee_description: The committee_description of this AuditCase.  # noqa: E501
        :type: str
        """

        self._committee_description = committee_description

    @property
    def committee_designation(self):
        """Gets the committee_designation of this AuditCase.  # noqa: E501


        :return: The committee_designation of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._committee_designation

    @committee_designation.setter
    def committee_designation(self, committee_designation):
        """Sets the committee_designation of this AuditCase.


        :param committee_designation: The committee_designation of this AuditCase.  # noqa: E501
        :type: str
        """

        self._committee_designation = committee_designation

    @property
    def committee_id(self):
        """Gets the committee_id of this AuditCase.  # noqa: E501


        :return: The committee_id of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this AuditCase.


        :param committee_id: The committee_id of this AuditCase.  # noqa: E501
        :type: str
        """

        self._committee_id = committee_id

    @property
    def committee_name(self):
        """Gets the committee_name of this AuditCase.  # noqa: E501


        :return: The committee_name of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._committee_name

    @committee_name.setter
    def committee_name(self, committee_name):
        """Sets the committee_name of this AuditCase.


        :param committee_name: The committee_name of this AuditCase.  # noqa: E501
        :type: str
        """

        self._committee_name = committee_name

    @property
    def committee_type(self):
        """Gets the committee_type of this AuditCase.  # noqa: E501


        :return: The committee_type of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._committee_type

    @committee_type.setter
    def committee_type(self, committee_type):
        """Sets the committee_type of this AuditCase.


        :param committee_type: The committee_type of this AuditCase.  # noqa: E501
        :type: str
        """

        self._committee_type = committee_type

    @property
    def cycle(self):
        """Gets the cycle of this AuditCase.  # noqa: E501


        :return: The cycle of this AuditCase.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this AuditCase.


        :param cycle: The cycle of this AuditCase.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def far_release_date(self):
        """Gets the far_release_date of this AuditCase.  # noqa: E501


        :return: The far_release_date of this AuditCase.  # noqa: E501
        :rtype: date
        """
        return self._far_release_date

    @far_release_date.setter
    def far_release_date(self, far_release_date):
        """Sets the far_release_date of this AuditCase.


        :param far_release_date: The far_release_date of this AuditCase.  # noqa: E501
        :type: date
        """

        self._far_release_date = far_release_date

    @property
    def link_to_report(self):
        """Gets the link_to_report of this AuditCase.  # noqa: E501

         URL for retrieving the PDF document   # noqa: E501

        :return: The link_to_report of this AuditCase.  # noqa: E501
        :rtype: str
        """
        return self._link_to_report

    @link_to_report.setter
    def link_to_report(self, link_to_report):
        """Sets the link_to_report of this AuditCase.

         URL for retrieving the PDF document   # noqa: E501

        :param link_to_report: The link_to_report of this AuditCase.  # noqa: E501
        :type: str
        """

        self._link_to_report = link_to_report

    @property
    def primary_category_list(self):
        """Gets the primary_category_list of this AuditCase.  # noqa: E501


        :return: The primary_category_list of this AuditCase.  # noqa: E501
        :rtype: list[AuditCaseCategoryRelation]
        """
        return self._primary_category_list

    @primary_category_list.setter
    def primary_category_list(self, primary_category_list):
        """Sets the primary_category_list of this AuditCase.


        :param primary_category_list: The primary_category_list of this AuditCase.  # noqa: E501
        :type: list[AuditCaseCategoryRelation]
        """

        self._primary_category_list = primary_category_list

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
        if issubclass(AuditCase, dict):
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
        if not isinstance(other, AuditCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
