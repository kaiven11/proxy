#coding=utf-8
import time
import requests
import json
from logic.dataconf import DateRedis
from requests.exceptions import RequestException
from logic.conf import *
class timingcheck:
    dataoperator=DateRedis.Get_instance()
    def __init__(self,interval):
        self.event=True #是否运行的标志
        self.interval=interval
    def check_queue(self):
        """
        check the url if event is True
        """
        print('The Check Moudule Starts!')
        while self.event:
            proxies=self.dataoperator.pop_l()
            url=json.loads(proxies.decode())
            if proxies:
                print('Checking %s'%url)
                try:
                    f = requests.get(TEST_URL,proxies=url,timeout=10)
                    if f.status_code==200:
                        self.dataoperator.push_r(proxies)
                except RequestException:
                    pass

            else:
                print("The Proxies Is Depleted! ")
                time.sleep(20)
            time.sleep(10)
