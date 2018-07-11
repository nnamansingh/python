# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class AuthorizationV1Api(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_namespaced_local_subject_access_review(self, namespace, body, **kwargs):
        """
        create a LocalSubjectAccessReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_namespaced_local_subject_access_review(namespace, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param V1LocalSubjectAccessReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1LocalSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_namespaced_local_subject_access_review_with_http_info(namespace, body, **kwargs)
        else:
            (data) = self.create_namespaced_local_subject_access_review_with_http_info(namespace, body, **kwargs)
            return data

    def create_namespaced_local_subject_access_review_with_http_info(self, namespace, body, **kwargs):
        """
        create a LocalSubjectAccessReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_namespaced_local_subject_access_review_with_http_info(namespace, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param V1LocalSubjectAccessReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1LocalSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'body', 'pretty']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_namespaced_local_subject_access_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `create_namespaced_local_subject_access_review`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_namespaced_local_subject_access_review`")


        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api('/apis/authorization.k8s.io/v1/namespaces/{namespace}/localsubjectaccessreviews', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='V1LocalSubjectAccessReview',
                                        auth_settings=auth_settings,
                                        async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_self_subject_access_review(self, body, **kwargs):
        """
        create a SelfSubjectAccessReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_self_subject_access_review(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SelfSubjectAccessReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_self_subject_access_review_with_http_info(body, **kwargs)
        else:
            (data) = self.create_self_subject_access_review_with_http_info(body, **kwargs)
            return data

    def create_self_subject_access_review_with_http_info(self, body, **kwargs):
        """
        create a SelfSubjectAccessReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_self_subject_access_review_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SelfSubjectAccessReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'pretty']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_self_subject_access_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_self_subject_access_review`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api('/apis/authorization.k8s.io/v1/selfsubjectaccessreviews', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='V1SelfSubjectAccessReview',
                                        auth_settings=auth_settings,
                                        async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_self_subject_rules_review(self, body, **kwargs):
        """
        create a SelfSubjectRulesReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_self_subject_rules_review(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SelfSubjectRulesReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectRulesReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_self_subject_rules_review_with_http_info(body, **kwargs)
        else:
            (data) = self.create_self_subject_rules_review_with_http_info(body, **kwargs)
            return data

    def create_self_subject_rules_review_with_http_info(self, body, **kwargs):
        """
        create a SelfSubjectRulesReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_self_subject_rules_review_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SelfSubjectRulesReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectRulesReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'pretty']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_self_subject_rules_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_self_subject_rules_review`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api('/apis/authorization.k8s.io/v1/selfsubjectrulesreviews', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='V1SelfSubjectRulesReview',
                                        auth_settings=auth_settings,
                                        async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_subject_access_review(self, body, **kwargs):
        """
        create a SubjectAccessReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_subject_access_review(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SubjectAccessReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1SubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_subject_access_review_with_http_info(body, **kwargs)
        else:
            (data) = self.create_subject_access_review_with_http_info(body, **kwargs)
            return data

    def create_subject_access_review_with_http_info(self, body, **kwargs):
        """
        create a SubjectAccessReview
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_subject_access_review_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SubjectAccessReview body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1SubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'pretty']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subject_access_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_subject_access_review`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api('/apis/authorization.k8s.io/v1/subjectaccessreviews', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='V1SubjectAccessReview',
                                        auth_settings=auth_settings,
                                        async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_api_resources(self, **kwargs):
        """
        get available resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_resources(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1APIResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_resources_with_http_info(**kwargs)
        else:
            (data) = self.get_api_resources_with_http_info(**kwargs)
            return data

    def get_api_resources_with_http_info(self, **kwargs):
        """
        get available resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_resources_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1APIResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_resources" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])

        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api('/apis/authorization.k8s.io/v1/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='V1APIResourceList',
                                        auth_settings=auth_settings,
                                        async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
