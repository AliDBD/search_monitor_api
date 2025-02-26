# E-commerce Search Monitor (API)
通过API监控公司电商平台搜索准确度和质量的自动化工具。

## 安装
1. 克隆仓库：`git clone https://github.com/AliDBD/search_monitor_api.git`
2. 安装依赖：`pip install -r requirements.txt`

## 使用
运行：`python src/main.py`


**
search_monitor_api/
├── config/                  # 配置文件，存放项目设置
│   ├── __init__.py          # 标记为Python包，导出配置函数
│   ├── load_config.py       # 读取platform_config.yaml的函数
│   └── platform_config.yaml  # YAML配置文件，定义平台URL、API端点、关键词等
├── src/                     # 源代码，核心逻辑
│   ├── __init__.py          # 标记为Python包，导出所有模块
│   ├── collectors/          # 采集模块，负责API调用获取搜索结果
│   │   ├── __init__.py      # 标记为Python包，导出ApiCollector
│   │   └── api_collector.py  # ApiCollector类，调用API采集数据
│   ├── processors/          # 处理模块，评估搜索准确度和质量
│   │   ├── __init__.py      # 标记为Python包，导出AccuracyProcessor
│   │   └── accuracy_processor.py  # AccuracyProcessor类，处理数据
│   ├── analyzers/           # 分析模块，分析趋势并生成图表
│   │   ├── __init__.py      # 标记为Python包，导出TrendAnalyzer
│   │   └── trend_analyzer.py  # TrendAnalyzer类，计算趋势、绘图
│   ├── outputs/             # 输出模块，生成报告
│   │   ├── __init__.py      # 标记为Python包，导出ReportGenerator
│   │   └── report_generator.py  # ReportGenerator类，生成CSV/HTML报告
│   └── schedulers/          # 调度模块，定时运行任务
│       ├── __init__.py      # 标记为Python包，导出run_daily
│       └── task_scheduler.py  # TaskScheduler类，使用apscheduler定时运行main
├── tests/                   # 单元测试，确保模块稳定
│   ├── __init__.py          # 标记为Python包，组织测试
│   ├── test_collectors.py   # 测试ApiCollector
│   ├── test_processors.py   # 测试AccuracyProcessor
│   ├── test_analyzers.py    # 测试TrendAnalyzer
│   └── test_outputs.py      # 测试ReportGenerator
├── docs/                    # 文档，记录设计和说明
│   └── design.md            # Markdown文档，描述架构
├── logs/                    # 日志，运行时生成文件（如accuracy_trend.png、search_metrics.csv）
├── venv/                    # 虚拟环境，隔离Python依赖（忽略Git）
├── search_monitor_api.code-workspace  # Cursor工作区文件，记录项目配置
├── README.md                # 项目说明，描述功能、安装、运行
└── requirements.txt         # 依赖列表，记录Python包
**