"""
处理模块，评估搜索准确度和质量
"""
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AccuracyProcessor:
    def process_results(self, results):
        metrics = {}
        for keyword, data in results.items():
            if not data:
                metrics[keyword] = {
                    "accuracy": 0,
                    "zero_result": True,
                    "duplicate_rate": 0,
                    "result_count": 0
                }
                logger.warning(f"关键词'{keyword}'无搜索结果")
                continue

            accurate_count = sum(1 for item in data if re.search(r'\b' + keyword + r'\b', item.get("title", ""), re.IGNORECASE))
            accuracy = (accurate_count / len(data)) * 100 if len(data) > 0 else 0

            zero_result = len(data) == 0

            urls = [item.get("url", "") for item in data]
            duplicates = sum(1 for url, count in [(url, urls.count(url)) for url in set(urls)] if count > 1)
            duplicate_rate = (duplicates / len(data)) * 100 if len(data) > 0 else 0

            metrics[keyword] = {
                "accuracy": accuracy,
                "zero_result": zero_result,
                "duplicate_rate": duplicate_rate,
                "result_count": len(data)
            }
            logger.info(f"关键词'{keyword}'处理完成，准确度：{accuracy}%")
        return metrics