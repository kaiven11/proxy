#coding=utf-8
from requests.exceptions import RequestException, ProxyError
from logic.conf import *
import grequests

class filter_url:
    def __init__(self,tar_url=TEST_URL):
        self.tar_url=tar_url
        self.proxy={}

    def ok(self,url):
        """
        check the proxie and return the result
        :param url: proxy
        :return: asyncrequest objects
        """
        ip = url[0]
        port = url[1]
        type = url[2]
        proxy_end="{}://{}:{}".format(type,ip,port)
        self.proxy.update({type:proxy_end})
        try:
            print("Checking %s"%(ip))
            r=grequests.get(self.tar_url,proxies=self.proxy,timeout=10)
            self.proxy={} #清空proxy
            return r
        except (RequestException,ProxyError):
            print('%s is invalid'%ip)



