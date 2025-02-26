import os
import pytest
from src.analyzers.trend_analyzer import TrendAnalyzer

def test_trend_analyzer():
    """测试TrendAnalyzer的analyze方法"""
    analyzer = TrendAnalyzer()
    metrics = {
        "红苹果": {"accuracy": 85, "zero_result": False, "duplicate_rate": 5},
        "手机": {"accuracy": 90, "zero_result": False, "duplicate_rate": 3}
    }
    trends = analyzer.analyze(metrics)
    assert isinstance(trends, dict), "Trends should be a dictionary"
    assert trends["红苹果"]["accuracy_trend"] == 85, "Accuracy trend calculation failed"
    assert trends["手机"]["accuracy_trend"] == 90, "Accuracy trend calculation failed"
    assert not trends["红苹果"]["zero_result_trend"], "Zero result trend incorrect"

def test_calculate_trends():
    """测试_calculate_trends方法"""
    analyzer = TrendAnalyzer()
    metrics = {"红苹果": {"accuracy": 85, "zero_result": False, "duplicate_rate": 5}}
    trends = analyzer._calculate_trends()
    assert trends["红苹果"]["accuracy_trend"] == 85, "_calculate_trends accuracy failed"
    assert trends["红苹果"]["duplicate_rate_trend"] == 5, "_calculate_trends duplicate rate failed"

def test_generate_plot():
    """测试_generate_plot方法，验证图表生成"""
    analyzer = TrendAnalyzer()
    metrics = {
        "红苹果": {"accuracy": 85, "zero_result": False, "duplicate_rate": 5},
        "手机": {"accuracy": 90, "zero_result": False, "duplicate_rate": 3}
    }
    analyzer.analyze(metrics)
    plot_path = os.path.join("logs", "accuracy_trend.png")
    assert os.path.exists(plot_path), "Trend plot not generated"