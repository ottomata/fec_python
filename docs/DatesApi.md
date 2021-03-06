# swagger_client.DatesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_dates_export_get**](DatesApi.md#calendar_dates_export_get) | **GET** /calendar-dates/export/ | 
[**calendar_dates_get**](DatesApi.md#calendar_dates_get) | **GET** /calendar-dates/ | 
[**election_dates_get**](DatesApi.md#election_dates_get) | **GET** /election-dates/ | 
[**reporting_dates_get**](DatesApi.md#reporting_dates_get) | **GET** /reporting-dates/ | 


# **calendar_dates_export_get**
> CalendarDatePage calendar_dates_export_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, description=description, min_start_date=min_start_date, max_end_date=max_end_date, renderer=renderer, max_start_date=max_start_date, min_end_date=min_end_date, per_page=per_page, sort_nulls_last=sort_nulls_last, calendar_category_id=calendar_category_id, summary=summary, event_id=event_id)



 Returns CSV or ICS for downloading directly into calendar applications like Google, Outlook or other applications.  Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State filtering now applies to elections, reports and reporting periods.  Presidential pre-primary report due dates are not shown on even years. Filers generally opt to file monthly rather than submit over 50 pre-primary election reports. All reporting deadlines are available at /reporting-dates/ for reference.  This is [the sql function](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V40__omnibus_dates.sql) that creates the calendar.  

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
api_instance = swagger_client.DatesApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = '-start_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -start_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
description = ['description_example'] # list[str] | Brief description of event (optional)
min_start_date = '2013-10-20' # date |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_end_date = '2013-10-20' # date |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
renderer = 'ics' # str |  (optional) (default to ics)
max_start_date = '2013-10-20' # date |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_end_date = '2013-10-20' # date |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
calendar_category_id = [56] # list[int] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  (optional)
summary = ['summary_example'] # list[str] | Longer description of event (optional)
event_id = 56 # int | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. (optional)

try:
    api_response = api_instance.calendar_dates_export_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, description=description, min_start_date=min_start_date, max_end_date=max_end_date, renderer=renderer, max_start_date=max_start_date, min_end_date=min_end_date, per_page=per_page, sort_nulls_last=sort_nulls_last, calendar_category_id=calendar_category_id, summary=summary, event_id=event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatesApi->calendar_dates_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -start_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **description** | [**list[str]**](str.md)| Brief description of event | [optional] 
 **min_start_date** | **date**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_end_date** | **date**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **renderer** | **str**|  | [optional] [default to ics]
 **max_start_date** | **date**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_end_date** | **date**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **calendar_category_id** | [**list[int]**](int.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
 **summary** | [**list[str]**](str.md)| Longer description of event | [optional] 
 **event_id** | **int**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_dates_get**
> CalendarDatePage calendar_dates_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, description=description, min_start_date=min_start_date, max_end_date=max_end_date, max_start_date=max_start_date, min_end_date=min_end_date, per_page=per_page, sort_nulls_last=sort_nulls_last, calendar_category_id=calendar_category_id, summary=summary, event_id=event_id)



 Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State and report type filtering is no longer available. 

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
api_instance = swagger_client.DatesApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = '-start_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -start_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
description = ['description_example'] # list[str] | Brief description of event (optional)
min_start_date = '2013-10-20' # date |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_end_date = '2013-10-20' # date |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_start_date = '2013-10-20' # date |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_end_date = '2013-10-20' # date |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
calendar_category_id = [56] # list[int] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  (optional)
summary = ['summary_example'] # list[str] | Longer description of event (optional)
event_id = 56 # int | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. (optional)

try:
    api_response = api_instance.calendar_dates_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, description=description, min_start_date=min_start_date, max_end_date=max_end_date, max_start_date=max_start_date, min_end_date=min_end_date, per_page=per_page, sort_nulls_last=sort_nulls_last, calendar_category_id=calendar_category_id, summary=summary, event_id=event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatesApi->calendar_dates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -start_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **description** | [**list[str]**](str.md)| Brief description of event | [optional] 
 **min_start_date** | **date**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_end_date** | **date**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_start_date** | **date**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_end_date** | **date**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **calendar_category_id** | [**list[int]**](int.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
 **summary** | [**list[str]**](str.md)| Longer description of event | [optional] 
 **event_id** | **int**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **election_dates_get**
> InlineResponseDefault election_dates_get(api_key, max_primary_general_date=max_primary_general_date, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_create_date=min_create_date, min_update_date=min_update_date, election_year=election_year, election_state=election_state, max_election_date=max_election_date, election_type_id=election_type_id, election_district=election_district, office_sought=office_sought, sort_nulls_last=sort_nulls_last, sort=sort, page=page, election_party=election_party, min_primary_general_date=min_primary_general_date, max_create_date=max_create_date, max_update_date=max_update_date, per_page=per_page, min_election_date=min_election_date)



 FEC election dates since 1995. 

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
api_instance = swagger_client.DatesApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
max_primary_general_date = '2013-10-20' # date |  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_create_date = '2013-10-20' # date |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_update_date = '2013-10-20' # date |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
election_year = ['election_year_example'] # list[str] | Year of election (optional)
election_state = ['election_state_example'] # list[str] |  State or territory of the office sought.  (optional)
max_election_date = '2013-10-20' # date |  The maximum date of election.  (optional)
election_type_id = ['election_type_id_example'] # list[str] |  Election type id  (optional)
election_district = ['election_district_example'] # list[str] |  House district of the office sought, if applicable.  (optional)
office_sought = ['office_sought_example'] # list[str] |  House, Senate or presidential office.  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort = '-election_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -election_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
election_party = ['election_party_example'] # list[str] |  Party, if applicable.  (optional)
min_primary_general_date = '2013-10-20' # date |  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_create_date = '2013-10-20' # date |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_update_date = '2013-10-20' # date |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
min_election_date = '2013-10-20' # date |  The minimum date of election.  (optional)

try:
    api_response = api_instance.election_dates_get(api_key, max_primary_general_date=max_primary_general_date, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_create_date=min_create_date, min_update_date=min_update_date, election_year=election_year, election_state=election_state, max_election_date=max_election_date, election_type_id=election_type_id, election_district=election_district, office_sought=office_sought, sort_nulls_last=sort_nulls_last, sort=sort, page=page, election_party=election_party, min_primary_general_date=min_primary_general_date, max_create_date=max_create_date, max_update_date=max_update_date, per_page=per_page, min_election_date=min_election_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatesApi->election_dates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **max_primary_general_date** | **date**|  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_create_date** | **date**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_update_date** | **date**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **election_year** | [**list[str]**](str.md)| Year of election | [optional] 
 **election_state** | [**list[str]**](str.md)|  State or territory of the office sought.  | [optional] 
 **max_election_date** | **date**|  The maximum date of election.  | [optional] 
 **election_type_id** | [**list[str]**](str.md)|  Election type id  | [optional] 
 **election_district** | [**list[str]**](str.md)|  House district of the office sought, if applicable.  | [optional] 
 **office_sought** | [**list[str]**](str.md)|  House, Senate or presidential office.  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -election_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **election_party** | [**list[str]**](str.md)|  Party, if applicable.  | [optional] 
 **min_primary_general_date** | **date**|  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_create_date** | **date**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_update_date** | **date**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **min_election_date** | **date**|  The minimum date of election.  | [optional] 

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reporting_dates_get**
> InlineResponseDefault2 reporting_dates_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_update_date=min_update_date, min_create_date=min_create_date, page=page, min_due_date=min_due_date, sort=sort, max_due_date=max_due_date, max_create_date=max_create_date, max_update_date=max_update_date, per_page=per_page, sort_nulls_last=sort_nulls_last, report_type=report_type, report_year=report_year)



 FEC election dates since 1995. 

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
api_instance = swagger_client.DatesApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_update_date = '2013-10-20' # date |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_create_date = '2013-10-20' # date |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_due_date = '2013-10-20' # date |  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort = '-due_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -due_date)
max_due_date = '2013-10-20' # date |  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_create_date = '2013-10-20' # date |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_update_date = '2013-10-20' # date |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
report_type = ['report_type_example'] # list[str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)
report_year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)

try:
    api_response = api_instance.reporting_dates_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_update_date=min_update_date, min_create_date=min_create_date, page=page, min_due_date=min_due_date, sort=sort, max_due_date=max_due_date, max_create_date=max_create_date, max_update_date=max_update_date, per_page=per_page, sort_nulls_last=sort_nulls_last, report_type=report_type, report_year=report_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatesApi->reporting_dates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_update_date** | **date**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_create_date** | **date**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_due_date** | **date**|  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -due_date]
 **max_due_date** | **date**|  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_create_date** | **date**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_update_date** | **date**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **report_type** | [**list[str]**](str.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **report_year** | [**list[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 

### Return type

[**InlineResponseDefault2**](InlineResponseDefault2.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

