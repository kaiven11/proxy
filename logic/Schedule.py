#coding=utf-8
import json
import time
import multiprocessing as mp
from logic.filter_url import filter_url
from logic.getter import proxy_get
from logic.timing_check import timingcheck
from logic.dataconf import DateRedis
import  grequests


class Schedule:
    RedisOperator = DateRedis.Get_instance()
    def __init__(self,maxlen):
        self.MaxLength=maxlen #the proxie maxlengh
        self.check=timingcheck(2)
        self.cache=[]
        self.res=[]

    def run(self):
            pool=mp.Pool(3)
            #if the proxies count is not enough,first check the cache
            if self.cache:
                for k,v in enumerate(self.cache):
                    if self.Get_count() < self.MaxLength:
                        self.RedisOperator.push_r(json.dumps(v))
                        self.cache.remove(v)
            else:
                m = proxy_get()
                #start the defined funtions in getter moudule
                for fun in m.funtool:
                    self.res.extend(fun(m))
                #check the proxies
                result_map = pool.map(filter_url().ok, self.res)
                result=grequests.map(result_map)
                #beacause the count of result_map equal the count of result,and the order is the same
                for k,v in zip(result_map,result):
                    if v:
                        correct_proxies=k.__dict__['kwargs']
                        proxies=correct_proxies['proxies']
                        if self.Get_count() < self.MaxLength:
                            self.RedisOperator.push_r(json.dumps(proxies))
                        self.cache.append(proxies)

    def excute(self):
        """
        check the count of proxies for loop,if less then start the function of run
        """
        while True:
            if self.Get_count()==0:
                self.check.event=False

            if self.Get_count()<self.MaxLength:
                print('Insufficient number of agents, start filling operation!')
                self.run()
                self.check.event=True
            else:
                print('The Proxy Is Enough')
                time.sleep(5)


    def start_timingcheck(self):
        """
        start the check moudule
        """
        self.check.check_queue()
    def Get_count(self):
        """
        get the count of proxies from redis
        """
        return  self.RedisOperator.get_count()
    def start(self):
        """
        start two processes to get proxies and check the proxies
        """
        p1 = mp.Process(target=self.excute, args=())
        p2 = mp.Process(target=self.start_timingcheck)
        p1.start()
        p2.start()








