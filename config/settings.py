import os
# 读取本地.env环境变量
from dotenv import load_dotenv
# 导入路径工具
from utils.file_path import CONFIG_PATH
# 导入yaml读取工具
from common.yaml_handler import YamlHandler

# 加载本地.env文件的环境变量
load_dotenv()

# 读取公开环境配置yaml
env_config = YamlHandler(os.path.join(CONFIG_PATH, "env.yaml")).read_yaml()

# 当前生效环境
CURRENT_ENV = env_config["env"]
# 对应环境的接口根路径
BASE_URL = env_config[CURRENT_ENV]["base_url"]
# 请求超时时间
TIMEOUT = env_config[CURRENT_ENV]["timeout"]
# 全局公共请求头
GLOBAL_HEADERS = env_config["global_headers"]

# 全局token变量，跨所有用例共享登录凭证
TOKEN = ""

# 从本地.env获取私密信息
TEST_USER = os.getenv("TEST_USER")
TEST_PWD = os.getenv("TEST_PWD")
SIGN_KEY = os.getenv("SIGN_KEY")