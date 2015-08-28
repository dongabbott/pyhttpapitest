# -*-coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'dongjie'
__data__ = '2015-05-20'

from pyapilog import pyapilog
import requests
import json
import urllib

class SendHttpRequest(object):
    def __init__(self, url):
        self.url = url
    # post request

    def post(self, value=None):
        params = urllib.urlencode(value)
        try:
            req = requests.post(self.url + "?%s" % params)
        except Exception, err:
            print err
        if req.status_code == 200:
            pyapilog().info(u"发送post请求: %s  服务器返回:  %s" % (req.url, req.status_code))
        else:
            pyapilog().error(u"发送post请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
        return req.text

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
            pyapilog().info(u"发送get请求: %s   服务器返回:  %s" % (req.url, req.status_code))
        else:
            pyapilog().error(u"发送get请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
        return req.text
