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


class CandidateTotal(object):
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
        'candidate_inactive': 'bool',
        'cash_on_hand_end_period': 'float',
        'coverage_end_date': 'date',
        'coverage_start_date': 'date',
        'cycle': 'int',
        'debts_owed_by_committee': 'float',
        'disbursements': 'float',
        'election_year': 'int',
        'federal_funds_flag': 'bool',
        'has_raised_funds': 'bool',
        'is_election': 'bool',
        'office': 'str',
        'party': 'str',
        'receipts': 'float'
    }

    attribute_map = {
        'candidate_id': 'candidate_id',
        'candidate_inactive': 'candidate_inactive',
        'cash_on_hand_end_period': 'cash_on_hand_end_period',
        'coverage_end_date': 'coverage_end_date',
        'coverage_start_date': 'coverage_start_date',
        'cycle': 'cycle',
        'debts_owed_by_committee': 'debts_owed_by_committee',
        'disbursements': 'disbursements',
        'election_year': 'election_year',
        'federal_funds_flag': 'federal_funds_flag',
        'has_raised_funds': 'has_raised_funds',
        'is_election': 'is_election',
        'office': 'office',
        'party': 'party',
        'receipts': 'receipts'
    }

    def __init__(self, candidate_id=None, candidate_inactive=None, cash_on_hand_end_period=None, coverage_end_date=None, coverage_start_date=None, cycle=None, debts_owed_by_committee=None, disbursements=None, election_year=None, federal_funds_flag=None, has_raised_funds=None, is_election=None, office=None, party=None, receipts=None):  # noqa: E501
        """CandidateTotal - a model defined in Swagger"""  # noqa: E501

        self._candidate_id = None
        self._candidate_inactive = None
        self._cash_on_hand_end_period = None
        self._coverage_end_date = None
        self._coverage_start_date = None
        self._cycle = None
        self._debts_owed_by_committee = None
        self._disbursements = None
        self._election_year = None
        self._federal_funds_flag = None
        self._has_raised_funds = None
        self._is_election = None
        self._office = None
        self._party = None
        self._receipts = None
        self.discriminator = None

        self.candidate_id = candidate_id
        if candidate_inactive is not None:
            self.candidate_inactive = candidate_inactive
        if cash_on_hand_end_period is not None:
            self.cash_on_hand_end_period = cash_on_hand_end_period
        if coverage_end_date is not None:
            self.coverage_end_date = coverage_end_date
        if coverage_start_date is not None:
            self.coverage_start_date = coverage_start_date
        self.cycle = cycle
        if debts_owed_by_committee is not None:
            self.debts_owed_by_committee = debts_owed_by_committee
        if disbursements is not None:
            self.disbursements = disbursements
        if election_year is not None:
            self.election_year = election_year
        if federal_funds_flag is not None:
            self.federal_funds_flag = federal_funds_flag
        if has_raised_funds is not None:
            self.has_raised_funds = has_raised_funds
        self.is_election = is_election
        if office is not None:
            self.office = office
        if party is not None:
            self.party = party
        if receipts is not None:
            self.receipts = receipts

    @property
    def candidate_id(self):
        """Gets the candidate_id of this CandidateTotal.  # noqa: E501


        :return: The candidate_id of this CandidateTotal.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this CandidateTotal.


        :param candidate_id: The candidate_id of this CandidateTotal.  # noqa: E501
        :type: str
        """
        if candidate_id is None:
            raise ValueError("Invalid value for `candidate_id`, must not be `None`")  # noqa: E501

        self._candidate_id = candidate_id

    @property
    def candidate_inactive(self):
        """Gets the candidate_inactive of this CandidateTotal.  # noqa: E501

         True indicates that a candidate is inactive.   # noqa: E501

        :return: The candidate_inactive of this CandidateTotal.  # noqa: E501
        :rtype: bool
        """
        return self._candidate_inactive

    @candidate_inactive.setter
    def candidate_inactive(self, candidate_inactive):
        """Sets the candidate_inactive of this CandidateTotal.

         True indicates that a candidate is inactive.   # noqa: E501

        :param candidate_inactive: The candidate_inactive of this CandidateTotal.  # noqa: E501
        :type: bool
        """

        self._candidate_inactive = candidate_inactive

    @property
    def cash_on_hand_end_period(self):
        """Gets the cash_on_hand_end_period of this CandidateTotal.  # noqa: E501


        :return: The cash_on_hand_end_period of this CandidateTotal.  # noqa: E501
        :rtype: float
        """
        return self._cash_on_hand_end_period

    @cash_on_hand_end_period.setter
    def cash_on_hand_end_period(self, cash_on_hand_end_period):
        """Sets the cash_on_hand_end_period of this CandidateTotal.


        :param cash_on_hand_end_period: The cash_on_hand_end_period of this CandidateTotal.  # noqa: E501
        :type: float
        """

        self._cash_on_hand_end_period = cash_on_hand_end_period

    @property
    def coverage_end_date(self):
        """Gets the coverage_end_date of this CandidateTotal.  # noqa: E501

        Ending date of the reporting period  # noqa: E501

        :return: The coverage_end_date of this CandidateTotal.  # noqa: E501
        :rtype: date
        """
        return self._coverage_end_date

    @coverage_end_date.setter
    def coverage_end_date(self, coverage_end_date):
        """Sets the coverage_end_date of this CandidateTotal.

        Ending date of the reporting period  # noqa: E501

        :param coverage_end_date: The coverage_end_date of this CandidateTotal.  # noqa: E501
        :type: date
        """

        self._coverage_end_date = coverage_end_date

    @property
    def coverage_start_date(self):
        """Gets the coverage_start_date of this CandidateTotal.  # noqa: E501

        Beginning date of the reporting period  # noqa: E501

        :return: The coverage_start_date of this CandidateTotal.  # noqa: E501
        :rtype: date
        """
        return self._coverage_start_date

    @coverage_start_date.setter
    def coverage_start_date(self, coverage_start_date):
        """Sets the coverage_start_date of this CandidateTotal.

        Beginning date of the reporting period  # noqa: E501

        :param coverage_start_date: The coverage_start_date of this CandidateTotal.  # noqa: E501
        :type: date
        """

        self._coverage_start_date = coverage_start_date

    @property
    def cycle(self):
        """Gets the cycle of this CandidateTotal.  # noqa: E501


        :return: The cycle of this CandidateTotal.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this CandidateTotal.


        :param cycle: The cycle of this CandidateTotal.  # noqa: E501
        :type: int
        """
        if cycle is None:
            raise ValueError("Invalid value for `cycle`, must not be `None`")  # noqa: E501

        self._cycle = cycle

    @property
    def debts_owed_by_committee(self):
        """Gets the debts_owed_by_committee of this CandidateTotal.  # noqa: E501


        :return: The debts_owed_by_committee of this CandidateTotal.  # noqa: E501
        :rtype: float
        """
        return self._debts_owed_by_committee

    @debts_owed_by_committee.setter
    def debts_owed_by_committee(self, debts_owed_by_committee):
        """Sets the debts_owed_by_committee of this CandidateTotal.


        :param debts_owed_by_committee: The debts_owed_by_committee of this CandidateTotal.  # noqa: E501
        :type: float
        """

        self._debts_owed_by_committee = debts_owed_by_committee

    @property
    def disbursements(self):
        """Gets the disbursements of this CandidateTotal.  # noqa: E501


        :return: The disbursements of this CandidateTotal.  # noqa: E501
        :rtype: float
        """
        return self._disbursements

    @disbursements.setter
    def disbursements(self, disbursements):
        """Sets the disbursements of this CandidateTotal.


        :param disbursements: The disbursements of this CandidateTotal.  # noqa: E501
        :type: float
        """

        self._disbursements = disbursements

    @property
    def election_year(self):
        """Gets the election_year of this CandidateTotal.  # noqa: E501


        :return: The election_year of this CandidateTotal.  # noqa: E501
        :rtype: int
        """
        return self._election_year

    @election_year.setter
    def election_year(self, election_year):
        """Sets the election_year of this CandidateTotal.


        :param election_year: The election_year of this CandidateTotal.  # noqa: E501
        :type: int
        """

        self._election_year = election_year

    @property
    def federal_funds_flag(self):
        """Gets the federal_funds_flag of this CandidateTotal.  # noqa: E501

        A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.  # noqa: E501

        :return: The federal_funds_flag of this CandidateTotal.  # noqa: E501
        :rtype: bool
        """
        return self._federal_funds_flag

    @federal_funds_flag.setter
    def federal_funds_flag(self, federal_funds_flag):
        """Sets the federal_funds_flag of this CandidateTotal.

        A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.  # noqa: E501

        :param federal_funds_flag: The federal_funds_flag of this CandidateTotal.  # noqa: E501
        :type: bool
        """

        self._federal_funds_flag = federal_funds_flag

    @property
    def has_raised_funds(self):
        """Gets the has_raised_funds of this CandidateTotal.  # noqa: E501

        A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)  # noqa: E501

        :return: The has_raised_funds of this CandidateTotal.  # noqa: E501
        :rtype: bool
        """
        return self._has_raised_funds

    @has_raised_funds.setter
    def has_raised_funds(self, has_raised_funds):
        """Sets the has_raised_funds of this CandidateTotal.

        A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)  # noqa: E501

        :param has_raised_funds: The has_raised_funds of this CandidateTotal.  # noqa: E501
        :type: bool
        """

        self._has_raised_funds = has_raised_funds

    @property
    def is_election(self):
        """Gets the is_election of this CandidateTotal.  # noqa: E501


        :return: The is_election of this CandidateTotal.  # noqa: E501
        :rtype: bool
        """
        return self._is_election

    @is_election.setter
    def is_election(self, is_election):
        """Sets the is_election of this CandidateTotal.


        :param is_election: The is_election of this CandidateTotal.  # noqa: E501
        :type: bool
        """
        if is_election is None:
            raise ValueError("Invalid value for `is_election`, must not be `None`")  # noqa: E501

        self._is_election = is_election

    @property
    def office(self):
        """Gets the office of this CandidateTotal.  # noqa: E501

        Federal office candidate runs for: H, S or P  # noqa: E501

        :return: The office of this CandidateTotal.  # noqa: E501
        :rtype: str
        """
        return self._office

    @office.setter
    def office(self, office):
        """Sets the office of this CandidateTotal.

        Federal office candidate runs for: H, S or P  # noqa: E501

        :param office: The office of this CandidateTotal.  # noqa: E501
        :type: str
        """
        if office is not None and len(office) > 1:
            raise ValueError("Invalid value for `office`, length must be less than or equal to `1`")  # noqa: E501

        self._office = office

    @property
    def party(self):
        """Gets the party of this CandidateTotal.  # noqa: E501

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :return: The party of this CandidateTotal.  # noqa: E501
        :rtype: str
        """
        return self._party

    @party.setter
    def party(self, party):
        """Sets the party of this CandidateTotal.

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :param party: The party of this CandidateTotal.  # noqa: E501
        :type: str
        """
        if party is not None and len(party) > 3:
            raise ValueError("Invalid value for `party`, length must be less than or equal to `3`")  # noqa: E501

        self._party = party

    @property
    def receipts(self):
        """Gets the receipts of this CandidateTotal.  # noqa: E501


        :return: The receipts of this CandidateTotal.  # noqa: E501
        :rtype: float
        """
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        """Sets the receipts of this CandidateTotal.


        :param receipts: The receipts of this CandidateTotal.  # noqa: E501
        :type: float
        """

        self._receipts = receipts

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
        if issubclass(CandidateTotal, dict):
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
        if not isinstance(other, CandidateTotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
