# swagger_client.FilerResourcesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rad_analyst_get**](FilerResourcesApi.md#rad_analyst_get) | **GET** /rad-analyst/ | 
[**state_election_office_get**](FilerResourcesApi.md#state_election_office_get) | **GET** /state-election-office/ | 


# **rad_analyst_get**
> RadAnalystPage rad_analyst_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, max_assignment_update_date=max_assignment_update_date, page=page, title=title, sort=sort, analyst_id=analyst_id, analyst_short_id=analyst_short_id, committee_id=committee_id, telephone_ext=telephone_ext, email=email, min_assignment_update_date=min_assignment_update_date, per_page=per_page, name=name, sort_nulls_last=sort_nulls_last)



 Use this endpoint to look up the RAD Analyst for a committee.  The mission of the Reports Analysis Division (RAD) is to ensure that campaigns and political committees file timely and accurate reports that fully disclose their financial activities.  RAD is responsible for reviewing statements and financial reports filed by political committees participating in federal elections, providing assistance and guidance to the committees to properly file their reports, and for taking appropriate action to ensure compliance with the Federal Election Campaign Act (FECA). 

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
api_instance = swagger_client.FilerResourcesApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
max_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made before this date (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
title = ['title_example'] # list[str] | Title of RAD analyst (optional)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
analyst_id = [56] # list[int] | ID of RAD analyst (optional)
analyst_short_id = [56] # list[int] | Short ID of RAD analyst (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
telephone_ext = [56] # list[int] | Telephone extension of RAD analyst (optional)
email = ['email_example'] # list[str] | Email of RAD analyst (optional)
min_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made after this date (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
name = ['name_example'] # list[str] | Name of RAD analyst (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.rad_analyst_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, max_assignment_update_date=max_assignment_update_date, page=page, title=title, sort=sort, analyst_id=analyst_id, analyst_short_id=analyst_short_id, committee_id=committee_id, telephone_ext=telephone_ext, email=email, min_assignment_update_date=min_assignment_update_date, per_page=per_page, name=name, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilerResourcesApi->rad_analyst_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **max_assignment_update_date** | **date**| Filter results for assignment updates made before this date | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **title** | [**list[str]**](str.md)| Title of RAD analyst | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **analyst_id** | [**list[int]**](int.md)| ID of RAD analyst | [optional] 
 **analyst_short_id** | [**list[int]**](int.md)| Short ID of RAD analyst | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **telephone_ext** | [**list[int]**](int.md)| Telephone extension of RAD analyst | [optional] 
 **email** | [**list[str]**](str.md)| Email of RAD analyst | [optional] 
 **min_assignment_update_date** | **date**| Filter results for assignment updates made after this date | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **name** | [**list[str]**](str.md)| Name of RAD analyst | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**RadAnalystPage**](RadAnalystPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_election_office_get**
> StateElectionOfficeInfoPage state_election_office_get(state, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, per_page=per_page, sort_nulls_last=sort_nulls_last)



 State laws and procedures govern elections for state or local offices as well as how candidates appear on election ballots. Contact the appropriate state election office for more information. 

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
api_instance = swagger_client.FilerResourcesApi(swagger_client.ApiClient(configuration))
state = 'state_example' # str |  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.  
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.state_election_office_get(state, api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, page=page, sort=sort, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilerResourcesApi->state_election_office_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.   | 
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**StateElectionOfficeInfoPage**](StateElectionOfficeInfoPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

