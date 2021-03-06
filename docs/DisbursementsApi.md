# swagger_client.DisbursementsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_b_by_purpose_get**](DisbursementsApi.md#schedules_schedule_b_by_purpose_get) | **GET** /schedules/schedule_b/by_purpose/ | 
[**schedules_schedule_b_by_recipient_get**](DisbursementsApi.md#schedules_schedule_b_by_recipient_get) | **GET** /schedules/schedule_b/by_recipient/ | 
[**schedules_schedule_b_by_recipient_id_get**](DisbursementsApi.md#schedules_schedule_b_by_recipient_id_get) | **GET** /schedules/schedule_b/by_recipient_id/ | 
[**schedules_schedule_b_efile_get**](DisbursementsApi.md#schedules_schedule_b_efile_get) | **GET** /schedules/schedule_b/efile/ | 
[**schedules_schedule_b_get**](DisbursementsApi.md#schedules_schedule_b_get) | **GET** /schedules/schedule_b/ | 
[**schedules_schedule_b_sub_id_get**](DisbursementsApi.md#schedules_schedule_b_sub_id_get) | **GET** /schedules/schedule_b/{sub_id}/ | 


# **schedules_schedule_b_by_purpose_get**
> ScheduleBByPurposePage schedules_schedule_b_by_purpose_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, per_page=per_page, purpose=purpose, cycle=cycle, sort_nulls_last=sort_nulls_last)



 Schedule B disbursements aggregated by disbursement purpose category. To avoid double counting, memoed items are not included. Purpose is a combination of transaction codes, category codes and disbursement description. See the `disbursement_purpose` sql function within the migrations for more details. 

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
api_instance = swagger_client.DisbursementsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
purpose = ['purpose_example'] # list[str] | Disbursement purpose category (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.schedules_schedule_b_by_purpose_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, per_page=per_page, purpose=purpose, cycle=cycle, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_by_purpose_get: %s\n" % e)
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
 **purpose** | [**list[str]**](str.md)| Disbursement purpose category | [optional] 
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**ScheduleBByPurposePage**](ScheduleBByPurposePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_b_by_recipient_get**
> ScheduleBByRecipientPage schedules_schedule_b_by_recipient_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, recipient_name=recipient_name, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)



 Schedule B disbursements aggregated by recipient name. To avoid double counting, memoed items are not included. 

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
api_instance = swagger_client.DisbursementsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
recipient_name = ['recipient_name_example'] # list[str] | Name of the entity receiving the disbursement (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.schedules_schedule_b_by_recipient_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, committee_id=committee_id, recipient_name=recipient_name, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_by_recipient_get: %s\n" % e)
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
 **recipient_name** | [**list[str]**](str.md)| Name of the entity receiving the disbursement | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**ScheduleBByRecipientPage**](ScheduleBByRecipientPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_b_by_recipient_id_get**
> ScheduleBByRecipientIDPage schedules_schedule_b_by_recipient_id_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, recipient_id=recipient_id, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)



 Schedule B disbursements aggregated by recipient committee ID, if applicable. To avoid double counting, memoed items are not included. 

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
api_instance = swagger_client.DisbursementsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = 'null' # str | Provide a field to sort by. Use - for descending order. (optional) (default to null)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
recipient_id = ['recipient_id_example'] # list[str] | The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.schedules_schedule_b_by_recipient_id_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, sort=sort, page=page, recipient_id=recipient_id, committee_id=committee_id, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_by_recipient_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to null]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **recipient_id** | [**list[str]**](str.md)| The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**ScheduleBByRecipientIDPage**](ScheduleBByRecipientIDPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_b_efile_get**
> ScheduleBEfilePage schedules_schedule_b_efile_get(api_key, sort_null_only=sort_null_only, per_page=per_page, sort_hide_null=sort_hide_null, sort=sort, page=page, image_number=image_number, recipient_city=recipient_city, committee_id=committee_id, max_amount=max_amount, min_amount=min_amount, min_date=min_date, max_date=max_date, recipient_state=recipient_state, sort_nulls_last=sort_nulls_last, disbursement_description=disbursement_description)



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
api_instance = swagger_client.DisbursementsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = '-disbursement_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -disbursement_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
recipient_city = ['recipient_city_example'] # list[str] | City of recipient (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts less than a value. (optional)
min_date = 'null' # date | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional) (default to null)
max_date = 'null' # date | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional) (default to null)
recipient_state = ['recipient_state_example'] # list[str] | State of recipient (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
disbursement_description = ['disbursement_description_example'] # list[str] | Description of disbursement (optional)

try:
    api_response = api_instance.schedules_schedule_b_efile_get(api_key, sort_null_only=sort_null_only, per_page=per_page, sort_hide_null=sort_hide_null, sort=sort, page=page, image_number=image_number, recipient_city=recipient_city, committee_id=committee_id, max_amount=max_amount, min_amount=min_amount, min_date=min_date, max_date=max_date, recipient_state=recipient_state, sort_nulls_last=sort_nulls_last, disbursement_description=disbursement_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_efile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -disbursement_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **recipient_city** | [**list[str]**](str.md)| City of recipient | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_date** | **date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to null]
 **max_date** | **date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to null]
 **recipient_state** | [**list[str]**](str.md)| State of recipient | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **disbursement_description** | [**list[str]**](str.md)| Description of disbursement | [optional] 

### Return type

[**ScheduleBEfilePage**](ScheduleBEfilePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_b_get**
> ScheduleBPage schedules_schedule_b_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, max_image_number=max_image_number, spender_committee_type=spender_committee_type, committee_id=committee_id, recipient_committee_id=recipient_committee_id, max_date=max_date, recipient_state=recipient_state, last_disbursement_date=last_disbursement_date, spender_committee_designation=spender_committee_designation, last_disbursement_amount=last_disbursement_amount, sort=sort, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, max_amount=max_amount, min_amount=min_amount, recipient_name=recipient_name, spender_committee_org_type=spender_committee_org_type, min_image_number=min_image_number, per_page=per_page, recipient_city=recipient_city, disbursement_purpose_category=disbursement_purpose_category, disbursement_description=disbursement_description)



 Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called `two_year_transaction_period`, which is derived from the `report_year` submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the `last_indexes` object from `pagination` to the URL of your last request. For example, when sorting by `disbursement_date`, you might receive a page of results with the following pagination information:  ``` pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \"230906248\",         last_disbursement_date: \"2014-07-04\"     } } ```  To fetch the next page of sorted results, append `last_index=230906248` and `last_disbursement_date=2014-07-04` to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. `last_disbursement_date`), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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
