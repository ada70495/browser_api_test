from common.base_api import BaseApi


class BasePage:
    """POM分层父类，所有业务接口页面都继承此类"""
    def __init__(self):
        # 所有业务页面复用同一个底层请求api
        self.api = BaseApi()