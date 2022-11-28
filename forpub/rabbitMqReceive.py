# -*- coding: UTF-8 -*-
import json
import logging

import requests
import pika

"""
多个消费者的情况下，采用的是轮训机制依次转发给每一个消费者
"""
# 验证
credentials = pika.PlainCredentials('zxc', 'zxc')
# 创建连接 virtual_host rabbitMQ 使用的虚拟主机(可以有多个，对不同用户进行权限分离)
conn = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.85.134', port=5672, virtual_host='/shaanxituishu', credentials=credentials))
# 建立一个channel
chan = conn.channel()
# 创建一个队列(生成者没有指定 exchange), 如果确定已经创建了, 可以不在创建
# chan.queue_declare(queue='active')
# 生产者指定exchange, 要绑定队列和exchange, 不绑定，exchange不知道把消息转发给那个队列
chan.queue_bind(queue='rabbit', exchange='sxts')


def callback(chan, method, properties, body):
    """
    消息处理函数 4个参数是固定的
    :param chan: channel对象
    :param method: 交付信息
        包含了:
            consumer_tag: 消费者的标识
            delivery_tag: 消息的索引从1开始
            exchange: 指定的exchange
            redelivered: 是不是重复接收的消息
            routing_key: 队列名称
    :param properties: 消息属性
    :param body: 消息
    :return:
    """
    body=body.decode("utf-8")
    try:
        body=json.loads(body)
        qqurl=body["url"]
        logging.info(qqurl)
        print(qqurl)
        jiamibiaoshi=body["jiamibiaoshi"]
        logging.info(jiamibiaoshi)
        print(jiamibiaoshi)
        shaanxi_tuishu_a=body["msg"]
        if jiamibiaoshi=="0":
            shaanxi_tuishu_a=json.loads(shaanxi_tuishu_a)
            ret = requests.post(qqurl, json=shaanxi_tuishu_a,timeout=3)
        else:
            ret = requests.post(qqurl, data=shaanxi_tuishu_a,timeout=3)
        logging.info(ret.text)
        logging.info("log推数完成............推数到：" + str(qqurl))
        print("print推数完成............推数到：" + str(qqurl))
    except:
        logging.info("陕西推数失败，推数地址或mq报文异常，url传入端口不正确，url请传入正确推数的端口")
        print("陕西推数失败，推数地址或mq报文异常，url传入端口不正确，url请传入正确推数的端口")
    # 通知服务端，消息取走了，如果auto_ack=False，不加下面，消息会一直存在
    # 保证数据安全
    # 回复确认，rabbitmq的server就把该消息删除
    chan.basic_ack(delivery_tag=method.delivery_tag)


# auto_ack 默认是False 不给生产者发确认消息(重启consume时会按顺序读取), 如果设置自动确认, 宕机消息就丢了. 可以手动确认
chan.basic_consume(queue='rabbit', on_message_callback=callback,auto_ack=False)

# 开始监听
logging.info("start consuming")
print("start consuming")
chan.start_consuming()
