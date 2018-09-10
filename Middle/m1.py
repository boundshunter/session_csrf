#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'


from django.utils.deprecation import MiddlewareMixin


class Row1(MiddlewareMixin):
    def process_request(self, request):
        print('王森')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('王森2')

    def process_response(self, request, response):
        print('王森1')
        return response

from django.shortcuts import HttpResponse
class Row2(MiddlewareMixin):
    def process_request(self, request):
        print('诚意强')
        # return HttpResponse('66666')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('诚意强2')

    def process_response(self, request, response):
        print('诚意强1')
        return response


class Row3(MiddlewareMixin):
    def process_request(self, request):
        print('刘东')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('刘东2')

    def process_response(self, request,  response):
        print('刘东1')
        return response
