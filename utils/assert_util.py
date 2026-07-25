def assert_status_code(response, expect_code=200):
    """断言HTTP接口响应状态码"""
    actual_code = response.status_code
    assert actual_code == expect_code, f"状态码错误，实际:{actual_code}，预期:{expect_code}"


def assert_json_contain(res_json, key):
    """断言返回的json字典包含指定key字段"""
    assert key in res_json, f"返回JSON缺失必填字段：{key}"


def assert_equal(res_json, key, expect_value):
    """断言json内某个key的值等于预期值"""
    actual_val = res_json.get(key)
    assert actual_val == expect_value, f"字段{key}断言失败，实际值:{actual_val}，预期值:{expect_value}"


def assert_msg_contain(res_json, msg):
    """断言返回提示信息包含指定关键字"""
    actual_msg = res_json.get("msg", "")
    assert msg in actual_msg, f"提示文案不匹配，实际：{actual_msg}，预期包含：{msg}"