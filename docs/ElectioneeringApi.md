# swagger_client.ElectioneeringApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**committee_committee_id_electioneering_by_candidate_get**](ElectioneeringApi.md#committee_committee_id_electioneering_by_candidate_get) | **GET** /committee/{committee_id}/electioneering/by_candidate/ | 
[**electioneering_aggregates_get**](ElectioneeringApi.md#electioneering_aggregates_get) | **GET** /electioneering/aggregates/ | 
[**electioneering_by_candidate_get**](ElectioneeringApi.md#electioneering_by_candidate_get) | **GET** /electioneering/by_candidate/ | 
[**electioneering_get**](ElectioneeringApi.md#electioneering_get) | **GET** /electioneering/ | 
[**electioneering_totals_by_candidate_get**](ElectioneeringApi.md#electioneering_totals_by_candidate_get) | **GET** /electioneering/totals/by_candidate/ | 


# **committee_committee_id_electioneering_by_candidate_get**
> ElectioneeringByCandidatePage committee_committee_id_electioneering_by_candidate_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



Electioneering costs aggregated by candidate

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
api_instance = swagger_client.ElectioneeringApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str | 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.committee_committee_id_electioneering_by_candidate_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectioneeringApi->committee_committee_id_electioneering_by_candidate_get: %s\n" % e)
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
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**ElectioneeringByCandidatePage**](ElectioneeringByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **electioneering_aggregates_get**
> ElectioneeringByCandidatePage electioneering_aggregates_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



Electioneering communications costs aggregates

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
api_instance = swagger_client.ElectioneeringApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.electioneering_aggregates_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectioneeringApi->electioneering_aggregates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**ElectioneeringByCandidatePage**](ElectioneeringByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **electioneering_by_candidate_get**
> ElectioneeringByCandidatePage electioneering_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



Electioneering costs aggregated by candidate

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
api_instance = swagger_client.ElectioneeringApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)

try:
    api_response = api_instance.electioneering_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, district=district, election_full=election_full, office=office, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectioneeringApi->electioneering_by_candidate_get: %s\n" % e)
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
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 

### Return type

[**ElectioneeringByCandidatePage**](ElectioneeringByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **electioneering_get**
> ElectioneeringPage electioneering_get(api_key, sort_null_only=sort_null_only, per_page=per_page, sort_hide_null=sort_hide_null, last_index=last_index, page=page, description=description, sort=sort, committee_id=committee_id, max_amount=max_amount, min_amount=min_amount, min_date=min_date, max_date=max_date, candidate_id=candidate_id, sort_nulls_last=sort_nulls_last, report_year=report_year)



 An electioneering communication is any broadcast, cable or satellite communication that fulfills each of the following conditions:  _The communication refers to a clearly identified federal candidate._  _The communication is publicly distributed by a television station, radio station, cable television system or satellite system for a fee._  _The communication is distributed within 60 days prior to a general election or 30 days prior to a primary election to federal office._ 

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
api_instance = swagger_client.ElectioneeringApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
last_index = 56 # int | Index of last result from previous page (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
description = 'description_example' # str |  (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
min_date = '2013-10-20' # date | Minimum disbursement date (optional)
max_date = '2013-10-20' # date | Maximum disbursement date (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
report_year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)

try:
    api_response = api_instance.electioneering_get(api_key, sort_null_only=sort_null_only, per_page=per_page, sort_hide_null=sort_hide_null, last_index=last_index, page=page, description=description, sort=sort, committee_id=committee_id, max_amount=max_amount, min_amount=min_amount, min_date=min_date, max_date=max_date, candidate_id=candidate_id, sort_nulls_last=sort_nulls_last, report_year=report_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectioneeringApi->electioneering_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **description** | **str**|  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **min_date** | **date**| Minimum disbursement date | [optional] 
 **max_date** | **date**| Maximum disbursement date | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **report_year** | [**list[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 

### Return type

[**ElectioneeringPage**](ElectioneeringPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **electioneering_totals_by_candidate_get**
> ECTotalsByCandidatePage electioneering_totals_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)



 Total electioneering communications spent on candidates by cycle or candidate election year 

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
api_instance = swagger_client.ElectioneeringApi(swagger_client.ApiClient(configuration))
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
    api_response = api_instance.electioneering_totals_by_candidate_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectioneeringApi->electioneering_totals_by_candidate_get: %s\n" % e)
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

[**ECTotalsByCandidatePage**](ECTotalsByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

