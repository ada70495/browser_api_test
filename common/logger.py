from loguru import logger
from utils.file_path import LOG_PATH
import os

# 拼接日志文件完整路径
log_file = os.path.join(LOG_PATH, "browser_api_test.log")

# 日志配置：文件分割、过期清理、编码、多线程安全、日志格式
logger.add(
    log_file,
    rotation="500MB",
    retention="10 days",
    encoding="utf-8",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function}:{line} | {message}"
)

# 全局日志对象，整个项目统一调用
log = logger