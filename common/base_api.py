import requests
from config.settings import BASE_URL, TIMEOUT, GLOBAL_HEADERS, TOKEN
from common.logger import log
from common.allure_attach import attach_request, attach_response


class BaseApi:
    def __init__(self):
        # 使用session保持会话，自动维持cookie，长连接复用
        self.session = requests.Session()

    def send_request(self, path, method, json_data=None, params=None, headers=None):
        """
        统一接口请求入口
        :param path: 接口后缀路径 /user/login
        :param method: 请求方式 GET/POST/PUT/DELETE
        :param json_data: post请求json入参
        :param params: get请求url参数
        :param headers: 自定义额外请求头
        :return: requests响应对象
        """
        # 拼接完整接口地址
        url = f"{BASE_URL}{path}"
        # 拷贝全局请求头，避免原字典被修改
        headers_all = GLOBAL_HEADERS.copy()

        # 如果全局有token，自动加入鉴权头
        if TOKEN:
            headers_all["Authorization"] = f"Bearer {TOKEN}"
        # 合并自定义请求头
        if headers:
            headers_all.update(headers)

        log.info(f"【{method.upper()}】请求地址：{url}")
        log.info(f"params参数：{params} | json参数：{json_data}")
        # 请求信息写入allure报告
        attach_request(url, method, headers_all, json_data)

        try:
            # 分发不同请求方式
            if method.upper() == "GET":
                resp = self.session.get(url, headers=headers_all, params=params, timeout=TIMEOUT)
            elif method.upper() == "POST":
                resp = self.session.post(url, headers=headers_all, json=json_data, timeout=TIMEOUT)
            elif method.upper() == "PUT":
                resp = self.session.put(url, headers=headers_all, json=json_data, timeout=TIMEOUT)
            elif method.upper() == "DELETE":
                resp = self.session.delete(url, headers=headers_all, json=json_data, timeout=TIMEOUT)
            else:
                raise Exception(f"当前框架不支持该请求方式：{method}")

            log.info(f"接口响应状态码：{resp.status_code}")
            attach_response(resp)
            return resp
        except Exception as e:
            log.error(f"接口请求出现异常：{str(e)}")
            raise