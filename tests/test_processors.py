def test_accuracy_processor():
    from src.processors.accuracy_processor import AccuracyProcessor
    processor = AccuracyProcessor()
    results = {"红苹果": [{"title": "红苹果新鲜", "url": "https://..."}]}
    metrics = processor.process_results(results)
    assert metrics["红苹果"]["accuracy"] > 0, "准确度计算错误"