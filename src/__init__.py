# src/__init__.py
"""
导出所有模块
"""
from .collectors import ApiCollector
from .processors import AccuracyProcessor
from .analyzers import TrendAnalyzer
from .outputs import ReportGenerator
from .schedulers import run_daily