import allure
import pytest
import os
from page.login_page import LoginPage
from utils.assert_util import assert_status_code, assert_msg_contain, assert_json_contain
from utils.file_path import DATA_PATH
from common.yaml_handler import YamlHandler

yaml_path = os.path.join(DATA_PATH, "login_case.yaml")
login_data = YamlHandler(yaml_path).read_yaml()["login_cases"]

@allure.feature("浏览器-登录模块")
class TestLoginApi:
    @allure.story("账号密码登录接口")
    @pytest.mark.parametrize("case", login_data)
    def test_login_api(self, case):
        """yaml数据驱动执行多场景登录用例"""
        login = LoginPage()
        resp = login.login(username=case["username"], password=case["password"])
        res_json = resp.json()

        # 基础状态码断言
        assert_status_code(resp, case["expect_code"])
        # 提示文案断言
        assert_msg_contain(res_json, case["expect_msg"])
        # 成功用例额外校验token存在
        if case.get("expect_token_exist"):
            assert_json_contain(res_json["data"], "token")