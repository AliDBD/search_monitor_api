def test_api_collector():
    from src.collectors.api_collector import ApiCollector
    collector = ApiCollector()
    results = collector.collect_search_results("红苹果")
    assert len(results) > 0, "未抓取到结果"
    collector.close()