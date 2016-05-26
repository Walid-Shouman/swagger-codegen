# coding: utf-8

"""
    Swagger Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\ 
    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class StoreApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_order(self, order_id, **kwargs):
        """
        Delete purchase order by ID
        For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_order(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str order_id: ID of the order that needs to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_order" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'order_id' is set
        if ('order_id' not in params) or (params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `delete_order`")

        if 'order_id' in params and params['order_id'] < 1.0: 
            raise ValueError("Invalid value for parameter `order_id` when calling `delete_order`, must be a value greater than or equal to `1.0`")

        resource_path = '/store/order/{orderId}'.replace('{format}', 'json')
        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_inventory(self, **kwargs):
        """
        Returns pet inventories by status
        Returns a map of status codes to quantities

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_inventory(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/store/inventory'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='dict(str, int)',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_order_by_id(self, order_id, **kwargs):
        """
        Find purchase order by ID
        For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_order_by_id(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int order_id: ID of pet that needs to be fetched (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'order_id' is set
        if ('order_id' not in params) or (params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_by_id`")

        if 'order_id' in params and params['order_id'] > 5.0: 
            raise ValueError("Invalid value for parameter `order_id` when calling `get_order_by_id`, must be a value less than or equal to  `5.0`")
        if 'order_id' in params and params['order_id'] < 1.0: 
            raise ValueError("Invalid value for parameter `order_id` when calling `get_order_by_id`, must be a value greater than or equal to `1.0`")

        resource_path = '/store/order/{orderId}'.replace('{format}', 'json')
        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Order',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def place_order(self, body, **kwargs):
        """
        Place an order for a pet
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.place_order(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Order body: order placed for purchasing the pet (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `place_order`")


        resource_path = '/store/order'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Order',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
