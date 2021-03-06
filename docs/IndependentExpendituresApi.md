# swagger_client.IndependentExpendituresApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_e_by_candidate_get**](IndependentExpendituresApi.md#schedules_schedule_e_by_candidate_get) | **GET** /schedules/schedule_e/by_candidate/ | 
[**schedules_schedule_e_efile_get**](IndependentExpendituresApi.md#schedules_schedule_e_efile_get) | **GET** /schedules/schedule_e/efile/ | 
[**schedules_schedule_e_get**](IndependentExpendituresApi.md#schedules_schedule_e_get) | **GET** /schedules/schedule_e/ | 
[**schedules_schedule_e_totals_by_candidate_get**](IndependentExpendituresApi.md#schedules_schedule_e_totals_by_candidate_get) | **GET** /schedules/schedule_e/totals/by_candidate/ | 


# **schedules_schedule_e_by_candidate_get**
> ScheduleEByCandidatePage schedules_schedule_e_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, support_oppose=support_oppose, election_full=election_full, committee_id=committee_id, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



 Schedule E receipts aggregated by recipient candidate. To avoid double counting, memoed items are not included. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.IndependentExpendituresApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
support_oppose = 'null' # str | Support or opposition (optional) (default to null)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.schedules_schedule_e_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, support_oppose=support_oppose, election_full=election_full, committee_id=committee_id, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **state** | **str**| US state or territory where a candidate runs for office | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **support_oppose** | **str**| Support or opposition | [optional] [default to null]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**ScheduleEByCandidatePage**](ScheduleEByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_e_efile_get**
> ScheduleEEfilePage schedules_schedule_e_efile_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, candidate_office_state=candidate_office_state, payee_name=payee_name, committee_id=committee_id, most_recent=most_recent, spender_name=spender_name, support_oppose_indicator=support_oppose_indicator, sort_nulls_last=sort_nulls_last, max_filed_date=max_filed_date, candidate_office=candidate_office, candidate_search=candidate_search, sort=sort, page=page, min_filed_date=min_filed_date, max_expenditure_amount=max_expenditure_amount, is_notice=is_notice, image_number=image_number, filing_form=filing_form, min_expenditure_amount=min_expenditure_amount, max_expenditure_date=max_expenditure_date, candidate_office_district=candidate_office_district, max_dissemination_date=max_dissemination_date, candidate_party=candidate_party, min_expenditure_date=min_expenditure_date, per_page=per_page, min_dissemination_date=min_dissemination_date, candidate_id=candidate_id)



 Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don't contain the processed and coded data that you can find on other endpoints. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.IndependentExpendituresApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
candidate_office_state = ['candidate_office_state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
payee_name = ['payee_name_example'] # list[str] |  Name of the entity that received the payment.  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
most_recent = true # bool |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included.  (optional)
spender_name = ['spender_name_example'] # list[str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)
support_oppose_indicator = ['support_oppose_indicator_example'] # list[str] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
max_filed_date = '2013-10-20' # date | Timestamp of electronic or paper record that FEC received (optional)
candidate_office = 'candidate_office_example' # str | Federal office candidate runs for: H, S or P (optional)
candidate_search = ['candidate_search_example'] # list[str] |  Search for candidates by candiate id or candidate first or last name  (optional)
sort = '-expenditure_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -expenditure_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_filed_date = '2013-10-20' # date | Timestamp of electronic or paper record that FEC received (optional)
max_expenditure_amount = 56 # int | Selects all items expended by this committee less than this amount (optional)
is_notice = true # bool |  Record filed as 24- or 48-hour notice.  (optional)
image_number = ['image_number_example'] # list[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
filing_form = ['filing_form_example'] # list[str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
min_expenditure_amount = 56 # int | Selects all items expended by this committee greater than this amount (optional)
max_expenditure_date = '2013-10-20' # date | Selects all items expended by this committee before this date (optional)
candidate_office_district = ['candidate_office_district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
max_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee before this date (optional)
candidate_party = ['candidate_party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
min_expenditure_date = '2013-10-20' # date | Selects all items expended by this committee after this date (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
min_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee after this date (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.schedules_schedule_e_efile_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, candidate_office_state=candidate_office_state, payee_name=payee_name, committee_id=committee_id, most_recent=most_recent, spender_name=spender_name, support_oppose_indicator=support_oppose_indicator, sort_nulls_last=sort_nulls_last, max_filed_date=max_filed_date, candidate_office=candidate_office, candidate_search=candidate_search, sort=sort, page=page, min_filed_date=min_filed_date, max_expenditure_amount=max_expenditure_amount, is_notice=is_notice, image_number=image_number, filing_form=filing_form, min_expenditure_amount=min_expenditure_amount, max_expenditure_date=max_expenditure_date, candidate_office_district=candidate_office_district, max_dissemination_date=max_dissemination_date, candidate_party=candidate_party, min_expenditure_date=min_expenditure_date, per_page=per_page, min_dissemination_date=min_dissemination_date, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_efile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidate_office_state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **payee_name** | [**list[str]**](str.md)|  Name of the entity that received the payment.  | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **most_recent** | **bool**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] 
 **spender_name** | [**list[str]**](str.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
 **support_oppose_indicator** | [**list[str]**](str.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **max_filed_date** | **date**| Timestamp of electronic or paper record that FEC received | [optional] 
 **candidate_office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **candidate_search** | [**list[str]**](str.md)|  Search for candidates by candiate id or candidate first or last name  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -expenditure_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_filed_date** | **date**| Timestamp of electronic or paper record that FEC received | [optional] 
 **max_expenditure_amount** | **int**| Selects all items expended by this committee less than this amount | [optional] 
 **is_notice** | **bool**|  Record filed as 24- or 48-hour notice.  | [optional] 
 **image_number** | [**list[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **filing_form** | [**list[str]**](str.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **min_expenditure_amount** | **int**| Selects all items expended by this committee greater than this amount | [optional] 
 **max_expenditure_date** | **date**| Selects all items expended by this committee before this date | [optional] 
 **candidate_office_district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **max_dissemination_date** | **date**| Selects all items distributed by this committee before this date | [optional] 
 **candidate_party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **min_expenditure_date** | **date**| Selects all items expended by this committee after this date | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **min_dissemination_date** | **date**| Selects all items distributed by this committee after this date | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**ScheduleEEfilePage**](ScheduleEEfilePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_e_get**
> ScheduleEPage schedules_schedule_e_get(api_key, min_filing_date=min_filing_date, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, line_number=line_number, candidate_office_state=candidate_office_state, payee_name=payee_name, last_expenditure_date=last_expenditure_date, support_oppose_indicator=support_oppose_indicator, max_date=max_date, sort_nulls_last=sort_nulls_last, candidate_office=candidate_office, sort=sort, max_amount=max_amount, last_expenditure_amount=last_expenditure_amount, candidate_party=candidate_party, per_page=per_page, cycle=cycle, candidate_id=candidate_id, max_image_number=max_image_number, min_date=min_date, last_support_oppose_indicator=last_support_oppose_indicator, committee_id=committee_id, most_recent=most_recent, last_office_total_ytd=last_office_total_ytd, is_notice=is_notice, last_index=last_index, max_filing_date=max_filing_date, min_amount=min_amount, candidate_office_district=candidate_office_district, min_image_number=min_image_number, max_dissemination_date=max_dissemination_date, image_number=image_number, min_dissemination_date=min_dissemination_date, filing_form=filing_form)



 Schedule E covers the line item expenditures for independent expenditures. For example, if a super PAC bought ads on TV to oppose a federal candidate, each ad purchase would be recorded here with the expenditure amount, name and id of the candidate, and whether the ad supported or opposed the candidate.  An independent expenditure is an expenditure for a communication \"expressly advocating the election or defeat of a clearly identified candidate that is not made in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate, a candidate’s authorized committee, or their agents, or a political party or its agents.\"  Aggregates by candidate do not include 24 and 48 hour reports. This ensures we don't double count expenditures and the totals are more accurate. You can still find the information from 24 and 48 hour reports in `/schedule/schedule_e/`.  Due to the large quantity of Schedule E filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the `last_indexes` object from `pagination` to the URL of your last request. For example, when sorting by `expenditure_amount`, you might receive a page of results with the following pagination information:  ```  \"pagination\": {     \"count\": 152623,     \"last_indexes\": {       \"last_index\": \"3023037\",       \"last_expenditure_amount\": -17348.5     },     \"per_page\": 20,     \"pages\": 7632   } } ```  To fetch the next page of sorted results, append `last_index=3023037` and `last_expenditure_amount=` to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. `last_disbursement_date`), otherwise some resources may be unintentionally filtered out.  This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule E data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.IndependentExpendituresApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
min_filing_date = '2013-10-20' # date |  Selects all filings received after this date  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
candidate_office_state = ['candidate_office_state_example'] # list[str] | US state or territory (optional)
payee_name = ['payee_name_example'] # list[str] |  Name of the entity that received the payment.  (optional)
last_expenditure_date = 'null' # date |  When sorting by `expenditure_date`, this is populated with the `expenditure_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.  (optional) (default to null)
support_oppose_indicator = ['support_oppose_indicator_example'] # list[str] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
candidate_office = ['candidate_office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)
sort = '-expenditure_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -expenditure_date)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
last_expenditure_amount = 3.4 # float |  When sorting by `expenditure_amount`, this is populated with the `expenditure_amount` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.  (optional)
candidate_party = ['candidate_party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_image_number = 'max_image_number_example' # str |  (optional)
min_date = '2013-10-20' # date | Minimum date (optional)
last_support_oppose_indicator = 'null' # str |  When sorting by `support_oppose_indicator`, this is populated with the `support_oppose_indicator` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.'  (optional) (default to null)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
most_recent = true # bool |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included.  (optional)
last_office_total_ytd = 3.4 # float |  When sorting by `office_total_ytd`, this is populated with the `office_total_ytd` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.'  (optional)
is_notice = [True] # list[bool] |  Record filed as 24- or 48-hour notice.  (optional)
last_index = 56 # int | Index of last result from previous page (optional)
max_filing_date = '2013-10-20' # date |  Selects all filings received before this date  (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
candidate_office_district = ['candidate_office_district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
max_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee before this date (optional)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
min_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee after this date (optional)
filing_form = ['filing_form_example'] # list[str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)

try:
    api_response = api_instance.schedules_schedule_e_get(api_key, min_filing_date=min_filing_date, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, line_number=line_number, candidate_office_state=candidate_office_state, payee_name=payee_name, last_expenditure_date=last_expenditure_date, support_oppose_indicator=support_oppose_indicator, max_date=max_date, sort_nulls_last=sort_nulls_last, candidate_office=candidate_office, sort=sort, max_amount=max_amount, last_expenditure_amount=last_expenditure_amount, candidate_party=candidate_party, per_page=per_page, cycle=cycle, candidate_id=candidate_id, max_image_number=max_image_number, min_date=min_date, last_support_oppose_indicator=last_support_oppose_indicator, committee_id=committee_id, most_recent=most_recent, last_office_total_ytd=last_office_total_ytd, is_notice=is_notice, last_index=last_index, max_filing_date=max_filing_date, min_amount=min_amount, candidate_office_district=candidate_office_district, min_image_number=min_image_number, max_dissemination_date=max_dissemination_date, image_number=image_number, min_dissemination_date=min_dissemination_date, filing_form=filing_form)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **min_filing_date** | **date**|  Selects all filings received after this date  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **candidate_office_state** | [**list[str]**](str.md)| US state or territory | [optional] 
 **payee_name** | [**list[str]**](str.md)|  Name of the entity that received the payment.  | [optional] 
 **last_expenditure_date** | **date**|  When sorting by &#x60;expenditure_date&#x60;, this is populated with the &#x60;expenditure_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] [default to null]
 **support_oppose_indicator** | [**list[str]**](str.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **candidate_office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -expenditure_date]
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **last_expenditure_amount** | **float**|  When sorting by &#x60;expenditure_amount&#x60;, this is populated with the &#x60;expenditure_amount&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] 
 **candidate_party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **max_image_number** | **str**|  | [optional] 
 **min_date** | **date**| Minimum date | [optional] 
 **last_support_oppose_indicator** | **str**|  When sorting by &#x60;support_oppose_indicator&#x60;, this is populated with the &#x60;support_oppose_indicator&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] [default to null]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **most_recent** | **bool**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] 
 **last_office_total_ytd** | **float**|  When sorting by &#x60;office_total_ytd&#x60;, this is populated with the &#x60;office_total_ytd&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] 
 **is_notice** | [**list[bool]**](bool.md)|  Record filed as 24- or 48-hour notice.  | [optional] 
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **max_filing_date** | **date**|  Selects all filings received before this date  | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **candidate_office_district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **max_dissemination_date** | **date**| Selects all items distributed by this committee before this date | [optional] 
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **min_dissemination_date** | **date**| Selects all items distributed by this committee after this date | [optional] 
 **filing_form** | [**list[str]**](str.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 

### Return type

[**ScheduleEPage**](ScheduleEPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_e_totals_by_candidate_get**
> IETotalsByCandidatePage schedules_schedule_e_totals_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



 Total independent expenditure on supported or opposed candidates by cycle or candidate election year. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.IndependentExpendituresApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.schedules_schedule_e_totals_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_totals_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**IETotalsByCandidatePage**](IETotalsByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

