# 导包
import unittest

# 定义测试套件
from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")

# 获取报告存储文件流 并实例化Html TestRunner 调用run方法
with open("./report/report.html", "wb")as f:
    HTMLTestRunner(stream=f).run(suite)
