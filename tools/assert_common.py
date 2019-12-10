def assert_common(self, response, status_code=200, msg="操作成功！"):
    """
    :param self:unittest.TestCase实例对象
    :param response:接口请求后响应的对象
    :param status_code:默认状态码
    :param msg:默认消息
    :return:无返回
    """
    # 状态码200
    self.assertEqual(status_code, response.status_code)
    # 断言success
    self.assertTrue(response.json().get("success"))
    # 断言 code
    self.assertEqual(10000, response.json().get("code"))
    # 断言msg
    self.assertEqual(msg, response.json().get("message"))
