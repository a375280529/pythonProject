#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyclass import conOracle as con
import cx_Oracle as cx
import unittest

class callTest(unittest.TestCase):

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.conn = con.conOracle("jrwz2_zx/jrwz2_zx@192.168.81.41:1521/emserver")
        self.cursor = self.conn.cursor()
        print("连接数据库和获取游标")

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.cursor.close()
        self.conn.close()
        print("关闭游标和数据库")

    # 测试用例1：必须以test_开头
    def test_01(self):
        "简单测试存储过程"
        # 声明变量
        # plsql入参
        user = 'zxc'
        # plsql出参
        outresult = self.cursor.var(cx.STRING)
        try:
            self.cursor.callproc('AA_CESHI',[user, outresult])
        except Exception as e:
            print(e)
        result = outresult.getvalue()
        exp = user+", Good Morning!"
        #执行了的print会自动打印到测试报告
        print("预期结果：",exp,"，实际结果：",result)
        self.assertEqual(result,exp,msg="实际值不符合预期值！")

if __name__ == '__main__':
    unittest.main()