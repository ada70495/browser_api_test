from page.base_page import BasePage


class LoginPage(BasePage):
    def login(self, username, password):
        """
        浏览器账号密码登录接口
        :param username: 账号
        :param password: 密码
        :return: 接口response
        """
        path = "/user/login"
        body = {
            "username": username,
            "password": password
        }
        resp = self.api.send_request(path=path, method="POST", json_data=body)
        return resp