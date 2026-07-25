import os
import pytest
import subprocess
from utils.file_path import ALLURE_RAW_PATH, ALLURE_HTML_PATH
from common.logger import log


def run_auto_test():
    log.info("===== 浏览器后台接口自动化测试开始执行 =====")
    # 执行全部pytest自动化用例
    pytest.main()
    # 调用allure命令行生成可视化html报告
    cmd = f"allure generate {ALLURE_RAW_PATH} -o {ALLURE_HTML_PATH} --clean"
    subprocess.call(cmd, shell=True)
    log.info(f"测试执行完成，报告路径：{ALLURE_HTML_PATH}/index.html")
    # 可选：自动打开报告
    # subprocess.call(f"allure open {ALLURE_HTML_PATH}")


if __name__ == "__main__":
    run_auto_test()