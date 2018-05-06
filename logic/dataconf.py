#coding=utf-8
import redis

from logic.conf import *


class DateRedis:
    def __init__(self,redis_url,password=None,port=6379):
        self.redis_url=redis_url
        self.password=password
        self.port=port
        self.con=redis.Redis(host=self.redis_url,port=self.port,password=self.password)

    @staticmethod
    def Get_instance():
        return DateRedis(RedisIP)
    def push_r(self,values):
        """
        the new proxie push the right
        """
        if self.con.rpush("proxies",values):
            return  True
        return False


    def pop_r(self,name="proxies"):
        """
        pop the right proxy
        """
        return self.con.rpop("proxies")


    def pop_l(self,name="proxies"):
        """
        pop the left proxy
        """
        return self.con.lpop("proxies")


    def get_count(self):
        """
        return the left proxy
        """
        return self.con.llen("proxies")


