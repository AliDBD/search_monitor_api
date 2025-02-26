import requests
import logging
from config import load_config
#ssss

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ApiCollector:
    def __init__(self):
        config = load_config()
        self.base_url = config["platform_url"]
        self.endpoint = config["api"]["endpoint"]
        self.token = config["api"]["token"]
        self.params = config["api"]["params"]

    def collect_search_results(self, keyword):
        try:
            url = f"{self.base_url}{self.endpoint}"  # self.base_url 现在是"https://www.chinagoods.com"
            headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
            params = {**self.params, "q": keyword}
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = data.get("results", [])
            logger.info(f"关键词'{keyword}'采集成功，共{len(results)}条结果")
            return results
        except requests.RequestException as e:
            logger.error(f"API请求失败：{e}")
            return []

    def close(self):
        logger.info("API采集器关闭")