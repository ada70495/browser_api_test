import pytest
import os
from utils.file_path import DATA_PATH
from common.yaml_handler import YamlHandler
from page.login_page import LoginPage
from config import settings


# 读取登录yaml用例数据，供给test_login使用
@pytest.fixture(scope="session")
def login_data():
    yaml_path = os.path.join(DATA_PATH, "login_case.yaml")
    data = YamlHandler(yaml_path).read_yaml()
    return data["login_cases"]


# session级别全局登录，所有用例执行前登录一次，全局赋值token
@pytest.fixture(scope="session", autouse=True)
def get_login_token():
    login_api = LoginPage()
    # 读取本地.env配置的账号密码登录
    resp = login_api.login(settings.TEST_USER, settings.TEST_PWD)
    res_json = resp.json()
    # 全局赋值token，所有接口自动携带鉴权
    settings.TOKEN = res_json["data"]["token"]
    yield
    # 所有用例跑完清空token
    settings.TOKEN = ""