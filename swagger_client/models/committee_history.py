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


class CommitteeHistory(object):
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
        'affiliated_committee_name': 'str',
        'candidate_ids': 'list[str]',
        'city': 'str',
        'committee_id': 'str',
        'committee_type': 'str',
        'committee_type_full': 'str',
        'cycle': 'int',
        'cycles': 'list[int]',
        'cycles_has_activity': 'list[int]',
        'cycles_has_financial': 'list[int]',
        'designation': 'str',
        'designation_full': 'str',
        'filing_frequency': 'str',
        'is_active': 'bool',
        'last_cycle_has_activity': 'int',
        'last_cycle_has_financial': 'int',
        'name': 'str',
        'organization_type': 'str',
        'organization_type_full': 'str',
        'party': 'str',
        'party_full': 'str',
        'state': 'str',
        'state_full': 'str',
        'street_1': 'str',
        'street_2': 'str',
        'treasurer_name': 'str',
        'zip': 'str'
    }

    attribute_map = {
        'affiliated_committee_name': 'affiliated_committee_name',
        'candidate_ids': 'candidate_ids',
        'city': 'city',
        'committee_id': 'committee_id',
        'committee_type': 'committee_type',
        'committee_type_full': 'committee_type_full',
        'cycle': 'cycle',
        'cycles': 'cycles',
        'cycles_has_activity': 'cycles_has_activity',
        'cycles_has_financial': 'cycles_has_financial',
        'designation': 'designation',
        'designation_full': 'designation_full',
        'filing_frequency': 'filing_frequency',
        'is_active': 'is_active',
        'last_cycle_has_activity': 'last_cycle_has_activity',
        'last_cycle_has_financial': 'last_cycle_has_financial',
        'name': 'name',
        'organization_type': 'organization_type',
        'organization_type_full': 'organization_type_full',
        'party': 'party',
        'party_full': 'party_full',
        'state': 'state',
        'state_full': 'state_full',
        'street_1': 'street_1',
        'street_2': 'street_2',
        'treasurer_name': 'treasurer_name',
        'zip': 'zip'
    }

    def __init__(self, affiliated_committee_name=None, candidate_ids=None, city=None, committee_id=None, committee_type=None, committee_type_full=None, cycle=None, cycles=None, cycles_has_activity=None, cycles_has_financial=None, designation=None, designation_full=None, filing_frequency=None, is_active=None, last_cycle_has_activity=None, last_cycle_has_financial=None, name=None, organization_type=None, organization_type_full=None, party=None, party_full=None, state=None, state_full=None, street_1=None, street_2=None, treasurer_name=None, zip=None):  # noqa: E501
        """CommitteeHistory - a model defined in Swagger"""  # noqa: E501

        self._affiliated_committee_name = None
        self._candidate_ids = None
        self._city = None
        self._committee_id = None
        self._committee_type = None
        self._committee_type_full = None
        self._cycle = None
        self._cycles = None
        self._cycles_has_activity = None
        self._cycles_has_financial = None
        self._designation = None
        self._designation_full = None
        self._filing_frequency = None
        self._is_active = None
        self._last_cycle_has_activity = None
        self._last_cycle_has_financial = None
        self._name = None
        self._organization_type = None
        self._organization_type_full = None
        self._party = None
        self._party_full = None
        self._state = None
        self._state_full = None
        self._street_1 = None
        self._street_2 = None
        self._treasurer_name = None
        self._zip = None
        self.discriminator = None

        if affiliated_committee_name is not None:
            self.affiliated_committee_name = affiliated_committee_name
        if candidate_ids is not None:
            self.candidate_ids = candidate_ids
        if city is not None:
            self.city = city
        self.committee_id = committee_id
        if committee_type is not None:
            self.committee_type = committee_type
        if committee_type_full is not None:
            self.committee_type_full = committee_type_full
        self.cycle = cycle
        if cycles is not None:
            self.cycles = cycles
        if cycles_has_activity is not None:
            self.cycles_has_activity = cycles_has_activity
        if cycles_has_financial is not None:
            self.cycles_has_financial = cycles_has_financial
        if designation is not None:
            self.designation = designation
        if designation_full is not None:
            self.designation_full = designation_full
        if filing_frequency is not None:
            self.filing_frequency = filing_frequency
        if is_active is not None:
            self.is_active = is_active
        if last_cycle_has_activity is not None:
            self.last_cycle_has_activity = last_cycle_has_activity
        if last_cycle_has_financial is not None:
            self.last_cycle_has_financial = last_cycle_has_financial
        if name is not None:
            self.name = name
        if organization_type is not None:
            self.organization_type = organization_type
        if organization_type_full is not None:
            self.organization_type_full = organization_type_full
        if party is not None:
            self.party = party
        if party_full is not None:
            self.party_full = party_full
        if state is not None:
            self.state = state
        if state_full is not None:
            self.state_full = state_full
        if street_1 is not None:
            self.street_1 = street_1
        if street_2 is not None:
            self.street_2 = street_2
        if treasurer_name is not None:
            self.treasurer_name = treasurer_name
        if zip is not None:
            self.zip = zip

    @property
    def affiliated_committee_name(self):
        """Gets the affiliated_committee_name of this CommitteeHistory.  # noqa: E501

         Affiliated committee or connected organization   # noqa: E501

        :return: The affiliated_committee_name of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._affiliated_committee_name

    @affiliated_committee_name.setter
    def affiliated_committee_name(self, affiliated_committee_name):
        """Sets the affiliated_committee_name of this CommitteeHistory.

         Affiliated committee or connected organization   # noqa: E501

        :param affiliated_committee_name: The affiliated_committee_name of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if affiliated_committee_name is not None and len(affiliated_committee_name) > 100:
            raise ValueError("Invalid value for `affiliated_committee_name`, length must be less than or equal to `100`")  # noqa: E501

        self._affiliated_committee_name = affiliated_committee_name

    @property
    def candidate_ids(self):
        """Gets the candidate_ids of this CommitteeHistory.  # noqa: E501

         A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   # noqa: E501

        :return: The candidate_ids of this CommitteeHistory.  # noqa: E501
        :rtype: list[str]
        """
        return self._candidate_ids

    @candidate_ids.setter
    def candidate_ids(self, candidate_ids):
        """Sets the candidate_ids of this CommitteeHistory.

         A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   # noqa: E501

        :param candidate_ids: The candidate_ids of this CommitteeHistory.  # noqa: E501
        :type: list[str]
        """

        self._candidate_ids = candidate_ids

    @property
    def city(self):
        """Gets the city of this CommitteeHistory.  # noqa: E501

         City of committee as reported on the Form 1   # noqa: E501

        :return: The city of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CommitteeHistory.

         City of committee as reported on the Form 1   # noqa: E501

        :param city: The city of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 50:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `50`")  # noqa: E501

        self._city = city

    @property
    def committee_id(self):
        """Gets the committee_id of this CommitteeHistory.  # noqa: E501

         A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.   # noqa: E501

        :return: The committee_id of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this CommitteeHistory.

         A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.   # noqa: E501

        :param committee_id: The committee_id of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if committee_id is None:
            raise ValueError("Invalid value for `committee_id`, must not be `None`")  # noqa: E501

        self._committee_id = committee_id

    @property
    def committee_type(self):
        """Gets the committee_type of this CommitteeHistory.  # noqa: E501

        The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account   # noqa: E501

        :return: The committee_type of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._committee_type

    @committee_type.setter
    def committee_type(self, committee_type):
        """Sets the committee_type of this CommitteeHistory.

        The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account   # noqa: E501

        :param committee_type: The committee_type of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if committee_type is not None and len(committee_type) > 1:
            raise ValueError("Invalid value for `committee_type`, length must be less than or equal to `1`")  # noqa: E501

        self._committee_type = committee_type

    @property
    def committee_type_full(self):
        """Gets the committee_type_full of this CommitteeHistory.  # noqa: E501

        The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account   # noqa: E501

        :return: The committee_type_full of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._committee_type_full

    @committee_type_full.setter
    def committee_type_full(self, committee_type_full):
        """Sets the committee_type_full of this CommitteeHistory.

        The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account   # noqa: E501

        :param committee_type_full: The committee_type_full of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if committee_type_full is not None and len(committee_type_full) > 50:
            raise ValueError("Invalid value for `committee_type_full`, length must be less than or equal to `50`")  # noqa: E501

        self._committee_type_full = committee_type_full

    @property
    def cycle(self):
        """Gets the cycle of this CommitteeHistory.  # noqa: E501

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :return: The cycle of this CommitteeHistory.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this CommitteeHistory.

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :param cycle: The cycle of this CommitteeHistory.  # noqa: E501
        :type: int
        """
        if cycle is None:
            raise ValueError("Invalid value for `cycle`, must not be `None`")  # noqa: E501

        self._cycle = cycle

    @property
    def cycles(self):
        """Gets the cycles of this CommitteeHistory.  # noqa: E501

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :return: The cycles of this CommitteeHistory.  # noqa: E501
        :rtype: list[int]
        """
        return self._cycles

    @cycles.setter
    def cycles(self, cycles):
        """Sets the cycles of this CommitteeHistory.

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :param cycles: The cycles of this CommitteeHistory.  # noqa: E501
        :type: list[int]
        """

        self._cycles = cycles

    @property
    def cycles_has_activity(self):
        """Gets the cycles_has_activity of this CommitteeHistory.  # noqa: E501

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1), and the committee has filling activity during the cycle   # noqa: E501

        :return: The cycles_has_activity of this CommitteeHistory.  # noqa: E501
        :rtype: list[int]
        """
        return self._cycles_has_activity

    @cycles_has_activity.setter
    def cycles_has_activity(self, cycles_has_activity):
        """Sets the cycles_has_activity of this CommitteeHistory.

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1), and the committee has filling activity during the cycle   # noqa: E501

        :param cycles_has_activity: The cycles_has_activity of this CommitteeHistory.  # noqa: E501
        :type: list[int]
        """

        self._cycles_has_activity = cycles_has_activity

    @property
    def cycles_has_financial(self):
        """Gets the cycles_has_financial of this CommitteeHistory.  # noqa: E501

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s), and the commitee files the financial reports ('F3', 'F3X', 'F3P', 'F3L', 'F4', 'F5', 'F7', 'F13') during this cycle.   # noqa: E501

        :return: The cycles_has_financial of this CommitteeHistory.  # noqa: E501
        :rtype: list[int]
        """
        return self._cycles_has_financial

    @cycles_has_financial.setter
    def cycles_has_financial(self, cycles_has_financial):
        """Sets the cycles_has_financial of this CommitteeHistory.

         A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s), and the commitee files the financial reports ('F3', 'F3X', 'F3P', 'F3L', 'F4', 'F5', 'F7', 'F13') during this cycle.   # noqa: E501

        :param cycles_has_financial: The cycles_has_financial of this CommitteeHistory.  # noqa: E501
        :type: list[int]
        """

        self._cycles_has_financial = cycles_has_financial

    @property
    def designation(self):
        """Gets the designation of this CommitteeHistory.  # noqa: E501

        The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC   # noqa: E501

        :return: The designation of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._designation

    @designation.setter
    def designation(self, designation):
        """Sets the designation of this CommitteeHistory.

        The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC   # noqa: E501

        :param designation: The designation of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if designation is not None and len(designation) > 1:
            raise ValueError("Invalid value for `designation`, length must be less than or equal to `1`")  # noqa: E501

        self._designation = designation

    @property
    def designation_full(self):
        """Gets the designation_full of this CommitteeHistory.  # noqa: E501

        The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC   # noqa: E501

        :return: The designation_full of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._designation_full

    @designation_full.setter
    def designation_full(self, designation_full):
        """Sets the designation_full of this CommitteeHistory.

        The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC   # noqa: E501

        :param designation_full: The designation_full of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        # if designation_full is not None and len(designation_full) > 25:
        #     raise ValueError("Invalid value for `designation_full`, length must be less than or equal to `25`")  # noqa: E501

        self._designation_full = designation_full

    @property
    def filing_frequency(self):
        """Gets the filing_frequency of this CommitteeHistory.  # noqa: E501

        The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived   # noqa: E501

        :return: The filing_frequency of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._filing_frequency

    @filing_frequency.setter
    def filing_frequency(self, filing_frequency):
        """Sets the filing_frequency of this CommitteeHistory.

        The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived   # noqa: E501

        :param filing_frequency: The filing_frequency of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if filing_frequency is not None and len(filing_frequency) > 1:
            raise ValueError("Invalid value for `filing_frequency`, length must be less than or equal to `1`")  # noqa: E501

        self._filing_frequency = filing_frequency

    @property
    def is_active(self):
        """Gets the is_active of this CommitteeHistory.  # noqa: E501

         True indicates that a committee is active.   # noqa: E501

        :return: The is_active of this CommitteeHistory.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this CommitteeHistory.

         True indicates that a committee is active.   # noqa: E501

        :param is_active: The is_active of this CommitteeHistory.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def last_cycle_has_activity(self):
        """Gets the last_cycle_has_activity of this CommitteeHistory.  # noqa: E501

         The latest two year election cycle that the committee has filings   # noqa: E501

        :return: The last_cycle_has_activity of this CommitteeHistory.  # noqa: E501
        :rtype: int
        """
        return self._last_cycle_has_activity

    @last_cycle_has_activity.setter
    def last_cycle_has_activity(self, last_cycle_has_activity):
        """Sets the last_cycle_has_activity of this CommitteeHistory.

         The latest two year election cycle that the committee has filings   # noqa: E501

        :param last_cycle_has_activity: The last_cycle_has_activity of this CommitteeHistory.  # noqa: E501
        :type: int
        """

        self._last_cycle_has_activity = last_cycle_has_activity

    @property
    def last_cycle_has_financial(self):
        """Gets the last_cycle_has_financial of this CommitteeHistory.  # noqa: E501

         The latest two year election cycle that the committee files the financial reports ('F3', 'F3X', 'F3P', 'F3L', 'F4', 'F5', 'F7', 'F13').   # noqa: E501

        :return: The last_cycle_has_financial of this CommitteeHistory.  # noqa: E501
        :rtype: int
        """
        return self._last_cycle_has_financial

    @last_cycle_has_financial.setter
    def last_cycle_has_financial(self, last_cycle_has_financial):
        """Sets the last_cycle_has_financial of this CommitteeHistory.

         The latest two year election cycle that the committee files the financial reports ('F3', 'F3X', 'F3P', 'F3L', 'F4', 'F5', 'F7', 'F13').   # noqa: E501

        :param last_cycle_has_financial: The last_cycle_has_financial of this CommitteeHistory.  # noqa: E501
        :type: int
        """

        self._last_cycle_has_financial = last_cycle_has_financial

    @property
    def name(self):
        """Gets the name of this CommitteeHistory.  # noqa: E501

        The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.  # noqa: E501

        :return: The name of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommitteeHistory.

        The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.  # noqa: E501

        :param name: The name of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def organization_type(self):
        """Gets the organization_type of this CommitteeHistory.  # noqa: E501

        The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock   # noqa: E501

        :return: The organization_type of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._organization_type

    @organization_type.setter
    def organization_type(self, organization_type):
        """Sets the organization_type of this CommitteeHistory.

        The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock   # noqa: E501

        :param organization_type: The organization_type of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if organization_type is not None and len(organization_type) > 1:
            raise ValueError("Invalid value for `organization_type`, length must be less than or equal to `1`")  # noqa: E501

        self._organization_type = organization_type

    @property
    def organization_type_full(self):
        """Gets the organization_type_full of this CommitteeHistory.  # noqa: E501

        The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock   # noqa: E501

        :return: The organization_type_full of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._organization_type_full

    @organization_type_full.setter
    def organization_type_full(self, organization_type_full):
        """Sets the organization_type_full of this CommitteeHistory.

        The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock   # noqa: E501

        :param organization_type_full: The organization_type_full of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if organization_type_full is not None and len(organization_type_full) > 100:
            raise ValueError("Invalid value for `organization_type_full`, length must be less than or equal to `100`")  # noqa: E501

        self._organization_type_full = organization_type_full

    @property
    def party(self):
        """Gets the party of this CommitteeHistory.  # noqa: E501

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :return: The party of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._party

    @party.setter
    def party(self, party):
        """Sets the party of this CommitteeHistory.

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :param party: The party of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if party is not None and len(party) > 3:
            raise ValueError("Invalid value for `party`, length must be less than or equal to `3`")  # noqa: E501

        self._party = party

    @property
    def party_full(self):
        """Gets the party_full of this CommitteeHistory.  # noqa: E501

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :return: The party_full of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._party_full

    @party_full.setter
    def party_full(self, party_full):
        """Sets the party_full of this CommitteeHistory.

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :param party_full: The party_full of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if party_full is not None and len(party_full) > 50:
            raise ValueError("Invalid value for `party_full`, length must be less than or equal to `50`")  # noqa: E501

        self._party_full = party_full

    @property
    def state(self):
        """Gets the state of this CommitteeHistory.  # noqa: E501

         State of the committee's address as filed on the Form 1   # noqa: E501

        :return: The state of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CommitteeHistory.

         State of the committee's address as filed on the Form 1   # noqa: E501

        :param state: The state of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if state is not None and len(state) > 2:
            raise ValueError("Invalid value for `state`, length must be less than or equal to `2`")  # noqa: E501

        self._state = state

    @property
    def state_full(self):
        """Gets the state_full of this CommitteeHistory.  # noqa: E501

         State of committee as reported on the Form 1   # noqa: E501

        :return: The state_full of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._state_full

    @state_full.setter
    def state_full(self, state_full):
        """Sets the state_full of this CommitteeHistory.

         State of committee as reported on the Form 1   # noqa: E501

        :param state_full: The state_full of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if state_full is not None and len(state_full) > 50:
            raise ValueError("Invalid value for `state_full`, length must be less than or equal to `50`")  # noqa: E501

        self._state_full = state_full

    @property
    def street_1(self):
        """Gets the street_1 of this CommitteeHistory.  # noqa: E501

         Street address of committee as reported on the Form 1   # noqa: E501

        :return: The street_1 of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._street_1

    @street_1.setter
    def street_1(self, street_1):
        """Sets the street_1 of this CommitteeHistory.

         Street address of committee as reported on the Form 1   # noqa: E501

        :param street_1: The street_1 of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if street_1 is not None and len(street_1) > 50:
            raise ValueError("Invalid value for `street_1`, length must be less than or equal to `50`")  # noqa: E501

        self._street_1 = street_1

    @property
    def street_2(self):
        """Gets the street_2 of this CommitteeHistory.  # noqa: E501

         Second line of street address of committee as reported on the Form 1   # noqa: E501

        :return: The street_2 of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._street_2

    @street_2.setter
    def street_2(self, street_2):
        """Sets the street_2 of this CommitteeHistory.

         Second line of street address of committee as reported on the Form 1   # noqa: E501

        :param street_2: The street_2 of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if street_2 is not None and len(street_2) > 50:
            raise ValueError("Invalid value for `street_2`, length must be less than or equal to `50`")  # noqa: E501

        self._street_2 = street_2

    @property
    def treasurer_name(self):
        """Gets the treasurer_name of this CommitteeHistory.  # noqa: E501

        Name of the Committee's treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown.  # noqa: E501

        :return: The treasurer_name of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._treasurer_name

    @treasurer_name.setter
    def treasurer_name(self, treasurer_name):
        """Sets the treasurer_name of this CommitteeHistory.

        Name of the Committee's treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown.  # noqa: E501

        :param treasurer_name: The treasurer_name of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if treasurer_name is not None and len(treasurer_name) > 100:
            raise ValueError("Invalid value for `treasurer_name`, length must be less than or equal to `100`")  # noqa: E501

        self._treasurer_name = treasurer_name

    @property
    def zip(self):
        """Gets the zip of this CommitteeHistory.  # noqa: E501

         Zip code of committee as reported on the Form 1   # noqa: E501

        :return: The zip of this CommitteeHistory.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this CommitteeHistory.

         Zip code of committee as reported on the Form 1   # noqa: E501

        :param zip: The zip of this CommitteeHistory.  # noqa: E501
        :type: str
        """
        if zip is not None and len(zip) > 9:
            raise ValueError("Invalid value for `zip`, length must be less than or equal to `9`")  # noqa: E501

        self._zip = zip

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
        if issubclass(CommitteeHistory, dict):
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
        if not isinstance(other, CommitteeHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
