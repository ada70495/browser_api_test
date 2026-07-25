import allure
import os
import pytest
from common.yaml_handler import YamlHandler
from utils.file_path import DATA_PATH
from page.cache_page import CachePage
from utils.assert_util import assert_status_code, assert_msg_contain

cache_yaml_path = os.path.join(DATA_PATH, "cache_case.yaml")
cache_data = YamlHandler(cache_yaml_path).read_yaml()["clear_cache_cases"]


@allure.feature("浏览器-缓存与无痕模式")
class TestCacheApi:
    @allure.story("清理各类缓存接口")
    @pytest.mark.parametrize("case", cache_data)
    def test_clear_cache(self, case):
        cache = CachePage()
        resp = cache.clear_cache(cache_type=case["cache_type"])
        res_json = resp.json()
        assert_status_code(resp)
        assert_msg_contain(res_json, case["expect_msg"])

    @allure.story("切换无痕模式开关")
    def test_switch_incognito(self):
        cache = CachePage()
        resp = cache.set_incognito_mode(status=True)
        assert_status_code(resp)