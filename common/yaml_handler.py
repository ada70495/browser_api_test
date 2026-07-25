import yaml
from common.logger import log


class YamlHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_yaml(self):
        """读取yaml文件，异常捕获并打印日志"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            return data
        except Exception as e:
            log.error(f"读取YAML失败 | 文件路径：{self.file_path}, 报错详情：{e}")
            raise

    def write_yaml(self, data):
        """写入yaml文件，保证中文正常显示，不自动排序key"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)