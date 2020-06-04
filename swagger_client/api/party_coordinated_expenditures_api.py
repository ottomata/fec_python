# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PartyCoordinatedExpendituresApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def schedules_schedule_f_get(self, api_key, **kwargs):  # noqa: E501
        """schedules_schedule_f_get  # noqa: E501

         Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_f_get(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param bool sort_null_only: Toggle that filters out all rows having sort column that is non-null
        :param bool sort_hide_null: Hide null values on sorted column(s).
        :param str line_number: Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
        :param list[str] payee_name:
        :param list[str] committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
        :param date max_date: Maximum date
        :param bool sort_nulls_last: Toggle that sorts null values last
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param int page: For paginating through results, starting at page 1
        :param str sort: Provide a field to sort by. Use - for descending order.
        :param list[str] image_number: The image number of the page where the schedule item is reported
        :param str max_amount: Filter for all amounts less than a value.
        :param str min_amount: Filter for all amounts greater than a value.
        :param str min_image_number:
        :param date min_date: Minimum date
        :param list[int] cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
        :param list[str] candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
        :param str max_image_number:
        :return: InlineResponseDefault5
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_schedule_f_get_with_http_info(api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_schedule_f_get_with_http_info(api_key, **kwargs)  # noqa: E501
            return data

    def schedules_schedule_f_get_with_http_info(self, api_key, **kwargs):  # noqa: E501
        """schedules_schedule_f_get  # noqa: E501

         Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_f_get_with_http_info(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param bool sort_null_only: Toggle that filters out all rows having sort column that is non-null
        :param bool sort_hide_null: Hide null values on sorted column(s).
        :param str line_number: Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
        :param list[str] payee_name:
        :param list[str] committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
        :param date max_date: Maximum date
        :param bool sort_nulls_last: Toggle that sorts null values last
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param int page: For paginating through results, starting at page 1
        :param str sort: Provide a field to sort by. Use - for descending order.
        :param list[str] image_number: The image number of the page where the schedule item is reported
        :param str max_amount: Filter for all amounts less than a value.
        :param str min_amount: Filter for all amounts greater than a value.
        :param str min_image_number:
        :param date min_date: Minimum date
        :param list[int] cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
        :param list[str] candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
        :param str max_image_number:
        :return: InlineResponseDefault5
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'sort_null_only', 'sort_hide_null', 'line_number', 'payee_name', 'committee_id', 'max_date', 'sort_nulls_last', 'per_page', 'page', 'sort', 'image_number', 'max_amount', 'min_amount', 'min_image_number', 'min_date', 'cycle', 'candidate_id', 'max_image_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_schedule_f_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `schedules_schedule_f_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_null_only' in params:
            query_params.append(('sort_null_only', params['sort_null_only']))  # noqa: E501
        if 'sort_hide_null' in params:
            query_params.append(('sort_hide_null', params['sort_hide_null']))  # noqa: E501
        if 'line_number' in params:
            query_params.append(('line_number', params['line_number']))  # noqa: E501
        if 'payee_name' in params:
            query_params.append(('payee_name', params['payee_name']))  # noqa: E501
            collection_formats['payee_name'] = 'multi'  # noqa: E501
        if 'committee_id' in params:
            query_params.append(('committee_id', params['committee_id']))  # noqa: E501
            collection_formats['committee_id'] = 'multi'  # noqa: E501
        if 'max_date' in params:
            query_params.append(('max_date', params['max_date']))  # noqa: E501
        if 'sort_nulls_last' in params:
            query_params.append(('sort_nulls_last', params['sort_nulls_last']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'image_number' in params:
            query_params.append(('image_number', params['image_number']))  # noqa: E501
            collection_formats['image_number'] = 'multi'  # noqa: E501
        if 'max_amount' in params:
            query_params.append(('max_amount', params['max_amount']))  # noqa: E501
        if 'min_amount' in params:
            query_params.append(('min_amount', params['min_amount']))  # noqa: E501
        if 'min_image_number' in params:
            query_params.append(('min_image_number', params['min_image_number']))  # noqa: E501
        if 'min_date' in params:
            query_params.append(('min_date', params['min_date']))  # noqa: E501
        if 'cycle' in params:
            query_params.append(('cycle', params['cycle']))  # noqa: E501
            collection_formats['cycle'] = 'multi'  # noqa: E501
        if 'candidate_id' in params:
            query_params.append(('candidate_id', params['candidate_id']))  # noqa: E501
            collection_formats['candidate_id'] = 'multi'  # noqa: E501
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501
        if 'max_image_number' in params:
            query_params.append(('max_image_number', params['max_image_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/schedules/schedule_f/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault5',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_schedule_f_sub_id_get(self, api_key, sub_id, **kwargs):  # noqa: E501
        """schedules_schedule_f_sub_id_get  # noqa: E501

         Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_f_sub_id_get(api_key, sub_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param str sub_id: (required)
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param int page: For paginating through results, starting at page 1
        :return: InlineResponseDefault5
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_schedule_f_sub_id_get_with_http_info(api_key, sub_id, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_schedule_f_sub_id_get_with_http_info(api_key, sub_id, **kwargs)  # noqa: E501
            return data

    def schedules_schedule_f_sub_id_get_with_http_info(self, api_key, sub_id, **kwargs):  # noqa: E501
        """schedules_schedule_f_sub_id_get  # noqa: E501

         Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_f_sub_id_get_with_http_info(api_key, sub_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param str sub_id: (required)
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param int page: For paginating through results, starting at page 1
        :return: InlineResponseDefault5
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'sub_id', 'per_page', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_schedule_f_sub_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `schedules_schedule_f_sub_id_get`")  # noqa: E501
        # verify the required parameter 'sub_id' is set
        if ('sub_id' not in params or
                params['sub_id'] is None):
            raise ValueError("Missing the required parameter `sub_id` when calling `schedules_schedule_f_sub_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sub_id' in params:
            path_params['sub_id'] = params['sub_id']  # noqa: E501

        query_params = []
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/schedules/schedule_f/{sub_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault5',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
