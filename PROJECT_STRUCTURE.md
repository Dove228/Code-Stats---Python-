# Code Stats 项目结构

## 📁 项目目录结构

```
Code-Stats---Python-/
├── codestats_no_pathlib.py   # 主程序（单文件版本）
├── CodeStats.bat             # 启动脚本（双击运行）
├── .gitignore               # Git忽略配置
├── LICENSE                  # MIT许可证
├── pyproject.toml           # 项目配置
├── requirements.txt         # 依赖列表
├── README.md                # 项目主文档
├── PROJECT_STRUCTURE.md     # 项目结构文档
├── build_scripts/           # 打包脚本目录
│   ├── build.bat            # 批处理构建脚本
│   ├── build.py             # Python构建脚本
│   └── BUILD_GUIDE.md       # 构建指南
├── examples/                # 使用示例
│   └── USAGE.md             # 使用说明文档
├── src/                     # 源代码目录
│   └── code_stats/          # 主包
│       ├── __init__.py      # 包初始化
│       ├── __main__.py      # CLI入口
│       ├── core/            # 核心模块
│       │   ├── __init__.py
│       │   ├── analyzer.py   # 代码分析器
│       │   ├── complexity.py # 复杂度分析
│       │   ├── languages.py  # 语言定义
│       │   └── scanner.py    # 文件扫描器
│       ├── exporters/       # 导出器模块
│       │   ├── __init__.py
│       │   ├── json_exporter.py   # JSON导出器
│       │   ├── csv_exporter.py    # CSV导出器
│       │   └── markdown_exporter.py # Markdown导出器
│       └── utils/           # 工具模块
│           ├── __init__.py
│           ├── config.py      # 配置管理
│           ├── git_analyzer.py # Git分析
│           ├── interactive.py # 交互式界面
│           └── visualizer.py  # 可视化图表
└── tests/                   # 测试目录
    ├── __init__.py
    └── README.md            # 测试说明
```

## 🔗 模块依赖关系

```
┌──────────────────────────────────────────────────────────┐
│                     __main__.py (CLI入口)                 │
└──────────────────────────┬───────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  scanner.py   │   │  analyzer.py  │   │ complexity.py │
│  (文件扫描)   │   │  (代码分析)   │   │  (复杂度分析) │
└───────────────┘   └───────┬───────┘   └───────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ languages.py  │
                    │  (语言定义)   │
                    └───────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  json_export  │   │  csv_export   │   │md_export     │
│  (JSON导出)   │   │  (CSV导出)    │   │ (Markdown导出)│
└───────────────┘   └───────────────┘   └───────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  config.py    │   │git_analyzer.py│   │visualizer.py │
│  (配置管理)   │   │  (Git分析)   │   │  (可视化)    │
└───────────────┘   └───────────────┘   └───────────────┘
```

## 🎯 核心模块说明

### core/ - 核心模块

| 文件 | 说明 |
|------|------|
| `analyzer.py` | 代码分析器，统计代码行、注释行、空行 |
| `complexity.py` | 复杂度分析，计算圈复杂度 |
| `languages.py` | 语言定义，支持30+种编程语言 |
| `scanner.py` | 文件扫描器，递归扫描目录 |

### exporters/ - 导出器

| 文件 | 说明 |
|------|------|
| `json_exporter.py` | 导出JSON格式报告 |
| `csv_exporter.py` | 导出CSV格式报告 |
| `markdown_exporter.py` | 导出Markdown格式报告 |

### utils/ - 工具模块

| 文件 | 说明 |
|------|------|
| `config.py` | 配置文件管理 |
| `git_analyzer.py` | Git仓库分析 |
| `interactive.py` | 交互式界面 |
| `visualizer.py` | ASCII图表可视化 |

## 📊 项目统计

| 项目 | 数量 |
|------|------|
| Python文件 | 17个 |
| Markdown文档 | 5个 |
| 支持语言 | 30+种 |
| 核心模块 | 4个 |
| 导出器 | 3个 |
| 工具模块 | 4个 |

## 🔗 项目地址

GitHub: https://github.com/Dove228/Code-Stats---Python-