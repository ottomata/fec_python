# swagger_client.SearchApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**names_candidates_get**](SearchApi.md#names_candidates_get) | **GET** /names/candidates/ | 
[**names_committees_get**](SearchApi.md#names_committees_get) | **GET** /names/committees/ | 


# **names_candidates_get**
> CandidateSearchList names_candidates_get(api_key, q)



 Search for candidates or committees by name. If you're looking for information on a particular person or group, using a name to find the `candidate_id` or `committee_id` on this endpoint can be a helpful first step. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
q = ['q_example'] # list[str] | Name (candidate or committee) to search for

try:
    api_response = api_instance.names_candidates_get(api_key, q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->names_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **q** | [**list[str]**](str.md)| Name (candidate or committee) to search for | 

### Return type

[**CandidateSearchList**](CandidateSearchList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **names_committees_get**
> CommitteeSearchList names_committees_get(api_key, q)



 Search for candidates or committees by name. If you're looking for information on a particular person or group, using a name to find the `candidate_id` or `committee_id` on this endpoint can be a helpful first step. 

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
q = ['q_example'] # list[str] | Name (candidate or committee) to search for

try:
    api_response = api_instance.names_committees_get(api_key, q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->names_committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **q** | [**list[str]**](str.md)| Name (candidate or committee) to search for | 

### Return type

[**CommitteeSearchList**](CommitteeSearchList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

