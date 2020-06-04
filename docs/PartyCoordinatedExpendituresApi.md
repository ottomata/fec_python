# swagger_client.PartyCoordinatedExpendituresApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_f_get**](PartyCoordinatedExpendituresApi.md#schedules_schedule_f_get) | **GET** /schedules/schedule_f/ | 
[**schedules_schedule_f_sub_id_get**](PartyCoordinatedExpendituresApi.md#schedules_schedule_f_sub_id_get) | **GET** /schedules/schedule_f/{sub_id}/ | 


# **schedules_schedule_f_get**
> InlineResponseDefault5 schedules_schedule_f_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, line_number=line_number, payee_name=payee_name, committee_id=committee_id, max_date=max_date, sort_nulls_last=sort_nulls_last, per_page=per_page, page=page, sort=sort, image_number=image_number, max_amount=max_amount, min_amount=min_amount, min_image_number=min_image_number, min_date=min_date, cycle=cycle, candidate_id=candidate_id, max_image_number=max_image_number)



 Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees. 

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
api_instance = swagger_client.PartyCoordinatedExpendituresApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
payee_name = ['payee_name_example'] # list[str] |  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'expenditure_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to expenditure_date)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
min_date = '2013-10-20' # date | Minimum date (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_image_number = 'max_image_number_example' # str |  (optional)

try:
    api_response = api_instance.schedules_schedule_f_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, line_number=line_number, payee_name=payee_name, committee_id=committee_id, max_date=max_date, sort_nulls_last=sort_nulls_last, per_page=per_page, page=page, sort=sort, image_number=image_number, max_amount=max_amount, min_amount=min_amount, min_image_number=min_image_number, min_date=min_date, cycle=cycle, candidate_id=candidate_id, max_image_number=max_image_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyCoordinatedExpendituresApi->schedules_schedule_f_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **payee_name** | [**list[str]**](str.md)|  | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to expenditure_date]
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **min_date** | **date**| Minimum date | [optional] 
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **max_image_number** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault5**](InlineResponseDefault5.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_f_sub_id_get**
> InlineResponseDefault5 schedules_schedule_f_sub_id_get(api_key, sub_id, per_page=per_page, page=page)



 Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees. 

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
api_instance = swagger_client.PartyCoordinatedExpendituresApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sub_id = 'sub_id_example' # str | 
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)

try:
    api_response = api_instance.schedules_schedule_f_sub_id_get(api_key, sub_id, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyCoordinatedExpendituresApi->schedules_schedule_f_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sub_id** | **str**|  | 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]

### Return type

[**InlineResponseDefault5**](InlineResponseDefault5.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

