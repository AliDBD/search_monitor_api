# src/main.py
import logging
from config import load_config
from src.collectors.api_collector import ApiCollector
from src.processors.accuracy_processor import AccuracyProcessor
from src.analyzers.trend_analyzer import TrendAnalyzer
from src.outputs.report_generator import ReportGenerator
from src.schedulers.task_scheduler import run_daily

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    config = load_config()
    keywords = config["keywords"]

    # 采集数据
    collector = ApiCollector()
    results = {}
    for keyword in keywords:
        results[keyword] = collector.collect_search_results(keyword)
    collector.close()

    # 处理数据
    processor = AccuracyProcessor()
    metrics = processor.process_results(results)

    # 分析和输出
    analyzer = TrendAnalyzer()
    trends = analyzer.analyze(metrics)
    report = ReportGenerator()
    report.generate(trends, "search_report.html")
    logging.info("监控完成，报告已生成")

if __name__ == "__main__":
    main()  # 临时直接运行main
    # 如果需要调度，调用run_daily
    run_daily(main)