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


class InlineResponseDefault1AdvisoryOpinions(object):
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
        'ao_citations': 'list[InlineResponseDefault1AoCitations]',
        'aos_cited_by': 'list[InlineResponseDefault1AoCitations]',
        'commenter_names': 'list[str]',
        'document_highlights': 'object',
        'documents': 'list[InlineResponseDefault1Documents1]',
        'entities': 'list[InlineResponseDefault1Entities]',
        'highlights': 'list[str]',
        'is_pending': 'bool',
        'issue_date': 'date',
        'name': 'str',
        'no': 'str',
        'regulatory_citations': 'list[InlineResponseDefault1RegulatoryCitations]',
        'representative_names': 'list[str]',
        'request_date': 'date',
        'requestor_names': 'list[str]',
        'requestor_types': 'list[str]',
        'status': 'str',
        'statutory_citations': 'list[InlineResponseDefault1StatutoryCitations]',
        'summary': 'str'
    }

    attribute_map = {
        'ao_citations': 'ao_citations',
        'aos_cited_by': 'aos_cited_by',
        'commenter_names': 'commenter_names',
        'document_highlights': 'document_highlights',
        'documents': 'documents',
        'entities': 'entities',
        'highlights': 'highlights',
        'is_pending': 'is_pending',
        'issue_date': 'issue_date',
        'name': 'name',
        'no': 'no',
        'regulatory_citations': 'regulatory_citations',
        'representative_names': 'representative_names',
        'request_date': 'request_date',
        'requestor_names': 'requestor_names',
        'requestor_types': 'requestor_types',
        'status': 'status',
        'statutory_citations': 'statutory_citations',
        'summary': 'summary'
    }

    def __init__(self, ao_citations=None, aos_cited_by=None, commenter_names=None, document_highlights=None, documents=None, entities=None, highlights=None, is_pending=None, issue_date=None, name=None, no=None, regulatory_citations=None, representative_names=None, request_date=None, requestor_names=None, requestor_types=None, status=None, statutory_citations=None, summary=None):  # noqa: E501
        """InlineResponseDefault1AdvisoryOpinions - a model defined in Swagger"""  # noqa: E501

        self._ao_citations = None
        self._aos_cited_by = None
        self._commenter_names = None
        self._document_highlights = None
        self._documents = None
        self._entities = None
        self._highlights = None
        self._is_pending = None
        self._issue_date = None
        self._name = None
        self._no = None
        self._regulatory_citations = None
        self._representative_names = None
        self._request_date = None
        self._requestor_names = None
        self._requestor_types = None
        self._status = None
        self._statutory_citations = None
        self._summary = None
        self.discriminator = None

        if ao_citations is not None:
            self.ao_citations = ao_citations
        if aos_cited_by is not None:
            self.aos_cited_by = aos_cited_by
        if commenter_names is not None:
            self.commenter_names = commenter_names
        if document_highlights is not None:
            self.document_highlights = document_highlights
        if documents is not None:
            self.documents = documents
        if entities is not None:
            self.entities = entities
        if highlights is not None:
            self.highlights = highlights
        if is_pending is not None:
            self.is_pending = is_pending
        if issue_date is not None:
            self.issue_date = issue_date
        if name is not None:
            self.name = name
        if no is not None:
            self.no = no
        if regulatory_citations is not None:
            self.regulatory_citations = regulatory_citations
        if representative_names is not None:
            self.representative_names = representative_names
        if request_date is not None:
            self.request_date = request_date
        if requestor_names is not None:
            self.requestor_names = requestor_names
        if requestor_types is not None:
            self.requestor_types = requestor_types
        if status is not None:
            self.status = status
        if statutory_citations is not None:
            self.statutory_citations = statutory_citations
        if summary is not None:
            self.summary = summary

    @property
    def ao_citations(self):
        """Gets the ao_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The ao_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[InlineResponseDefault1AoCitations]
        """
        return self._ao_citations

    @ao_citations.setter
    def ao_citations(self, ao_citations):
        """Sets the ao_citations of this InlineResponseDefault1AdvisoryOpinions.


        :param ao_citations: The ao_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[InlineResponseDefault1AoCitations]
        """

        self._ao_citations = ao_citations

    @property
    def aos_cited_by(self):
        """Gets the aos_cited_by of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The aos_cited_by of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[InlineResponseDefault1AoCitations]
        """
        return self._aos_cited_by

    @aos_cited_by.setter
    def aos_cited_by(self, aos_cited_by):
        """Sets the aos_cited_by of this InlineResponseDefault1AdvisoryOpinions.


        :param aos_cited_by: The aos_cited_by of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[InlineResponseDefault1AoCitations]
        """

        self._aos_cited_by = aos_cited_by

    @property
    def commenter_names(self):
        """Gets the commenter_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The commenter_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[str]
        """
        return self._commenter_names

    @commenter_names.setter
    def commenter_names(self, commenter_names):
        """Sets the commenter_names of this InlineResponseDefault1AdvisoryOpinions.


        :param commenter_names: The commenter_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[str]
        """

        self._commenter_names = commenter_names

    @property
    def document_highlights(self):
        """Gets the document_highlights of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The document_highlights of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: object
        """
        return self._document_highlights

    @document_highlights.setter
    def document_highlights(self, document_highlights):
        """Sets the document_highlights of this InlineResponseDefault1AdvisoryOpinions.


        :param document_highlights: The document_highlights of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: object
        """

        self._document_highlights = document_highlights

    @property
    def documents(self):
        """Gets the documents of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The documents of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[InlineResponseDefault1Documents1]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this InlineResponseDefault1AdvisoryOpinions.


        :param documents: The documents of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[InlineResponseDefault1Documents1]
        """

        self._documents = documents

    @property
    def entities(self):
        """Gets the entities of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The entities of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[InlineResponseDefault1Entities]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this InlineResponseDefault1AdvisoryOpinions.


        :param entities: The entities of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[InlineResponseDefault1Entities]
        """

        self._entities = entities

    @property
    def highlights(self):
        """Gets the highlights of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The highlights of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[str]
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this InlineResponseDefault1AdvisoryOpinions.


        :param highlights: The highlights of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[str]
        """

        self._highlights = highlights

    @property
    def is_pending(self):
        """Gets the is_pending of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The is_pending of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: bool
        """
        return self._is_pending

    @is_pending.setter
    def is_pending(self, is_pending):
        """Sets the is_pending of this InlineResponseDefault1AdvisoryOpinions.


        :param is_pending: The is_pending of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: bool
        """

        self._is_pending = is_pending

    @property
    def issue_date(self):
        """Gets the issue_date of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The issue_date of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: date
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this InlineResponseDefault1AdvisoryOpinions.


        :param issue_date: The issue_date of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: date
        """

        self._issue_date = issue_date

    @property
    def name(self):
        """Gets the name of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The name of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponseDefault1AdvisoryOpinions.


        :param name: The name of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def no(self):
        """Gets the no of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The no of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: str
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this InlineResponseDefault1AdvisoryOpinions.


        :param no: The no of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: str
        """

        self._no = no

    @property
    def regulatory_citations(self):
        """Gets the regulatory_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The regulatory_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[InlineResponseDefault1RegulatoryCitations]
        """
        return self._regulatory_citations

    @regulatory_citations.setter
    def regulatory_citations(self, regulatory_citations):
        """Sets the regulatory_citations of this InlineResponseDefault1AdvisoryOpinions.


        :param regulatory_citations: The regulatory_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[InlineResponseDefault1RegulatoryCitations]
        """

        self._regulatory_citations = regulatory_citations

    @property
    def representative_names(self):
        """Gets the representative_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The representative_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[str]
        """
        return self._representative_names

    @representative_names.setter
    def representative_names(self, representative_names):
        """Sets the representative_names of this InlineResponseDefault1AdvisoryOpinions.


        :param representative_names: The representative_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[str]
        """

        self._representative_names = representative_names

    @property
    def request_date(self):
        """Gets the request_date of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The request_date of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: date
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this InlineResponseDefault1AdvisoryOpinions.


        :param request_date: The request_date of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: date
        """

        self._request_date = request_date

    @property
    def requestor_names(self):
        """Gets the requestor_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The requestor_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[str]
        """
        return self._requestor_names

    @requestor_names.setter
    def requestor_names(self, requestor_names):
        """Sets the requestor_names of this InlineResponseDefault1AdvisoryOpinions.


        :param requestor_names: The requestor_names of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[str]
        """

        self._requestor_names = requestor_names

    @property
    def requestor_types(self):
        """Gets the requestor_types of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The requestor_types of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[str]
        """
        return self._requestor_types

    @requestor_types.setter
    def requestor_types(self, requestor_types):
        """Sets the requestor_types of this InlineResponseDefault1AdvisoryOpinions.


        :param requestor_types: The requestor_types of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[str]
        """

        self._requestor_types = requestor_types

    @property
    def status(self):
        """Gets the status of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The status of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponseDefault1AdvisoryOpinions.


        :param status: The status of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def statutory_citations(self):
        """Gets the statutory_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The statutory_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: list[InlineResponseDefault1StatutoryCitations]
        """
        return self._statutory_citations

    @statutory_citations.setter
    def statutory_citations(self, statutory_citations):
        """Sets the statutory_citations of this InlineResponseDefault1AdvisoryOpinions.


        :param statutory_citations: The statutory_citations of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: list[InlineResponseDefault1StatutoryCitations]
        """

        self._statutory_citations = statutory_citations

    @property
    def summary(self):
        """Gets the summary of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501


        :return: The summary of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this InlineResponseDefault1AdvisoryOpinions.


        :param summary: The summary of this InlineResponseDefault1AdvisoryOpinions.  # noqa: E501
        :type: str
        """

        self._summary = summary

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
        if issubclass(InlineResponseDefault1AdvisoryOpinions, dict):
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
        if not isinstance(other, InlineResponseDefault1AdvisoryOpinions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
