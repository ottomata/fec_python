# swagger_client.PresidentialApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**presidential_contributions_by_candidate_get**](PresidentialApi.md#presidential_contributions_by_candidate_get) | **GET** /presidential/contributions/by_candidate/ | 
[**presidential_contributions_by_size_get**](PresidentialApi.md#presidential_contributions_by_size_get) | **GET** /presidential/contributions/by_size/ | 
[**presidential_contributions_by_state_get**](PresidentialApi.md#presidential_contributions_by_state_get) | **GET** /presidential/contributions/by_state/ | 
[**presidential_coverage_end_date_get**](PresidentialApi.md#presidential_coverage_end_date_get) | **GET** /presidential/coverage_end_date/ | 
[**presidential_financial_summary_get**](PresidentialApi.md#presidential_financial_summary_get) | **GET** /presidential/financial_summary/ | 


# **presidential_contributions_by_candidate_get**
> PresidentialByCandidatePage presidential_contributions_by_candidate_get(api_key, sort_null_only=sort_null_only, contributor_state=contributor_state, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last)



 Net receipts per candidate.  Filter with `contributor_state='US'` for national totals 

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
api_instance = swagger_client.PresidentialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
contributor_state = ['contributor_state_example'] # list[str] | State of contributor (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-net_receipts' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -net_receipts)
election_year = [56] # list[int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.presidential_contributions_by_candidate_get(api_key, sort_null_only=sort_null_only, contributor_state=contributor_state, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresidentialApi->presidential_contributions_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **contributor_state** | [**list[str]**](str.md)| State of contributor | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -net_receipts]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**PresidentialByCandidatePage**](PresidentialByCandidatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **presidential_contributions_by_size_get**
> PresidentialBySizePage presidential_contributions_by_size_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_year=election_year, size=size, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)



 Contribution receipts by size per candidate.  Filter by candidate_id, election_year and/or size 

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
api_instance = swagger_client.PresidentialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'size' # str | Provide a field to sort by. Use - for descending order. (optional) (default to size)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
election_year = [56] # list[int] | Year of election (optional)
size = [56] # list[int] |  The total all contributions in the following ranges: ```   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + ``` Unitemized contributions are included in the `0` category.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  (optional)

try:
    api_response = api_instance.presidential_contributions_by_size_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, election_year=election_year, size=size, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresidentialApi->presidential_contributions_by_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to size]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 
 **size** | [**list[int]**](int.md)|  The total all contributions in the following ranges: &#x60;&#x60;&#x60;   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + &#x60;&#x60;&#x60; Unitemized contributions are included in the &#x60;0&#x60; category.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  | [optional] 

### Return type

[**PresidentialBySizePage**](PresidentialBySizePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **presidential_contributions_by_state_get**
> PresidentialByStatePage presidential_contributions_by_state_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)



 Contribution receipts by state per candidate.  Filter by candidate_id and/or election_year 

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
api_instance = swagger_client.PresidentialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-contribution_receipt_amount' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -contribution_receipt_amount)
election_year = [56] # list[int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  (optional)

try:
    api_response = api_instance.presidential_contributions_by_state_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresidentialApi->presidential_contributions_by_state_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -contribution_receipt_amount]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  | [optional] 

### Return type

[**PresidentialByStatePage**](PresidentialByStatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **presidential_coverage_end_date_get**
> PresidentialCoveragePage presidential_coverage_end_date_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)



 Coverage end date per candidate.  Filter by candidate_id and/or election_year 

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
api_instance = swagger_client.PresidentialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'candidate_id' # str | Provide a field to sort by. Use - for descending order. (optional) (default to candidate_id)
election_year = [56] # list[int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  (optional)

try:
    api_response = api_instance.presidential_coverage_end_date_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresidentialApi->presidential_coverage_end_date_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to candidate_id]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  | [optional] 

### Return type

[**PresidentialCoveragePage**](PresidentialCoveragePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **presidential_financial_summary_get**
> PresidentialSummaryPage presidential_financial_summary_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)



 Financial summary per candidate.  Filter by candidate_id and/or election_year 

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
api_instance = swagger_client.PresidentialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-net_receipts' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -net_receipts)
election_year = [56] # list[int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  (optional)

try:
    api_response = api_instance.presidential_financial_summary_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_year=election_year, per_page=per_page, sort_nulls_last=sort_nulls_last, candidate_id=candidate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresidentialApi->presidential_financial_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -net_receipts]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  | [optional] 

### Return type

[**PresidentialSummaryPage**](PresidentialSummaryPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

