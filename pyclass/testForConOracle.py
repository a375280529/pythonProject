#!/usr/bin/python
# -*- coding: utf-8 -*-

import cx_Oracle as cx
import logging

class TestCase(object):
    def __init__(self, methodName='runTest'):
        self._testMethodName = methodName
        self._outcome = None
        self._testMethodDoc = 'No test'
        try:
            testMethod = getattr(self, methodName)
        except AttributeError:
            if methodName != 'runTest':
                # we allow instantiation with no explicit method name
                # but not an *incorrect* or missing method name
                raise ValueError("no such test method in %s: %s" %
                      (self.__class__, methodName))
        else:
            self._testMethodDoc = testMethod.__doc__
        self._cleanups = []
        self._subtest = None

        # Map types to custom assertEqual functions that will compare
        # instances of said type in more detail to generate a more useful
        # error message.
        self._type_equality_funcs = {}
        self.conOracle(dict, 'assertDictEqual')
        self.conOracle(list, 'assertListEqual')
        self.conOracle(tuple, 'assertTupleEqual')
        self.conOracle(set, 'assertSetEqual')
        self.conOracle(frozenset, 'assertSetEqual')
        self.conOracle(str, 'assertMultiLineEqual')

    def conOracle(self,url):
        # 连接数据库
        conn = cx.connect(url)
        # # 使用cursor()方法获取操作游标
        # cursor = conn.cursor()
        # # 使用execute方法执行SQL语句
        # result = cursor.execute('select * from A t')
        # # 使用fetchone()方法获取一条数据
        # # data = cursor.fetchone()
        # # 获取所有数据
        # all_data = cursor.fetchall()
        # # 获取部分数据，根据传入数字来判断获取多少条
        # # many_data=cursor.fetchmany(8)
        # print(all_data)
        # print(len(all_data))
        # # 关闭游标
        # cursor.close()
        # # 关闭数据库连接
        # conn.close()
        return conn


    def queryOracle(self,url, sql):
        conn = self.conOracle(url)
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 使用execute方法执行SQL语句
        result = cursor.execute(sql)
        # 使用fetchone()方法获取一条数据
        # data = cursor.fetchone()
        # 获取所有数据
        all_data = cursor.fetchall()
        # 获取部分数据，8条
        # many_data=cursor.fetchmany(8)
        print(all_data)
        print(len(all_data))
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()


    def updateOracle(self,url, sql):
        # 连接数据库
        # "jrwz2_zx/jrwz2_zx@192.168.81.41:1521/emserver"
        conn = self.conOracle(url)
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        try:
            # 使用execute方法执行SQL语句
            # "INSERT INTO A (A, B, C, D)VALUES('CESHI', 'CESHI', sysdate, sysdate)"
            cursor.execute(sql)
            # 提交数据
            conn.commit()
            logging.info("插入或更新成功！")
        except:
            conn.rollback()
            logging.error("异常sql！")
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()



if __name__ == '__main__':
    pass
