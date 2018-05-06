#coding=utf-8
import re

import requests
from requests import RequestException
from logic.conf import *


class proxy_get:
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        """
        add "funtool" to the class when instantiation
        """
        cls.funtool = []
        for k, v in proxy_get.__dict__.items():
            if (type(v).__name__) == 'function':
                if not k.startswith('__') and k.startswith('Crawl'):
                    cls.funtool.append(v)
        return object.__new__(cls)

    def Crawl_data5u(self):
        """
        Crawl the url and return the result
        """
        print('Crawl_data5u')
        url='http://www.data5u.com/'
        try:
            r=requests.get(url=url,headers=HEADERS)
        except RequestException as e:
            return
        if r.status_code==200:
            result=re.compile('<ul class="l2">.*?<span>.*?<li>(.*?)</li>.*?</span>.*?<li class="port.*?>(.*?)</li>.*?<a class="href" href=".*?free/type.*?>(.*?)</a>.*?</li>.*?</ul>',re.S).findall(r.text)
            return result
    def parse_string(self,data):
        """
        parse the data from 66ip
        :param data:
        :return:proxies
        """
        a=[]
        b=[]
        for k, v in enumerate(data):
            if k % 5 == 0:
                a.append(v)
            if k % 5 == 1:
                b.append(v)
        c=['https' for x in range(len(a))]
        return list(zip(a,b,c))[1:]

    def Crawl_66ip(self):
        """
        Crawl the 66ip
        :return:
        """
        url = 'http://www.66ip.cn/'
        try:
            r = requests.get(url=url, headers=HEADERS)
        except RequestException as e:
            return
        if r.status_code == 200:
            result = re.compile('<td>(.*?)</td>').findall(r.text)
            m=self.parse_string(result)
            return m

