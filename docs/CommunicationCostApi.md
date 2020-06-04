# swagger_client.CommunicationCostApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**committee_committee_id_communication_costs_by_candidate_get**](CommunicationCostApi.md#committee_committee_id_communication_costs_by_candidate_get) | **GET** /committee/{committee_id}/communication_costs/by_candidate/ | 
[**communication_costs_aggregates_get**](CommunicationCostApi.md#communication_costs_aggregates_get) | **GET** /communication_costs/aggregates/ | 
[**communication_costs_by_candidate_get**](CommunicationCostApi.md#communication_costs_by_candidate_get) | **GET** /communication_costs/by_candidate/ | 
[**communication_costs_get**](CommunicationCostApi.md#communication_costs_get) | **GET** /communication-costs/ | 
[**communication_costs_totals_by_candidate_get**](CommunicationCostApi.md#communication_costs_totals_by_candidate_get) | **GET** /communication_costs/totals/by_candidate/ | 


# **committee_committee_id_communication_costs_by_candidate_get**
> CommunicationCostByCandidatePage committee_committee_id_communication_costs_by_candidate_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, support_oppose=support_oppose, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



Communication cost aggregated by candidate ID and committee ID.

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
api_instance = swagger_client.CommunicationCostApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str | 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
support_oppose = 'null' # str | Support or opposition (optional) (default to null)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.committee_committee_id_communication_costs_by_candidate_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, support_oppose=support_oppose, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationCostApi->committee_committee_id_communication_costs_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **state** | **str**| US state or territory where a candidate runs for office | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **support_oppose** | **str**| Support or opposition | [optional] [default to null]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**CommunicationCostByCandidatePage**](CommunicationCostByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_costs_aggregates_get**
> CommunicationCostByCandidatePage communication_costs_aggregates_get(api_key, sort_null_only=sort_null_only, per_page=per_page, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, support_oppose_indicator=support_oppose_indicator, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



Communication cost aggregated by candidate ID and committee ID.

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
api_instance = swagger_client.CommunicationCostApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
support_oppose_indicator = 'null' # str | Support or opposition (optional) (default to null)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.communication_costs_aggregates_get(api_key, sort_null_only=sort_null_only, per_page=per_page, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, support_oppose_indicator=support_oppose_indicator, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationCostApi->communication_costs_aggregates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **support_oppose_indicator** | **str**| Support or opposition | [optional] [default to null]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**CommunicationCostByCandidatePage**](CommunicationCostByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_costs_by_candidate_get**
> CommunicationCostByCandidatePage communication_costs_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, support_oppose=support_oppose, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



Communication cost aggregated by candidate ID and committee ID.

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
api_instance = swagger_client.CommunicationCostApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
support_oppose = 'null' # str | Support or opposition (optional) (default to null)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.communication_costs_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, support_oppose=support_oppose, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationCostApi->communication_costs_by_candidate_get: %s\n" % e)
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
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**CommunicationCostByCandidatePage**](CommunicationCostByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_costs_get**
> CommunicationCostPage communication_costs_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, committee_id=committee_id, support_oppose_indicator=support_oppose_indicator, max_date=max_date, sort_nulls_last=sort_nulls_last, page=page, sort=sort, image_number=image_number, max_amount=max_amount, min_amount=min_amount, min_image_number=min_image_number, per_page=per_page, candidate_id=candidate_id, max_image_number=max_image_number)



 52 U.S.C. 30118 allows \"communications by a corporation to its stockholders and executive or administrative personnel and their families or by a labor organization to its members and their families on any subject,\" including the express advocacy of the election or defeat of any Federal candidate.  The costs of such communications must be reported to the Federal Election Commission under certain circumstances. 

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
api_instance = swagger_client.CommunicationCostApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_date = '2013-10-20' # date | Minimum date (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
support_oppose_indicator = ['support_oppose_indicator_example'] # list[str] | Support or opposition (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_image_number = 'max_image_number_example' # str |  (optional)

try:
    api_response = api_instance.communication_costs_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, committee_id=committee_id, support_oppose_indicator=support_oppose_indicator, max_date=max_date, sort_nulls_last=sort_nulls_last, page=page, sort=sort, image_number=image_number, max_amount=max_amount, min_amount=min_amount, min_image_number=min_image_number, per_page=per_page, candidate_id=candidate_id, max_image_number=max_image_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationCostApi->communication_costs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_date** | **date**| Minimum date | [optional] 
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **support_oppose_indicator** | [**list[str]**](str.md)| Support or opposition | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **max_image_number** | **str**|  | [optional] 

### Return type

[**CommunicationCostPage**](CommunicationCostPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_costs_totals_by_candidate_get**
> CCTotalsByCandidatePage communication_costs_totals_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



 Total communications costs aggregated across committees on supported or opposed candidates by cycle or candidate election year. 

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
api_instance = swagger_client.CommunicationCostApi(swagger_client.ApiClient(configuration))
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
    api_response = api_instance.communication_costs_totals_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationCostApi->communication_costs_totals_by_candidate_get: %s\n" % e)
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

[**CCTotalsByCandidatePage**](CCTotalsByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

