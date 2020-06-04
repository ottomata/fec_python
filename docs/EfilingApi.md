# swagger_client.EfilingApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**efile_filings_get**](EfilingApi.md#efile_filings_get) | **GET** /efile/filings/ | 
[**efile_reports_house_senate_get**](EfilingApi.md#efile_reports_house_senate_get) | **GET** /efile/reports/house-senate/ | 
[**efile_reports_pac_party_get**](EfilingApi.md#efile_reports_pac_party_get) | **GET** /efile/reports/pac-party/ | 
[**efile_reports_presidential_get**](EfilingApi.md#efile_reports_presidential_get) | **GET** /efile/reports/presidential/ | 


# **efile_filings_get**
> EFilingsPage efile_filings_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)



Basic information about electronic files coming into the FEC, posted as they are received.

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
api_instance = swagger_client.EfilingApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = '-receipt_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -receipt_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.efile_filings_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EfilingApi->efile_filings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -receipt_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**EFilingsPage**](EFilingsPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efile_reports_house_senate_get**
> BaseF3FilingPage efile_reports_house_senate_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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
api_instance = swagger_client.EfilingApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = '-receipt_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -receipt_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.efile_reports_house_senate_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EfilingApi->efile_reports_house_senate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -receipt_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**BaseF3FilingPage**](BaseF3FilingPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efile_reports_pac_party_get**
> BaseF3XFilingPage efile_reports_pac_party_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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
api_instance = swagger_client.EfilingApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = '-receipt_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -receipt_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.efile_reports_pac_party_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EfilingApi->efile_reports_pac_party_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -receipt_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**BaseF3XFilingPage**](BaseF3XFilingPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efile_reports_presidential_get**
> BaseF3PFilingPage efile_reports_presidential_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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
api_instance = swagger_client.EfilingApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort = '-receipt_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -receipt_date)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)

try:
    api_response = api_instance.efile_reports_presidential_get(api_key, sort_null_only=sort_null_only, min_receipt_date=min_receipt_date, sort_hide_null=sort_hide_null, sort=sort, page=page, file_number=file_number, committee_id=committee_id, max_receipt_date=max_receipt_date, per_page=per_page, sort_nulls_last=sort_nulls_last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EfilingApi->efile_reports_presidential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -receipt_date]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**BaseF3PFilingPage**](BaseF3PFilingPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

