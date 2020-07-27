"""
============================
Author:柠檬班-木森
Time:2020/7/7   14:47
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from unittestreport import TestRunner,HTMLTestRunner

suite1 = unittest.defaultTestLoader.discover(r"C:\project\musen\case_test")

tr = HTMLTestRunner(stream=open("report.html",'wb'), title='木森的测试报告',)
tr.run(suite1)
