# swagger_client.CommitteeApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidate_candidate_id_committees_get**](CommitteeApi.md#candidate_candidate_id_committees_get) | **GET** /candidate/{candidate_id}/committees/ | 
[**candidate_candidate_id_committees_history_cycle_get**](CommitteeApi.md#candidate_candidate_id_committees_history_cycle_get) | **GET** /candidate/{candidate_id}/committees/history/{cycle}/ | 
[**candidate_candidate_id_committees_history_get**](CommitteeApi.md#candidate_candidate_id_committees_history_get) | **GET** /candidate/{candidate_id}/committees/history/ | 
[**committee_committee_id_get**](CommitteeApi.md#committee_committee_id_get) | **GET** /committee/{committee_id}/ | 
[**committee_committee_id_history_cycle_get**](CommitteeApi.md#committee_committee_id_history_cycle_get) | **GET** /committee/{committee_id}/history/{cycle}/ | 
[**committee_committee_id_history_get**](CommitteeApi.md#committee_committee_id_history_get) | **GET** /committee/{committee_id}/history/ | 
[**committees_get**](CommitteeApi.md#committees_get) | **GET** /committees/ | 


# **candidate_candidate_id_committees_get**
> CommitteeDetailPage candidate_candidate_id_committees_get(api_key, candidate_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_type=committee_type, filing_frequency=filing_frequency, organization_type=organization_type, per_page=per_page, year=year, cycle=cycle, designation=designation, sort_nulls_last=sort_nulls_last)



 This endpoint is useful for finding detailed information about a particular committee or filer. Use the `committee_id` to find the most recent information about the committee. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_type = ['committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
filing_frequency = ['filing_frequency_example'] # list[str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
organization_type = ['organization_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
year = [56] # list[int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
cycle = [56] # list[int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.candidate_candidate_id_committees_get(api_key, candidate_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_type=committee_type, filing_frequency=filing_frequency, organization_type=organization_type, per_page=per_page, year=year, cycle=cycle, designation=designation, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->candidate_candidate_id_committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **filing_frequency** | [**list[str]**](str.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **organization_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **year** | [**list[int]**](int.md)| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional] 
 **cycle** | [**list[int]**](int.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**CommitteeDetailPage**](CommitteeDetailPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidate_candidate_id_committees_history_cycle_get**
> CommitteeHistoryPage candidate_candidate_id_committees_history_cycle_get(api_key, cycle, candidate_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
cycle = 56 # int |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)

try:
    api_response = api_instance.candidate_candidate_id_committees_history_cycle_get(api_key, cycle, candidate_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **cycle** | **int**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidate_candidate_id_committees_history_get**
> CommitteeHistoryPage candidate_candidate_id_committees_history_get(api_key, candidate_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)

try:
    api_response = api_instance.candidate_candidate_id_committees_history_get(api_key, candidate_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_get**
> CommitteeDetailPage committee_committee_id_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_type=committee_type, filing_frequency=filing_frequency, organization_type=organization_type, per_page=per_page, year=year, cycle=cycle, designation=designation, sort_nulls_last=sort_nulls_last)



 This endpoint is useful for finding detailed information about a particular committee or filer. Use the `committee_id` to find the most recent information about the committee. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_type = ['committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
filing_frequency = ['filing_frequency_example'] # list[str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
organization_type = ['organization_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
year = [56] # list[int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
cycle = [56] # list[int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.committee_committee_id_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_type=committee_type, filing_frequency=filing_frequency, organization_type=organization_type, per_page=per_page, year=year, cycle=cycle, designation=designation, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committee_committee_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **filing_frequency** | [**list[str]**](str.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **organization_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **year** | [**list[int]**](int.md)| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional] 
 **cycle** | [**list[int]**](int.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**CommitteeDetailPage**](CommitteeDetailPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_history_cycle_get**
> CommitteeHistoryPage committee_committee_id_history_cycle_get(api_key, committee_id, cycle, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
cycle = 56 # int |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)

try:
    api_response = api_instance.committee_committee_id_history_cycle_get(api_key, committee_id, cycle, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committee_committee_id_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **cycle** | **int**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_history_get**
> CommitteeHistoryPage committee_committee_id_history_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)

try:
    api_response = api_instance.committee_committee_id_history_get(api_key, committee_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, election_full=election_full, per_page=per_page, sort_nulls_last=sort_nulls_last, designation=designation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committee_committee_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committees_get**
> CommitteePage committees_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, committee_type=committee_type, filing_frequency=filing_frequency, committee_id=committee_id, max_last_f1_date=max_last_f1_date, sort_nulls_last=sort_nulls_last, designation=designation, party=party, max_first_file_date=max_first_file_date, q=q, sort=sort, page=page, min_first_file_date=min_first_file_date, organization_type=organization_type, treasurer_name=treasurer_name, per_page=per_page, year=year, cycle=cycle, candidate_id=candidate_id, min_last_f1_date=min_last_f1_date)



 Fetch basic information about committees and filers. Use parameters to filter for particular characteristics.  

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
state = ['state_example'] # list[str] | US state or territory (optional)
committee_type = ['committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
filing_frequency = ['filing_frequency_example'] # list[str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_last_f1_date = '2013-10-20' # date | Filter for committees whose latest Form 1 was received on or before this date. (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
max_first_file_date = '2013-10-20' # date | Filter for committees whose first filing was received on or before this date. (optional)
q = ['q_example'] # list[str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_first_file_date = '2013-10-20' # date | Filter for committees whose first filing was received on or after this date. (optional)
organization_type = ['organization_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
treasurer_name = ['treasurer_name_example'] # list[str] | Name of the Committee's treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
year = [56] # list[int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
cycle = [56] # list[int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
min_last_f1_date = '2013-10-20' # date | Filter for committees whose latest Form 1 was received on or after this date. (optional)

try:
    api_response = api_instance.committees_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, state=state, committee_type=committee_type, filing_frequency=filing_frequency, committee_id=committee_id, max_last_f1_date=max_last_f1_date, sort_nulls_last=sort_nulls_last, designation=designation, party=party, max_first_file_date=max_first_file_date, q=q, sort=sort, page=page, min_first_file_date=min_first_file_date, organization_type=organization_type, treasurer_name=treasurer_name, per_page=per_page, year=year, cycle=cycle, candidate_id=candidate_id, min_last_f1_date=min_last_f1_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **state** | [**list[str]**](str.md)| US state or territory | [optional] 
 **committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **filing_frequency** | [**list[str]**](str.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_last_f1_date** | **date**| Filter for committees whose latest Form 1 was received on or before this date. | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **max_first_file_date** | **date**| Filter for committees whose first filing was received on or before this date. | [optional] 
 **q** | [**list[str]**](str.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_first_file_date** | **date**| Filter for committees whose first filing was received on or after this date. | [optional] 
 **organization_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **treasurer_name** | [**list[str]**](str.md)| Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **year** | [**list[int]**](int.md)| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional] 
 **cycle** | [**list[int]**](int.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **min_last_f1_date** | **date**| Filter for committees whose latest Form 1 was received on or after this date. | [optional] 

### Return type

[**CommitteePage**](CommitteePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

