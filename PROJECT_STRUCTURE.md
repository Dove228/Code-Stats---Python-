# Code Stats 项目结构

```
code-stats/
�?├── src/code_stats/           # 主包目录
�?  ├── __init__.py          # 包初始化，导出主要API
�?  ├── __main__.py          # CLI命令行入�?�?  �?�?  ├── core/                # 核心模块
�?  �?  ├── __init__.py
�?  �?  ├── analyzer.py      # 代码分析�?�?  �?  ├── complexity.py    # 复杂度分�?�?  �?  ├── languages.py      # 语言定义�?0+语言�?�?  �?  ├── scanner.py       # 文件扫描�?�?  �?  └── stats.py         # 统计数据结构
�?  �?�?  ├── exporters/           # 导出器模�?�?  �?  ├── __init__.py
�?  �?  ├── csv_exporter.py  # CSV格式导出
�?  �?  ├── json_exporter.py # JSON格式导出
�?  �?  └── markdown_exporter.py # Markdown导出
�?  �?�?  └── utils/              # 工具模块
�?      ├── __init__.py
�?      ├── config.py        # 配置管理
�?      ├── git_analyzer.py  # Git分析工具
�?      └── visualizer.py    # 可视化图�?�?├── tests/                   # 测试目录
�?  ├── __init__.py
�?  ├── README.md           # 测试说明文档
�?  ├── test_analyzer.py    # 分析器测试（待实现）
�?  ├── test_complexity.py  # 复杂度测试（待实现）
�?  ├── test_exporters.py   # 导出器测试（待实现）
�?  └── test_scanner.py     # 扫描器测试（待实现）
�?├── examples/                # 示例目录
�?  └── USAGE.md           # 详细使用指南
�?├── .gitignore              # Git忽略文件配置
├── LICENSE                 # MIT许可�?├── README.md               # 项目主文�?├── pyproject.toml          # Python项目配置
└── requirements.txt        # 依赖列表
```

## 模块说明

### core - 核心模块

#### analyzer.py
代码分析器，负责统计文件行数、代码行、注释行、空行�?
#### complexity.py
复杂度分析器，计算圈复杂�?CC)、函数和类数量�?
#### languages.py
语言注册表，支持30+种编程语言的文件识别和注释统计�?
#### scanner.py
文件扫描器，支持递归/非递归扫描，自动排除常见目录�?
#### stats.py
统计数据结构，包含FileStats、LanguageStats、ProjectStats等数据类�?
### exporters - 导出�?
#### json_exporter.py
将统计结果导出为JSON格式，包含完整数据�?
#### csv_exporter.py
将统计结果导出为CSV格式，支持详细和摘要两种模式�?
#### markdown_exporter.py
将统计结果导出为Markdown格式，生成美观的报告�?
### utils - 工具模块

#### config.py
配置文件管理，支持JSON和YAML格式配置�?
#### git_analyzer.py
Git集成工具，获取分支、远程仓库、贡献者等信息�?
#### visualizer.py
可视化工具，生成ASCII条形图和统计图表�?
## 文件统计

```
总文件数: 29
├── Python文件: 16�?├── Markdown文件: 3�?└── 配置文件: 3�?(.gitignore, LICENSE, pyproject.toml, requirements.txt)
```

## 依赖关系

```
__main__.py
├── core/
�?  ├── analyzer.py
�?  ├── scanner.py
�?  ├── complexity.py
�?  ├── languages.py
�?  └── stats.py
├── exporters/
�?  ├── json_exporter.py
�?  ├── csv_exporter.py
�?  └── markdown_exporter.py
└── utils/
    ├── config.py
    ├── git_analyzer.py
    └── visualizer.py
```

## 扩展�?
项目设计遵循模块化原则，方便扩展�?
- 添加新语言：在`languages.py`中注册新语言配置
- 添加新导出格式：在`exporters/`中添加新的Exporter�?- 添加新功能：在`utils/`中添加新的工具类
- 添加测试：在`tests/`中添加测试文�?