api_instance = swagger_client.DisbursementsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_date = '2013-10-20' # date | Minimum date (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
max_image_number = 'max_image_number_example' # str |  (optional)
spender_committee_type = ['spender_committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
recipient_committee_id = ['recipient_committee_id_example'] # list[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
recipient_state = ['recipient_state_example'] # list[str] | State of recipient (optional)
last_disbursement_date = 'null' # date | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. (optional) (default to null)
spender_committee_designation = ['spender_committee_designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
last_disbursement_amount = 3.4 # float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
sort = '-disbursement_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -disbursement_date)
last_index = 56 # int | Index of last result from previous page (optional)
two_year_transaction_period = [56] # list[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
recipient_name = ['recipient_name_example'] # list[str] | Name of the entity receiving the disbursement (optional)
spender_committee_org_type = ['spender_committee_org_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
recipient_city = ['recipient_city_example'] # list[str] | City of recipient (optional)
disbursement_purpose_category = ['disbursement_purpose_category_example'] # list[str] | Disbursement purpose category (optional)
disbursement_description = ['disbursement_description_example'] # list[str] | Description of disbursement (optional)

try:
    api_response = api_instance.schedules_schedule_b_get(api_key, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, max_image_number=max_image_number, spender_committee_type=spender_committee_type, committee_id=committee_id, recipient_committee_id=recipient_committee_id, max_date=max_date, recipient_state=recipient_state, last_disbursement_date=last_disbursement_date, spender_committee_designation=spender_committee_designation, last_disbursement_amount=last_disbursement_amount, sort=sort, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, max_amount=max_amount, min_amount=min_amount, recipient_name=recipient_name, spender_committee_org_type=spender_committee_org_type, min_image_number=min_image_number, per_page=per_page, recipient_city=recipient_city, disbursement_purpose_category=disbursement_purpose_category, disbursement_description=disbursement_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_date** | **date**| Minimum date | [optional] 
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **max_image_number** | **str**|  | [optional] 
 **spender_committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **recipient_committee_id** | [**list[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **recipient_state** | [**list[str]**](str.md)| State of recipient | [optional] 
 **last_disbursement_date** | **date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to null]
 **spender_committee_designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **last_disbursement_amount** | **float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -disbursement_date]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **two_year_transaction_period** | [**list[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **recipient_name** | [**list[str]**](str.md)| Name of the entity receiving the disbursement | [optional] 
 **spender_committee_org_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **recipient_city** | [**list[str]**](str.md)| City of recipient | [optional] 
 **disbursement_purpose_category** | [**list[str]**](str.md)| Disbursement purpose category | [optional] 
 **disbursement_description** | [**list[str]**](str.md)| Description of disbursement | [optional] 

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_b_sub_id_get**
> ScheduleBPage schedules_schedule_b_sub_id_get(api_key, sub_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, max_image_number=max_image_number, spender_committee_type=spender_committee_type, committee_id=committee_id, recipient_committee_id=recipient_committee_id, max_date=max_date, recipient_state=recipient_state, last_disbursement_date=last_disbursement_date, spender_committee_designation=spender_committee_designation, last_disbursement_amount=last_disbursement_amount, sort=sort, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, max_amount=max_amount, min_amount=min_amount, recipient_name=recipient_name, spender_committee_org_type=spender_committee_org_type, min_image_number=min_image_number, per_page=per_page, recipient_city=recipient_city, disbursement_purpose_category=disbursement_purpose_category, disbursement_description=disbursement_description)



 Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called `two_year_transaction_period`, which is derived from the `report_year` submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the `last_indexes` object from `pagination` to the URL of your last request. For example, when sorting by `disbursement_date`, you might receive a page of results with the following pagination information:  ``` pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \"230906248\",         last_disbursement_date: \"2014-07-04\"     } } ```  To fetch the next page of sorted results, append `last_index=230906248` and `last_disbursement_date=2014-07-04` to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. `last_disbursement_date`), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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
api_instance = swagger_client.DisbursementsApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sub_id = 'sub_id_example' # str | 
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_date = '2013-10-20' # date | Minimum date (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
max_image_number = 'max_image_number_example' # str |  (optional)
spender_committee_type = ['spender_committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
recipient_committee_id = ['recipient_committee_id_example'] # list[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
recipient_state = ['recipient_state_example'] # list[str] | State of recipient (optional)
last_disbursement_date = 'null' # date | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. (optional) (default to null)
spender_committee_designation = ['spender_committee_designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
last_disbursement_amount = 3.4 # float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
sort = '-disbursement_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -disbursement_date)
last_index = 56 # int | Index of last result from previous page (optional)
two_year_transaction_period = [56] # list[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
recipient_name = ['recipient_name_example'] # list[str] | Name of the entity receiving the disbursement (optional)
spender_committee_org_type = ['spender_committee_org_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
recipient_city = ['recipient_city_example'] # list[str] | City of recipient (optional)
disbursement_purpose_category = ['disbursement_purpose_category_example'] # list[str] | Disbursement purpose category (optional)
disbursement_description = ['disbursement_description_example'] # list[str] | Description of disbursement (optional)

try:
    api_response = api_instance.schedules_schedule_b_sub_id_get(api_key, sub_id, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, max_image_number=max_image_number, spender_committee_type=spender_committee_type, committee_id=committee_id, recipient_committee_id=recipient_committee_id, max_date=max_date, recipient_state=recipient_state, last_disbursement_date=last_disbursement_date, spender_committee_designation=spender_committee_designation, last_disbursement_amount=last_disbursement_amount, sort=sort, last_index=last_index, two_year_transaction_period=two_year_transaction_period, image_number=image_number, max_amount=max_amount, min_amount=min_amount, recipient_name=recipient_name, spender_committee_org_type=spender_committee_org_type, min_image_number=min_image_number, per_page=per_page, recipient_city=recipient_city, disbursement_purpose_category=disbursement_purpose_category, disbursement_description=disbursement_description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sub_id** | **str**|  | 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_date** | **date**| Minimum date | [optional] 
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **max_image_number** | **str**|  | [optional] 
 **spender_committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **recipient_committee_id** | [**list[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **max_date** | **date**| Maximum date | [optional] 
 **recipient_state** | [**list[str]**](str.md)| State of recipient | [optional] 
 **last_disbursement_date** | **date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to null]
 **spender_committee_designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **last_disbursement_amount** | **float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -disbursement_date]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **two_year_transaction_period** | [**list[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional] 
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional] 
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional] 
 **recipient_name** | [**list[str]**](str.md)| Name of the entity receiving the disbursement | [optional] 
 **spender_committee_org_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **recipient_city** | [**list[str]**](str.md)| City of recipient | [optional] 
 **disbursement_purpose_category** | [**list[str]**](str.md)| Disbursement purpose category | [optional] 
 **disbursement_description** | [**list[str]**](str.md)| Description of disbursement | [optional] 

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

