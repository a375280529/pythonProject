#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys

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

        self.browser.get("http://192.168.81.105:58085/hydra-h5/#/?web_type=h5&province=1200&city=1200&appId=AidT5fedbfb0e4b0acafaebc8bec&nsrsbh=&frmc=&frzjhm=&reqId=undefined&companyName=&certCode=&legalPersonName=&protocol_uri=undefined")

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

        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/input").send_keys("a123456")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/input").send_keys("ax")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/input").send_keys("dd")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/input").send_keys("ff")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[5]/div/input").send_keys("6666")

        time.sleep(3)
        self.browser.execute_script(
            "ff=document.getElementsByClassName('item')[4].getElementsByTagName('div')[0].getElementsByTagName('input')[0];"
            "ff.value='7898';")
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/input").clear()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[4]/input").send_keys("8888")
        time.sleep(3)
        self.browser.execute_script("ff=document.getElementsByClassName('item')[4].getElementsByTagName('div')[0].getElementsByTagName('input')[0];"
                                    "ff.value='1233';")
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[6]").click()


        # 需要进行截图的时候，直接调用截图函数就ok，下同

        # self.save_img('打开登录页面')
        #
        # time.sleep(1)
        #
        # self.browser.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        #
        # self.browser.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("a123456")
        #
        # self.browser.find_element_by_id("TANGRAM__PSP_11__password").send_keys("123456")
        #
        # time.sleep(1)
        #
        # self.save_img('输入账号密码')
        #
        # self.browser.find_element_by_id("TANGRAM__PSP_11__submit").click()
        # self.assertEqual("1","2")
        #
        # time.sleep(1)
        #
        # self.save_img('登录')


if __name__ == '__main__':
    unittest.main()
