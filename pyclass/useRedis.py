#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379,db是第几个db库
def connectredis(host,db):
    red = redis.Redis(host=host,db=db, port=6379, decode_responses=True)
    return red



if __name__ == '__main__':
    r=connectredis('127.0.0.1',1)
    # pool = redis.ConnectionPool(host='localhost', port=6379,db=1,max_connections=1000,
    #                             decode_responses=True)  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    # r = redis.Redis(connection_pool=pool)
    # r.set('gender', 'male')  # key是"gender" value是"male" 将键值对存入redis缓存
    # r.setex('gender',10,"dsfsd")
    # print(r.get('gender'))  # gender 取出键male对应的值
    #r.rpush("list2", 11, 22, 33)  # 表示从右向左操作
    print(r.lrange("list2",0,-1))  # 列表长度
    #print(r.lpop("list2"))  # 切片取出值，范围是索引号0-3
