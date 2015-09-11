# -*-coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'dongjie'
__data__ = '2015-05-20'

import requests
from requests.exceptions import Timeout
import json
from json import JSONEncoder
import urllib
import settings
from urlparse import urljoin
from pyapilog import pyapilog

# 从配置文件获取http请求第一地址
request_address = settings.SERVER + ':' + str(settings.PORT) + '/'
print request_address

# http请求方法实现,目前暂时只实现post 和get方法
class SendHttpRequest(object):
    def __init__(self, path):
        '''
        :param uri: 接口请求路径
        '''
        self.url = urljoin(request_address, path)

    def post(self, *args, **kwargs):
        '''
        :param args:
        :param kwargs: 以多的参数的形式传入
        :return: http请求内容
        '''
        params = urllib.urlencode(kwargs)
        up_url = urljoin(self.url, '/'.join(args))
        req_url = up_url + '?' + params
        try:
            req = requests.post(req_url, timeout=10)
        except Exception, err:
            pyapilog().error(err)
        if req.status_code == 200:
            pyapilog().info(u"发送post请求: %s  服务器返回:  %s\n" % (req.url, req.status_code))
            try:
                result = JSONEncoder().encode(req.json())
            except ValueError:
                result = req.text
            return result
        else:
            pyapilog().error(u"发送post请求: %s   服务器返回:  %s\n" % (req.url, req.status_code))

    def post_json(self, value):
        head = {'content-type': 'application/json'}
        try:
            req = requests.post(self.url, data=json.dumps(value), headers=head)
            print req.url
        except Exception, err:
            print err
        if req.status_code == 200:
            pyapilog().info(u"发送post请求: %s  服务器返回:  %s" % (req.url, req.status_code))
            return req.text
        else:
            pyapilog().error(u"发送post请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))

    def get(self, value=None):
        try:
            req = requests.get(self.url, params=value)
        except Exception, err:
            print err
        if req.status_code == 200:
            pyapilog().info(u"发送get请求: %s   服务器返回:  %s  内容：%s" % (req.url, req.status_code, req.text))
        else:
            pyapilog().error(u"发送get请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
        return req.text