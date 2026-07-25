from page.base_page import BasePage


class BookmarkPage(BasePage):
    def add_bookmark(self, title, url):
        """新增网页收藏"""
        path = "/bookmark/add"
        body = {"title": title, "url": url}
        resp = self.api.send_request(path=path, method="POST", json_data=body)
        return resp

    def get_bookmark_list(self):
        """获取全部收藏列表"""
        path = "/bookmark/list"
        resp = self.api.send_request(path=path, method="GET")
        return resp

    def delete_bookmark(self, bookmark_id):
        """根据id删除单条收藏"""
        path = "/bookmark/delete"
        body = {"bookmark_id": bookmark_id}
        resp = self.api.send_request(path=path, method="DELETE", json_data=body)
        return resp