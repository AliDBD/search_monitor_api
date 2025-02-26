import os

def test_report_generator():
    from src.outputs.report_generator import ReportGenerator
    generator = ReportGenerator()
    trends = {"红苹果": {"accuracy_trend": 85}}
    generator.generate(trends, "test_report.html")
    assert os.path.exists("test_report.html"), "Report not generated"