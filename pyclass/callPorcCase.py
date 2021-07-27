#!/usr/bin/python
# -*- coding: utf-8 -*-
import conOracle as con
import cx_Oracle as cx
import unittest

class callProcCase(unittest.TestCase):
    def setUp(self):
        print("连接数据库和获取游标")

    def tearDown(self):
        print("关闭游标和数据库")

    def useCallporc(self,url):
        #conn = conOracle("hrxj_test/hrxj_test@192.168.85.81:1521/emserver")
        conn = con.conOracle("jrwz2_zx/jrwz2_zx@192.168.81.41:1521/emserver")
        cursor = conn.cursor()
        # 声明变量
        # plsql入参
        user = 'zxc'
        #V_NSRSBH = '914201125848100005'
        # plsql出参
        V_OUT_RESULT = cursor.var(cx.STRING)
        # V_OUT = cursor.var(cx.STRING)
        # OUT_FLAG = cursor.var(cx.NATIVE_FLOAT)
        # RATE_1 = cursor.var(cx.STRING)
        # YSXED_1 = cursor.var(cx.STRING)
        # XYPJ_1 = cursor.var(cx.STRING)
        # RISK_LABEL = cursor.var(cx.STRING)
        try:
            cursor.callproc('AA_CESHI',[user, V_OUT_RESULT])
        except Exception as e:
            print(e)
        self.assertEqual(V_OUT_RESULT.getvalue(),user+", Good Morning!")
        print(123)
        cursor.close()
        conn.close()

if __name__ == '__main__':
    unittest.main()