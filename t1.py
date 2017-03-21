#coding=utf-8
__author__ = 'kidd'


class A(object):
    a=3

import redis

r = redis.Redis(host='192.168.1.222', db=0, password='123')

r1 = redis.StrictRedis(host='192.168.1.222', db=1, password='123')

# r0.zadd('name', 'p', '1')
#
# r1.zadd('name', 'p', '1')


print r.sort('today_cost', desc=True, start=0, num=3)

r.scan(count=3, match='*')
r.lindex('a', 1)

r.publish()