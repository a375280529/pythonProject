#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
import datetime

class Test(unittest.TestCase):

    # 定义一个保存截图函数

    def save_img(self, img_name):
        img_path = "D:/test/img"
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        self.browser.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(img_path), img_name))

    # 启动函数，每个用例测试前，都会执行该函数

    def setUp(self):
        self.browser = webdriver.Chrome()

        self.browser.set_window_size(1920, 1080)

        self.starttime = datetime.datetime.now()
        self.start=time.time()

        print("开始测试时间：", self.starttime)
        print("开始测试时间time：", self.starttime)

        self.browser.get("https://www.baidu.com/")

        time.sleep(1)

    # 结束函数，每个用例测试结束后，都会执行该函数

    def tearDown(self):
        time.sleep(1)

        self.browser.quit()

        self.endtime = datetime.datetime.now()
        self.end=time.time()

        print("测试结束时间：", self.endtime)
        print("测试结束时间time：", self.endtime)

        totaltime = (self.endtime - self.starttime).total_seconds()
        total = '{0:.3} s'.format((self.end - self.start))
        print("总时长：", totaltime, "秒")
        print("总时长time：", total)

    # 测试用例1：必须以test_开头

    def test_01(self):
        u"""登录"""

        self.browser.find_element_by_xpath("//*[@id=\"s-top-loginbtn\"]").click()

        # 需要进行截图的时候，直接调用截图函数就ok，下同

        self.save_img('打开登录页面')

        time.sleep(1)

        self.browser.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

        self.browser.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("a123456")

        self.browser.find_element_by_id("TANGRAM__PSP_11__password").send_keys("123456")

        time.sleep(1)

        self.save_img('输入账号密码')

        self.browser.find_element_by_id("TANGRAM__PSP_11__submit").click()
        self.assertEqual("1","2")

        time.sleep(1)

        self.save_img('登录')


if __name__ == '__main__':
    unittest.main()
