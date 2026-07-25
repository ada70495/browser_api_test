import allure
import os
import pytest
from common.yaml_handler import YamlHandler
from utils.file_path import DATA_PATH
from page.history_page import HistoryPage
from utils.assert_util import assert_status_code, assert_msg_contain

history_yaml_path = os.path.join(DATA_PATH, "history_case.yaml")
history_data = YamlHandler(history_yaml_path).read_yaml()["add_history_cases"]


@allure.feature("浏览器-浏览历史模块")
class TestHistoryApi:
    @allure.story("新增浏览记录接口")
    @pytest.mark.parametrize("case", history_data)
    def test_add_history(self, case):
        history = HistoryPage()
        resp = history.add_history(title=case["title"], url=case["url"], visit_time=case["visit_time"])
        res_json = resp.json()
        assert_status_code(resp)
        assert_msg_contain(res_json, case["expect_msg"])

    @allure.story("一键清空全部历史记录")
    def test_clear_history(self):
        history = HistoryPage()
        resp = history.clear_all_history()
        assert_status_code(resp)