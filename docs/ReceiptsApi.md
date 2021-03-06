# swagger_client.ReceiptsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_a_by_employer_get**](ReceiptsApi.md#schedules_schedule_a_by_employer_get) | **GET** /schedules/schedule_a/by_employer/ | 
[**schedules_schedule_a_by_occupation_get**](ReceiptsApi.md#schedules_schedule_a_by_occupation_get) | **GET** /schedules/schedule_a/by_occupation/ | 
[**schedules_schedule_a_by_size_by_candidate_get**](ReceiptsApi.md#schedules_schedule_a_by_size_by_candidate_get) | **GET** /schedules/schedule_a/by_size/by_candidate/ | 
[**schedules_schedule_a_by_size_get**](ReceiptsApi.md#schedules_schedule_a_by_size_get) | **GET** /schedules/schedule_a/by_size/ | 
[**schedules_schedule_a_by_state_by_candidate_get**](ReceiptsApi.md#schedules_schedule_a_by_state_by_candidate_get) | **GET** /schedules/schedule_a/by_state/by_candidate/ | 
[**schedules_schedule_a_by_state_by_candidate_totals_get**](ReceiptsApi.md#schedules_schedule_a_by_state_by_candidate_totals_get) | **GET** /schedules/schedule_a/by_state/by_candidate/totals/ | 
[**schedules_schedule_a_by_state_get**](ReceiptsApi.md#schedules_schedule_a_by_state_get) | **GET** /schedules/schedule_a/by_state/ | 
[**schedules_schedule_a_by_state_totals_get**](ReceiptsApi.md#schedules_schedule_a_by_state_totals_get) | **GET** /schedules/schedule_a/by_state/totals/ | 
[**schedules_schedule_a_by_zip_get**](ReceiptsApi.md#schedules_schedule_a_by_zip_get) | **GET** /schedules/schedule_a/by_zip/ | 
[**schedules_schedule_a_efile_get**](ReceiptsApi.md#schedules_schedule_a_efile_get) | **GET** /schedules/schedule_a/efile/ | 
[**schedules_schedule_a_get**](ReceiptsApi.md#schedules_schedule_a_get) | **GET** /schedules/schedule_a/ | 
[**schedules_schedule_a_sub_id_get**](ReceiptsApi.md#schedules_schedule_a_sub_id_get) | **GET** /schedules/schedule_a/{sub_id}/ | 


# **schedules_schedule_a_by_employer_get**
> ScheduleAByEmployerPage schedules_schedule_a_by_employer_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, employer=employer, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s employer name. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/ about-receipts-data/) of our “about the data” page. Unitemized individual contributions are not included. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
employer = ['employer_example'] # list[str] | Employer of contributor as reported on the committee's filing (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.schedules_schedule_a_by_employer_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, employer=employer, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_employer_get: %s\n" % e)
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
 **employer** | [**list[str]**](str.md)| Employer of contributor as reported on the committee&#39;s filing | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**ScheduleAByEmployerPage**](ScheduleAByEmployerPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_occupation_get**
> ScheduleAByOccupationPage schedules_schedule_a_by_occupation_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, occupation=occupation, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s occupation. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/ about-receipts-data/) of our “about the data” page. Unitemized individual contributions are not included. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
occupation = ['occupation_example'] # list[str] | Occupation of contributor as reported on the committee's filing (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.schedules_schedule_a_by_occupation_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, occupation=occupation, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_occupation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **occupation** | [**list[str]**](str.md)| Occupation of contributor as reported on the committee&#39;s filing | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**ScheduleAByOccupationPage**](ScheduleAByOccupationPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_size_by_candidate_get**
> ScheduleABySizeCandidatePage schedules_schedule_a_by_size_by_candidate_get(cycle, candidate_id, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last)



 This endpoint provides itemized individual contributions received by a committee, aggregated by size of contribution and candidate. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/ about-campaign-finance-data/about-receipts-data/) of our “about the data” page. Unitemized individual contributions are not included. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.schedules_schedule_a_by_size_by_candidate_get(cycle, candidate_id, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_size_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**ScheduleABySizeCandidatePage**](ScheduleABySizeCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_size_get**
> ScheduleABySizePage schedules_schedule_a_by_size_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, size=size, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)



 This endpoint provides individual contributions received by a committee, aggregated by size:  ```  - $200 and under  - $200.01 - $499.99  - $500 - $999.99  - $1000 - $1999.99  - $2000 + ```  The $200.00 and under category includes contributions of $200 or less combined with unitemized individual contributions. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
size = [56] # list[int] |  The total all contributions in the following ranges: ```   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + ``` Unitemized contributions are included in the `0` category.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.schedules_schedule_a_by_size_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, size=size, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_size_get: %s\n" % e)
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
 **size** | [**list[int]**](int.md)|  The total all contributions in the following ranges: &#x60;&#x60;&#x60;   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + &#x60;&#x60;&#x60; Unitemized contributions are included in the &#x60;0&#x60; category.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**ScheduleABySizePage**](ScheduleABySizePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_state_by_candidate_get**
> ScheduleAByStateCandidatePage schedules_schedule_a_by_state_by_candidate_get(cycle, candidate_id, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last)



 This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state and candidate. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/ about-campaign-finance-data/about-receipts-data/) of our “about the data” page. Unitemized individual contributions are not included. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.schedules_schedule_a_by_state_by_candidate_get(cycle, candidate_id, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_state_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**ScheduleAByStateCandidatePage**](ScheduleAByStateCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_state_by_candidate_totals_get**
> ScheduleAByStateCandidatePage schedules_schedule_a_by_state_by_candidate_totals_get(cycle, candidate_id, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last)



 Itemized individual contributions aggregated by contributor’s state, candidate, committee type and cycle. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/about-receipts-data/) of our “about the data” page. Unitemized individual contributions are not included.  

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.schedules_schedule_a_by_state_by_candidate_totals_get(cycle, candidate_id, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_state_by_candidate_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**ScheduleAByStateCandidatePage**](ScheduleAByStateCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_state_get**
> ScheduleAByStatePage schedules_schedule_a_by_state_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, hide_null=hide_null, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s state. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/ about-receipts-data/) of our “about the data” page. Unitemized individual contributions are not included. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = ['state_example'] # list[str] | State of contributor (optional)
sort = '-total' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -total)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
hide_null = false # bool | Exclude values with missing state (optional) (default to false)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.schedules_schedule_a_by_state_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, hide_null=hide_null, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_state_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **state** | [**list[str]**](str.md)| State of contributor | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -total]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **hide_null** | **bool**| Exclude values with missing state | [optional] [default to false]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**ScheduleAByStatePage**](ScheduleAByStatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_state_totals_get**
> ScheduleAByStateRecipientTotalsPage schedules_schedule_a_by_state_totals_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, committee_type=committee_type, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)



 This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state, committee type and cycle. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/ about-campaign-finance-data/about-receipts-data/) of our “about the data” page. Unitemized individual contributions are not included. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = ['state_example'] # list[str] | US state or territory (optional)
sort = 'cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to cycle)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_type = ['committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account         - all All Committee Types         - all_candidates All Candidate Committee Types (H, S, P)         - all_pacs All PAC Committee Types (N, O, Q, V, W)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.schedules_schedule_a_by_state_totals_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, committee_type=committee_type, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_state_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **state** | [**list[str]**](str.md)| US state or territory | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to cycle]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account         - all All Committee Types         - all_candidates All Candidate Committee Types (H, S, P)         - all_pacs All PAC Committee Types (N, O, Q, V, W)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**ScheduleAByStateRecipientTotalsPage**](ScheduleAByStateRecipientTotalsPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_by_zip_get**
> ScheduleAByZipPage schedules_schedule_a_by_zip_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, zip=zip)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s ZIP code. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/ about-receipts-data/) section of our “about the data” page. Unitemized individual contributions are not included. 

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = ['state_example'] # list[str] | State of contributor (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
zip = ['zip_example'] # list[str] | Zip code of contributor (optional)

try:
    api_response = api_instance.schedules_schedule_a_by_zip_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, sort=sort, page=page, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, zip=zip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_by_zip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **state** | [**list[str]**](str.md)| State of contributor | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **zip** | [**list[str]**](str.md)| Zip code of contributor | [optional] 

### Return type

[**ScheduleAByZipPage**](ScheduleAByZipPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_efile_get**
> ScheduleAEfilePage schedules_schedule_a_efile_get(api_key, sort_null_only=sort_null_only, contributor_state=contributor_state, contributor_occupation=contributor_occupation, line_number=line_number, sort_hide_null=sort_hide_null, min_date=min_date, contributor_employer=contributor_employer, committee_id=committee_id, contributor_name=contributor_name, max_date=max_date, sort_nulls_last=sort_nulls_last, contributor_city=contributor_city, sort=sort, page=page, image_number=image_number, max_amount=max_amount, min_amount=min_amount, min_image_number=min_image_number, per_page=per_page, max_image_number=max_image_number)



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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
contributor_state = ['contributor_state_example'] # list[str] | State of contributor (optional)
contributor_occupation = ['contributor_occupation_example'] # list[str] | Occupation of contributor, filers need to make an effort to gather this information (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_date = '2013-10-20' # date | Minimum date (optional)
contributor_employer = ['contributor_employer_example'] # list[str] | Employer of contributor, filers need to make an effort to gather this information (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
contributor_name = ['contributor_name_example'] # list[str] | Name of contributor (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
contributor_city = ['contributor_city_example'] # list[str] | City of contributor (optional)
sort = '-contribution_receipt_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -contribution_receipt_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_image_number = 'max_image_number_example' # str |  (optional)

try:
    api_response = api_instance.schedules_schedule_a_efile_get(api_key, sort_null_only=sort_null_only, contributor_state=contributor_state, contributor_occupation=contributor_occupation, line_number=line_number, sort_hide_null=sort_hide_null, min_date=min_date, contributor_employer=contributor_employer, committee_id=committee_id, contributor_name=contributor_name, max_date=max_date, sort_nulls_last=sort_nulls_last, contributor_city=contributor_city, sort=sort, page=page, image_number=image_number, max_amount=max_amount, min_amount=min_amount, min_image_number=min_image_number, per_page=per_page, max_image_number=max_image_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_efile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **contributor_state** | [**list[str]**](str.md)| State of contributor | [optional] 
 **contributor_occupation** | [**list[str]**](str.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] 
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_date** | **date**| Minimum date | [optional] 
 **contributor_employer** | [**list[str]**](str.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **contributor_name** | [**list[str]**](str.md)| Name of contributor | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **contributor_city** | [**list[str]**](str.md)| City of contributor | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -contribution_receipt_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **max_image_number** | **str**|  | [optional] 

### Return type

[**ScheduleAEfilePage**](ScheduleAEfilePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_get**
> ScheduleAPage schedules_schedule_a_get(api_key, sort_null_only=sort_null_only, last_contributor_aggregate_ytd=last_contributor_aggregate_ytd, contributor_state=contributor_state, contributor_occupation=contributor_occupation, line_number=line_number, sort_hide_null=sort_hide_null, min_date=min_date, contributor_employer=contributor_employer, committee_id=committee_id, last_contribution_receipt_amount=last_contribution_receipt_amount, contributor_name=contributor_name, max_date=max_date, contributor_city=contributor_city, contributor_zip=contributor_zip, sort=sort, recipient_committee_designation=recipient_committee_designation, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, last_contribution_receipt_date=last_contribution_receipt_date, contributor_type=contributor_type, max_amount=max_amount, is_individual=is_individual, recipient_committee_type=recipient_committee_type, min_amount=min_amount, min_image_number=min_image_number, contributor_id=contributor_id, per_page=per_page, recipient_committee_org_type=recipient_committee_org_type, max_image_number=max_image_number)



 This description is for both ​`/schedules​/schedule_a​/` and ​ `/schedules​/schedule_a​/{sub_id}​/`.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the `/schedules/schedule_a/` endpoint. For a more complete description of all Schedule A records see the [receipts section] (https://www.fec.gov/campaign-finance-data/ about-campaign-finance-data/about-receipts-data/) of our “about the data” page. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/) of our “about the data” page.  ​The `/schedules​/schedule_a​/` endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the `last_indexes` object from pagination to the URL of your last request as additional parameters. For example, when sorting by `contribution_receipt_date`, you might receive a page of results with the following pagination information:  ``` pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \"230880619\",         last_contribution_receipt_date: \"2014-01-01\"     } } ```  To fetch the next page of sorted results, append `last_index=230880619` and `last_contribution_receipt_date=2014-01-01` to the URL. We strongly advise paging through these results using sort indices. The default sort is ascending by `contribution_receipt_date`. If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​`/schedules​/schedule_a​/` may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  ​The `/schedules​/schedule_a​/{sub_id}​/` endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
last_contributor_aggregate_ytd = 3.4 # float | When sorting by `contributor_aggregate_ytd`, this is populated with the         `contributor_aggregate_ytd` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional)
contributor_state = ['contributor_state_example'] # list[str] | State of contributor (optional)
contributor_occupation = ['contributor_occupation_example'] # list[str] | Occupation of contributor, filers need to make an effort to gather this information (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_date = '2013-10-20' # date | Minimum date (optional)
contributor_employer = ['contributor_employer_example'] # list[str] | Employer of contributor, filers need to make an effort to gather this information (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
last_contribution_receipt_amount = 3.4 # float | When sorting by `contribution_receipt_amount`, this is populated with the         `contribution_receipt_amount` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional)
contributor_name = ['contributor_name_example'] # list[str] | Name of contributor (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
contributor_city = ['contributor_city_example'] # list[str] | City of contributor (optional)
contributor_zip = ['contributor_zip_example'] # list[str] | Zip code of contributor (optional)
sort = 'contribution_receipt_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to contribution_receipt_date)
recipient_committee_designation = ['recipient_committee_designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
last_index = 56 # int | Index of last result from previous page (optional)
two_year_transaction_period = [56] # list[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
last_contribution_receipt_date = 'null' # date | When sorting by `contribution_receipt_date`, this is populated with the         `contribution_receipt_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional) (default to null)
contributor_type = ['contributor_type_example'] # list[str] | Filters individual or committee contributions based on line number (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
is_individual = null # bool | Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. (optional) (default to null)
recipient_committee_type = ['recipient_committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
contributor_id = ['contributor_id_example'] # list[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
recipient_committee_org_type = ['recipient_committee_org_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
max_image_number = 'max_image_number_example' # str |  (optional)

try:
    api_response = api_instance.schedules_schedule_a_get(api_key, sort_null_only=sort_null_only, last_contributor_aggregate_ytd=last_contributor_aggregate_ytd, contributor_state=contributor_state, contributor_occupation=contributor_occupation, line_number=line_number, sort_hide_null=sort_hide_null, min_date=min_date, contributor_employer=contributor_employer, committee_id=committee_id, last_contribution_receipt_amount=last_contribution_receipt_amount, contributor_name=contributor_name, max_date=max_date, contributor_city=contributor_city, contributor_zip=contributor_zip, sort=sort, recipient_committee_designation=recipient_committee_designation, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, last_contribution_receipt_date=last_contribution_receipt_date, contributor_type=contributor_type, max_amount=max_amount, is_individual=is_individual, recipient_committee_type=recipient_committee_type, min_amount=min_amount, min_image_number=min_image_number, contributor_id=contributor_id, per_page=per_page, recipient_committee_org_type=recipient_committee_org_type, max_image_number=max_image_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **last_contributor_aggregate_ytd** | **float**| When sorting by &#x60;contributor_aggregate_ytd&#x60;, this is populated with the         &#x60;contributor_aggregate_ytd&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **contributor_state** | [**list[str]**](str.md)| State of contributor | [optional] 
 **contributor_occupation** | [**list[str]**](str.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] 
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_date** | **date**| Minimum date | [optional] 
 **contributor_employer** | [**list[str]**](str.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **last_contribution_receipt_amount** | **float**| When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **contributor_name** | [**list[str]**](str.md)| Name of contributor | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **contributor_city** | [**list[str]**](str.md)| City of contributor | [optional] 
 **contributor_zip** | [**list[str]**](str.md)| Zip code of contributor | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to contribution_receipt_date]
 **recipient_committee_designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **two_year_transaction_period** | [**list[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **last_contribution_receipt_date** | **date**| When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to null]
 **contributor_type** | [**list[str]**](str.md)| Filters individual or committee contributions based on line number | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **is_individual** | **bool**| Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. | [optional] [default to null]
 **recipient_committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **contributor_id** | [**list[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **recipient_committee_org_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **max_image_number** | **str**|  | [optional] 

### Return type

[**ScheduleAPage**](ScheduleAPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_a_sub_id_get**
> ScheduleAPage schedules_schedule_a_sub_id_get(api_key, sub_id, sort_null_only=sort_null_only, last_contributor_aggregate_ytd=last_contributor_aggregate_ytd, contributor_state=contributor_state, contributor_occupation=contributor_occupation, line_number=line_number, sort_hide_null=sort_hide_null, min_date=min_date, contributor_employer=contributor_employer, committee_id=committee_id, last_contribution_receipt_amount=last_contribution_receipt_amount, contributor_name=contributor_name, max_date=max_date, contributor_city=contributor_city, contributor_zip=contributor_zip, sort=sort, recipient_committee_designation=recipient_committee_designation, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, last_contribution_receipt_date=last_contribution_receipt_date, contributor_type=contributor_type, max_amount=max_amount, is_individual=is_individual, recipient_committee_type=recipient_committee_type, min_amount=min_amount, min_image_number=min_image_number, contributor_id=contributor_id, per_page=per_page, recipient_committee_org_type=recipient_committee_org_type, max_image_number=max_image_number)



 This description is for both ​`/schedules​/schedule_a​/` and ​ `/schedules​/schedule_a​/{sub_id}​/`.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the `/schedules/schedule_a/` endpoint. For a more complete description of all Schedule A records see the [receipts section] (https://www.fec.gov/campaign-finance-data/ about-campaign-finance-data/about-receipts-data/) of our “about the data” page. If you are interested in our “is_individual” methodology see the [methodology section] (https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/) of our “about the data” page.  ​The `/schedules​/schedule_a​/` endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the `last_indexes` object from pagination to the URL of your last request as additional parameters. For example, when sorting by `contribution_receipt_date`, you might receive a page of results with the following pagination information:  ``` pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \"230880619\",         last_contribution_receipt_date: \"2014-01-01\"     } } ```  To fetch the next page of sorted results, append `last_index=230880619` and `last_contribution_receipt_date=2014-01-01` to the URL. We strongly advise paging through these results using sort indices. The default sort is ascending by `contribution_receipt_date`. If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​`/schedules​/schedule_a​/` may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  ​The `/schedules​/schedule_a​/{sub_id}​/` endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

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
api_instance = swagger_client.ReceiptsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sub_id = 'sub_id_example' # str | 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
last_contributor_aggregate_ytd = 3.4 # float | When sorting by `contributor_aggregate_ytd`, this is populated with the         `contributor_aggregate_ytd` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional)
contributor_state = ['contributor_state_example'] # list[str] | State of contributor (optional)
contributor_occupation = ['contributor_occupation_example'] # list[str] | Occupation of contributor, filers need to make an effort to gather this information (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_date = '2013-10-20' # date | Minimum date (optional)
contributor_employer = ['contributor_employer_example'] # list[str] | Employer of contributor, filers need to make an effort to gather this information (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
last_contribution_receipt_amount = 3.4 # float | When sorting by `contribution_receipt_amount`, this is populated with the         `contribution_receipt_amount` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional)
contributor_name = ['contributor_name_example'] # list[str] | Name of contributor (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
contributor_city = ['contributor_city_example'] # list[str] | City of contributor (optional)
contributor_zip = ['contributor_zip_example'] # list[str] | Zip code of contributor (optional)
sort = 'contribution_receipt_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to contribution_receipt_date)
recipient_committee_designation = ['recipient_committee_designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
last_index = 56 # int | Index of last result from previous page (optional)
two_year_transaction_period = [56] # list[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
last_contribution_receipt_date = 'null' # date | When sorting by `contribution_receipt_date`, this is populated with the         `contribution_receipt_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional) (default to null)
contributor_type = ['contributor_type_example'] # list[str] | Filters individual or committee contributions based on line number (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
is_individual = null # bool | Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. (optional) (default to null)
recipient_committee_type = ['recipient_committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
contributor_id = ['contributor_id_example'] # list[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
recipient_committee_org_type = ['recipient_committee_org_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
max_image_number = 'max_image_number_example' # str |  (optional)

try:
    api_response = api_instance.schedules_schedule_a_sub_id_get(api_key, sub_id, sort_null_only=sort_null_only, last_contributor_aggregate_ytd=last_contributor_aggregate_ytd, contributor_state=contributor_state, contributor_occupation=contributor_occupation, line_number=line_number, sort_hide_null=sort_hide_null, min_date=min_date, contributor_employer=contributor_employer, committee_id=committee_id, last_contribution_receipt_amount=last_contribution_receipt_amount, contributor_name=contributor_name, max_date=max_date, contributor_city=contributor_city, contributor_zip=contributor_zip, sort=sort, recipient_committee_designation=recipient_committee_designation, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, last_contribution_receipt_date=last_contribution_receipt_date, contributor_type=contributor_type, max_amount=max_amount, is_individual=is_individual, recipient_committee_type=recipient_committee_type, min_amount=min_amount, min_image_number=min_image_number, contributor_id=contributor_id, per_page=per_page, recipient_committee_org_type=recipient_committee_org_type, max_image_number=max_image_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->schedules_schedule_a_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sub_id** | **str**|  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **last_contributor_aggregate_ytd** | **float**| When sorting by &#x60;contributor_aggregate_ytd&#x60;, this is populated with the         &#x60;contributor_aggregate_ytd&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **contributor_state** | [**list[str]**](str.md)| State of contributor | [optional] 
 **contributor_occupation** | [**list[str]**](str.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] 
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_date** | **date**| Minimum date | [optional] 
 **contributor_employer** | [**list[str]**](str.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **last_contribution_receipt_amount** | **float**| When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **contributor_name** | [**list[str]**](str.md)| Name of contributor | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **contributor_city** | [**list[str]**](str.md)| City of contributor | [optional] 
 **contributor_zip** | [**list[str]**](str.md)| Zip code of contributor | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to contribution_receipt_date]
 **recipient_committee_designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **two_year_transaction_period** | [**list[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **last_contribution_receipt_date** | **date**| When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to null]
 **contributor_type** | [**list[str]**](str.md)| Filters individual or committee contributions based on line number | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **is_individual** | **bool**| Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. | [optional] [default to null]
 **recipient_committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **contributor_id** | [**list[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **recipient_committee_org_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **max_image_number** | **str**|  | [optional] 

### Return type

[**ScheduleAPage**](ScheduleAPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

