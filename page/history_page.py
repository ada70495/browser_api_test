from page.base_page import BasePage


class HistoryPage(BasePage):
    def add_history(self, title, url, visit_time):
        """新增一条浏览历史记录"""
        path = "/history/add"
        body = {"title": title, "url": url, "visit_time": visit_time}
        resp = self.api.send_request(path=path, method="POST", json_data=body)
        return resp

    def clear_all_history(self):
        """一键清空全部浏览历史"""
        path = "/history/clear"
        resp = self.api.send_request(path=path, method="POST")
        return resp