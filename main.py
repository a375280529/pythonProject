# -*- coding: utf-8 -*-

import unittest
import time
from BeautifulReport import BeautifulReport
from forpub import forFinal
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))


#获取config
#config=forFinal.getIni("loggerAhp.ini")
config=forFinal.getIni("loggerLiangHua.ini")

# 用例存放位置

test_case_path = ".\\"+config["path"]["casepath"]


# 测试报告存放位置
nowday=time.strftime("%Y%m%d", time.localtime())
log_path = config["path"]["caseportpath"]+nowday

# 测试报告名称
name = config["name"]["casename"]
now = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename = name+'_自动化测试报告'+now

# 用例名称

description = name

# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*testa.py"

pattern = config["path"]["pattern"]

if __name__ == '__main__':
    print("执行中。。。")
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)

    result = BeautifulReport(test_suite)

    result.report(filename=filename, description=description, log_path=log_path)
    print("执行完成。。。")

