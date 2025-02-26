# src/analyzers/trend_analyzer.py
import pandas as pd
import matplotlib.pyplot as plt
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        plt.title("Search Accuracy Trends")
        plt.xlabel("Keyword")
        plt.ylabel("Accuracy (%)")
        plt.savefig(os.path.join("logs", "accuracy_trend.png"))
        plt.close()
        logger.info("Trend plot generated")