"""
分析模块，分析趋势并生成图表
"""
import pandas as pd
import matplotlib.pyplot as plt
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用宋体，支持中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

class TrendAnalyzer:
    def __init__(self):
        self.data = {}

    def analyze(self, metrics):
        self.data = metrics
        trends = self._calculate_trends()
        self._generate_plot(trends)
        return trends

    def _calculate_trends(self):
        trends = {}
        for keyword, metric in self.data.items():
            trends[keyword] = {
                "accuracy_trend": metric["accuracy"],
                "zero_result_trend": metric["zero_result"],
                "duplicate_rate_trend": metric["duplicate_rate"]
            }
        logger.info("Trends calculated successfully")
        return trends

    def _generate_plot(self, trends):
        df = pd.DataFrame(trends).T
        plt.figure(figsize=(10, 6))
        df["accuracy_trend"].plot(kind='line', marker='o')
        plt.title("搜索准确度趋势")
        plt.xlabel("关键词")
        plt.ylabel("准确度 (%)")
        plt.savefig(os.path.join("logs", "accuracy_trend.png"))
        plt.close()
        logger.info("Trend plot generated")