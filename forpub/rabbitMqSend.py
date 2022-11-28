# -*- coding: UTF-8 -*-
import json

import pika

# 验证 用户名和密码
credentials = pika.PlainCredentials('zxc', 'zxc')
# 创建连接 virtual_host: rabbitMQ 使用的虚拟主机(一个broker可以有多个，对不同用户进行权限分离)
conn = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.85.134', port=5672, virtual_host='/shaanxituishu', credentials=credentials))

# 建立一个channel
chan = conn.channel()
# 声明一个交换机，生成订阅
#chan.exchange_declare(exchange='m1',exchange_type='fanout')
# 创建一个队列
chan.queue_declare(queue='rabbit')


def encode_msg(msg):
    """格式化消息"""
    return json.dumps(msg)


while True:
    # 便于测试
    msg = input('msg: ')
    ps={}
    ps["zz"]=msg

    if msg == 'quit':
        break
    # 发送消息 exchange: 把消息发布到指定交换机, 通过这个交换机转发给消费者; 可以不指定
    # exchange 可以在后台创建
    chan.basic_publish(exchange='sxts', routing_key='rabbit', body=encode_msg(ps))

conn.close()