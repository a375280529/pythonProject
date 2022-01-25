# -*- coding: utf-8 -*-

import unittest
import time
from BeautifulReport import BeautifulReport
import configparser
import sys
import os
from modelCase.ayanshilei1 import checkCallProNew
import shutil
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))



#获取config
exepath = os.path.realpath(sys.executable)
endpath = exepath.split(exepath.split("\\")[-1])[0]
patha=os.path.join(os.path.abspath('.'), endpath + "iniFile\\")
path=".\\iniFile\\"+"loggeryanshi.ini"
config = configparser.ConfigParser()
config.read(path,encoding="utf-8-sig")

# 用例存放位置

test_case_path = ".\\"+config["path"]["casepath"]

# 测试报告存放位置
nowday=time.strftime("%Y%m%d", time.localtime())
exepath=os.path.realpath(sys.executable)
endpath=exepath.split(exepath.split("\\")[-1])[0]
log_path = os.path.join(os.path.abspath('.'), endpath+nowday)
log_path = config["path"]["caseportpath"]+nowday
bef = os.path.join(os.path.abspath('.'), endpath+"BeautifulReport/template/bueatifulcss")

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
    #test_suite=unittest.TestSuite()
    #test_suite.addTests([checkCallProNew("test_call_pro"),checkCallProNew("test_call_pro1")])
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description=description, log_path=log_path)
    # 用于无网络测试报告无网络的css和js
    # if not os.path.exists(log_path + "/bueatifulcss"):
    #     shutil.copytree(bef, log_path + "/bueatifulcss")
    print("执行完成。。。")
    time.sleep(1)