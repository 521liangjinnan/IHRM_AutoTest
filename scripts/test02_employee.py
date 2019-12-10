import unittest

import api
from parameterized import parameterized
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from tools.read_txt import read_txt


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls) -> None:
        # 获取ApiEmployee对象
        cls.api = ApiEmployee()

    # 新增员工
    @parameterized.expand(read_txt("employee_post.txt"))
    def test_01(self, username, mobile, workNumber):
        # 调用新增接口
        r = self.api.api_post_emp(username, mobile, workNumber)
        print("新增员工后的结果为：", r.json())
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        print("新增的员工id为：", api.user_id)
        # 断言
        assert_common(self, r)

    # # 更新员工
    # def test_02(self, username="bj16666"):
    #     # 调用修改接口
    #     r = self.api.api_put_emp(username)
    #     print("更新员工名称结果为: ", r.json())
    #     # 断言
    #     assert_common(self, r)
    #
    # # 查询员工
    # def test_03(self):
    #     # 调用查询接口
    #     r = self.api.api_get_emp()
    #     print("查询员工名称结果为：", r.json())
    #     # 断言
    #     assert_common(self, r)

    # 删除员工
    def test_04(self):
        # 调用删除接口
        r = self.api.api_delete_emp(api.user_id)
        print("删除数据结果为：", r.json())

        # 断言
        assert_common(self, r)
