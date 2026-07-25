from page.base_page import BasePage


class CachePage(BasePage):
    def clear_cache(self, cache_type="all"):
        """清理缓存：all全部/image图片/cookie"""
        path = "/cache/clear"
        body = {"cache_type": cache_type}
        resp = self.api.send_request(path=path, method="POST", json_data=body)
        return resp

    def set_incognito_mode(self, status):
        """切换无痕模式开关，status布尔值true开启/false关闭"""
        path = "/incognito/switch"
        body = {"open": status}
        resp = self.api.send_request(path=path, method="POST", json_data=body)
        return resp