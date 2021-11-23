#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from io import StringIO as StringIO
import time
import json
import unittest
import platform
import base64
from distutils.sysconfig import get_python_lib
import traceback
from functools import wraps


def report(description, filename: str = None, log_path='.',fimap={"testPass": 0,"testResult": [],"testName": "","testAll": 0,"testFail": 0,"beginTime": "","totalTime": "","testSkip": 0}):
    """
        生成测试报告,并放在当前运行路径下
    :param log_path: 生成report的文件存储路径
    :param filename: 生成文件的filename
    :param description: 生成文件的注释
    :return:
    """
    if filename:
        filename = filename if filename.endswith('.html') else filename + '.html'

    log_path = os.path.abspath(log_path)
    output_report(log_path=log_path,filename=filename,fimap=fimap)
    text = '\n测试已全部完成, 可前往{}查询测试报告'.format(log_path)
    print(text)

def output_report(log_path="",filename="",fimap={}):
    """
        生成测试报告到指定路径下
    :return:
    """
    # SITE_PAKAGE_PATH = get_python_lib()
    # config_tmp_path = SITE_PAKAGE_PATH + '/BeautifulReport/template/template'
    config_tmp_path = '.\\forpub\\template'
    template_path = config_tmp_path
    override_path = os.path.abspath(log_path) if \
        os.path.abspath(log_path).endswith('/') else \
        os.path.abspath(log_path) + '/'

    with open(template_path, 'rb') as file:
        body = file.readlines()
    if not os.path.exists(override_path):
        os.makedirs(override_path)
    with open(override_path + filename, 'wb') as write_file:
        for item in body:
            if item.strip().startswith(b'var resultData'):
                head = '    var resultData = '
                item = item.decode().split(head)
                # 测试报告赋值
                item[1] = head + json.dumps(fimap, ensure_ascii=False, indent=4)
                item = ''.join(item).encode()
                item = bytes(item) + b';\n'
            write_file.write(item)