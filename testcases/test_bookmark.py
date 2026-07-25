import allure
import os
import pytest
from common.yaml_handler import YamlHandler
from utils.file_path import DATA_PATH
from page.bookmark_page import BookmarkPage
from utils.assert_util import assert_status_code, assert_msg_contain

# 读取收藏用例yaml
bookmark_yaml_path = os.path.join(DATA_PATH, "bookmark_case.yaml")
bookmark_data = YamlHandler(bookmark_yaml_path).read_yaml()["add_bookmark_cases"]


@allure.feature("浏览器-收藏夹模块")
class TestBookmarkApi:
    @allure.story("新增收藏接口")
    @pytest.mark.parametrize("case", bookmark_data)
    def test_add_bookmark(self, case):
        bookmark = BookmarkPage()
        resp = bookmark.add_bookmark(title=case["title_name"], url=case["url"])
        res_json = resp.json()
        assert_status_code(resp)
        assert_msg_contain(res_json, case["expect_msg"])

    @allure.story("获取收藏列表接口")
    def test_get_bookmark_list(self):
        bookmark = BookmarkPage()
        resp = bookmark.get_bookmark_list()
        assert_status_code(resp)