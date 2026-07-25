import os

# 项目根目录绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 各个文件夹路径常量
CONFIG_PATH = os.path.join(BASE_DIR, "config")
DATA_PATH = os.path.join(BASE_DIR, "data")
LOG_PATH = os.path.join(BASE_DIR, "logs")
ALLURE_RAW_PATH = os.path.join(BASE_DIR, "reports", "allure_raw")
ALLURE_HTML_PATH = os.path.join(BASE_DIR, "reports", "allure_html")


def make_dir(path):
    """目录不存在则自动创建"""
    if not os.path.exists(path):
        os.makedirs(path)


# 程序启动自动创建全部需要的文件夹
make_dir(LOG_PATH)
make_dir(ALLURE_RAW_PATH)
make_dir(ALLURE_HTML_PATH)