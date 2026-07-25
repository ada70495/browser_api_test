import allure
import json


def attach_request(url, method, headers, body):
    """把完整请求信息附加到allure报告，方便问题排查"""
    content = f"""请求地址：{url}
请求方式：{method}
请求头：{json.dumps(headers, ensure_ascii=False, indent=2)}
请求体：{json.dumps(body, ensure_ascii=False, indent=2)}"""
    allure.attach(
        content,
        name="接口请求详情",
        attachment_type=allure.attachment_type.TEXT
    )


def attach_response(resp):
    """把响应内容附加到allure，兼容非json返回"""
    try:
        resp_json = resp.json()
        resp_text = json.dumps(resp_json, ensure_ascii=False, indent=2)
    except Exception:
        resp_text = resp.text
    content = f"响应状态码：{resp.status_code}\n完整响应内容：{resp_text}"
    allure.attach(
        content,
        name="接口响应详情",
        attachment_type=allure.attachment_type.TEXT
    )