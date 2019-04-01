# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import time
import random

from scrapy import signals

from myspider.settings import USER_AGENT_LIST, PROXY_LIST


class UserAgentMiddleware:

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        print('--'*1000)
        request.headers['User-Agent'] = user_agent

    def process_response(self,request,response,spider):
        print('random request header is -->', request.headers['User-Agent'])
        time.sleep(5)
        return response


class RandomProxyMiddleware(object):

    def process_request(self, request, spider):

        if not PROXY_LIST:
            print('not set proxy or proxy list is null')
            return

        proxy = random.choice(PROXY_LIST)
        print(proxy)

        if 'user_passwd' in proxy:
            print('收费代理')
            b64_up = base64.b64encode(proxy['user_passwd'].encode())
            request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
            request.meta['proxy'] = proxy['ip_port']
        else:
            print('免费代理')
            request.meta['proxy'] = proxy['ip_port']

