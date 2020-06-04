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


class InlineResponseDefault1Murs(object):
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
        'close_date': 'date',
        'commission_votes': 'list[InlineResponseDefault1CommissionVotes]',
        'dispositions': 'list[InlineResponseDefault1Dispositions]',
        'doc_id': 'str',
        'document_highlights': 'object',
        'documents': 'list[InlineResponseDefault1Documents]',
        'election_cycles': 'int',
        'highlights': 'list[str]',
        'mur_type': 'str',
        'name': 'str',
        'no': 'str',
        'open_date': 'date',
        'participants': 'list[InlineResponseDefault1Participants]',
        'respondents': 'list[str]',
        'subjects': 'list[str]',
        'url': 'str'
    }

    attribute_map = {
        'close_date': 'close_date',
        'commission_votes': 'commission_votes',
        'dispositions': 'dispositions',
        'doc_id': 'doc_id',
        'document_highlights': 'document_highlights',
        'documents': 'documents',
        'election_cycles': 'election_cycles',
        'highlights': 'highlights',
        'mur_type': 'mur_type',
        'name': 'name',
        'no': 'no',
        'open_date': 'open_date',
        'participants': 'participants',
        'respondents': 'respondents',
        'subjects': 'subjects',
        'url': 'url'
    }

    def __init__(self, close_date=None, commission_votes=None, dispositions=None, doc_id=None, document_highlights=None, documents=None, election_cycles=None, highlights=None, mur_type=None, name=None, no=None, open_date=None, participants=None, respondents=None, subjects=None, url=None):  # noqa: E501
        """InlineResponseDefault1Murs - a model defined in Swagger"""  # noqa: E501

        self._close_date = None
        self._commission_votes = None
        self._dispositions = None
        self._doc_id = None
        self._document_highlights = None
        self._documents = None
        self._election_cycles = None
        self._highlights = None
        self._mur_type = None
        self._name = None
        self._no = None
        self._open_date = None
        self._participants = None
        self._respondents = None
        self._subjects = None
        self._url = None
        self.discriminator = None

        if close_date is not None:
            self.close_date = close_date
        if commission_votes is not None:
            self.commission_votes = commission_votes
        if dispositions is not None:
            self.dispositions = dispositions
        if doc_id is not None:
            self.doc_id = doc_id
        if document_highlights is not None:
            self.document_highlights = document_highlights
        if documents is not None:
            self.documents = documents
        if election_cycles is not None:
            self.election_cycles = election_cycles
        if highlights is not None:
            self.highlights = highlights
        if mur_type is not None:
            self.mur_type = mur_type
        if name is not None:
            self.name = name
        if no is not None:
            self.no = no
        if open_date is not None:
            self.open_date = open_date
        if participants is not None:
            self.participants = participants
        if respondents is not None:
            self.respondents = respondents
        if subjects is not None:
            self.subjects = subjects
        if url is not None:
            self.url = url

    @property
    def close_date(self):
        """Gets the close_date of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The close_date of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: date
        """
        return self._close_date

    @close_date.setter
    def close_date(self, close_date):
        """Sets the close_date of this InlineResponseDefault1Murs.


        :param close_date: The close_date of this InlineResponseDefault1Murs.  # noqa: E501
        :type: date
        """

        self._close_date = close_date

    @property
    def commission_votes(self):
        """Gets the commission_votes of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The commission_votes of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: list[InlineResponseDefault1CommissionVotes]
        """
        return self._commission_votes

    @commission_votes.setter
    def commission_votes(self, commission_votes):
        """Sets the commission_votes of this InlineResponseDefault1Murs.


        :param commission_votes: The commission_votes of this InlineResponseDefault1Murs.  # noqa: E501
        :type: list[InlineResponseDefault1CommissionVotes]
        """

        self._commission_votes = commission_votes

    @property
    def dispositions(self):
        """Gets the dispositions of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The dispositions of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: list[InlineResponseDefault1Dispositions]
        """
        return self._dispositions

    @dispositions.setter
    def dispositions(self, dispositions):
        """Sets the dispositions of this InlineResponseDefault1Murs.


        :param dispositions: The dispositions of this InlineResponseDefault1Murs.  # noqa: E501
        :type: list[InlineResponseDefault1Dispositions]
        """

        self._dispositions = dispositions

    @property
    def doc_id(self):
        """Gets the doc_id of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The doc_id of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this InlineResponseDefault1Murs.


        :param doc_id: The doc_id of this InlineResponseDefault1Murs.  # noqa: E501
        :type: str
        """

        self._doc_id = doc_id

    @property
    def document_highlights(self):
        """Gets the document_highlights of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The document_highlights of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: object
        """
        return self._document_highlights

    @document_highlights.setter
    def document_highlights(self, document_highlights):
        """Sets the document_highlights of this InlineResponseDefault1Murs.


        :param document_highlights: The document_highlights of this InlineResponseDefault1Murs.  # noqa: E501
        :type: object
        """

        self._document_highlights = document_highlights

    @property
    def documents(self):
        """Gets the documents of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The documents of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: list[InlineResponseDefault1Documents]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this InlineResponseDefault1Murs.


        :param documents: The documents of this InlineResponseDefault1Murs.  # noqa: E501
        :type: list[InlineResponseDefault1Documents]
        """

        self._documents = documents

    @property
    def election_cycles(self):
        """Gets the election_cycles of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The election_cycles of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: int
        """
        return self._election_cycles

    @election_cycles.setter
    def election_cycles(self, election_cycles):
        """Sets the election_cycles of this InlineResponseDefault1Murs.


        :param election_cycles: The election_cycles of this InlineResponseDefault1Murs.  # noqa: E501
        :type: int
        """

        self._election_cycles = election_cycles

    @property
    def highlights(self):
        """Gets the highlights of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The highlights of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: list[str]
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this InlineResponseDefault1Murs.


        :param highlights: The highlights of this InlineResponseDefault1Murs.  # noqa: E501
        :type: list[str]
        """

        self._highlights = highlights

    @property
    def mur_type(self):
        """Gets the mur_type of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The mur_type of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: str
        """
        return self._mur_type

    @mur_type.setter
    def mur_type(self, mur_type):
        """Sets the mur_type of this InlineResponseDefault1Murs.


        :param mur_type: The mur_type of this InlineResponseDefault1Murs.  # noqa: E501
        :type: str
        """
        allowed_values = ["current", "archived"]  # noqa: E501
        if mur_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mur_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mur_type, allowed_values)
            )

        self._mur_type = mur_type

    @property
    def name(self):
        """Gets the name of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The name of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponseDefault1Murs.


        :param name: The name of this InlineResponseDefault1Murs.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def no(self):
        """Gets the no of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The no of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: str
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this InlineResponseDefault1Murs.


        :param no: The no of this InlineResponseDefault1Murs.  # noqa: E501
        :type: str
        """

        self._no = no

    @property
    def open_date(self):
        """Gets the open_date of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The open_date of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: date
        """
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        """Sets the open_date of this InlineResponseDefault1Murs.


        :param open_date: The open_date of this InlineResponseDefault1Murs.  # noqa: E501
        :type: date
        """

        self._open_date = open_date

    @property
    def participants(self):
        """Gets the participants of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The participants of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: list[InlineResponseDefault1Participants]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this InlineResponseDefault1Murs.


        :param participants: The participants of this InlineResponseDefault1Murs.  # noqa: E501
        :type: list[InlineResponseDefault1Participants]
        """

        self._participants = participants

    @property
    def respondents(self):
        """Gets the respondents of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The respondents of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: list[str]
        """
        return self._respondents

    @respondents.setter
    def respondents(self, respondents):
        """Sets the respondents of this InlineResponseDefault1Murs.


        :param respondents: The respondents of this InlineResponseDefault1Murs.  # noqa: E501
        :type: list[str]
        """

        self._respondents = respondents

    @property
    def subjects(self):
        """Gets the subjects of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The subjects of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: list[str]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """Sets the subjects of this InlineResponseDefault1Murs.


        :param subjects: The subjects of this InlineResponseDefault1Murs.  # noqa: E501
        :type: list[str]
        """

        self._subjects = subjects

    @property
    def url(self):
        """Gets the url of this InlineResponseDefault1Murs.  # noqa: E501


        :return: The url of this InlineResponseDefault1Murs.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponseDefault1Murs.


        :param url: The url of this InlineResponseDefault1Murs.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(InlineResponseDefault1Murs, dict):
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
        if not isinstance(other, InlineResponseDefault1Murs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other