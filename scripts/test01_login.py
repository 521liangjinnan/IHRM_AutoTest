import unittest

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls) -> None:
        # 获取ApiLogin对象
        cls.login = ApiLogin()

    # 结束
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # 登录测试方法
    def test01_login(self, mobile="13800000002", password="123456"):

        # 调用业务方法
        response = self.login.api_login(mobile, password)
        # print(response.json())

        # 提取token
        token = response.json().get("data")
        api.headers['Authorization'] = "Bearer " + token
        print("登录成功后的heders值为：", api.headers)

        # 断言
        assert_common(self, response)
