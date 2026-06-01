# Code Stats - Python 代码统计工具

一个功能强大的交互式代码统计工具，支持30+种编程语言的代码分析、复杂度分析、可视化报告和Git集成。

## ✨ 核心特性

### 🎯 交互式界面
- **数字键快捷选择**：按1-7快速选择功能
- **拖拽支持**：可直接拖拽文件夹到输入框
- **中文界面**：全中文提示，易于使用
- **无需安装**：双击即可运行

### 📊 统计功能
- **快速统计**：一键查看代码行数统计
- **详细统计**：显示完整的文件详情
- **复杂度分析**：圈复杂度(CC)、函数/类计数
- **Git统计**：分析提交、贡献者、文件历史
- **可视化图表**：ASCII图形显示分布
- **报告导出**：JSON/Markdown格式
- **完整分析**：一次性运行所有功能

### 🌐 支持语言
支持30+种编程语言，包括：
Python, JavaScript, TypeScript, Java, C/C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin, Scala, HTML, CSS, SQL, Shell等

## 🚀 安装使用

### 方法 1：双击运行（推荐）
```bash
# 双击运行启动脚本
CodeStats.bat
```

### 方法 2：命令行运行
```bash
# 基本用法
python codestats_no_pathlib.py /path/to/project

# 带参数
python codestats_no_pathlib.py /path/to/project -v -r --complexity
```

## 📁 项目结构
```
Code-Stats---Python-/
├── codestats_no_pathlib.py   # 主程序（单文件版本）
├── CodeStats.bat             # 启动脚本
├── build_scripts/            # 构建脚本
│   ├── build.bat
│   ├── build.py
│   └── BUILD_GUIDE.md
├── src/code_stats/           # 源代码目录
│   ├── core/                 # 核心模块
│   ├── exporters/            # 导出器
│   └── utils/                # 工具模块
├── examples/                 # 使用示例
└── tests/                    # 测试目录
```

## 📝 使用示例

```bash
# 快速统计当前目录
python codestats_no_pathlib.py .

# 递归统计并显示详细信息
python codestats_no_pathlib.py /path/to/project -r -v

# 分析复杂度
python codestats_no_pathlib.py . --complexity

# 导出报告
python codestats_no_pathlib.py . -o report.md
```

## 🔧 参数说明

| 参数 | 说明 |
|------|------|
| `-r`, `--recursive` | 递归扫描子目录 |
| `-v`, `--verbose` | 显示详细信息 |
| `--complexity` | 启用复杂度分析 |
| `--git` | 启用Git统计 |
| `--visualize` | 显示可视化图表 |
| `-o <file>` | 导出报告到文件 |
| `-e <dirs>` | 排除指定目录 |
| `--lang <langs>` | 只统计指定语言 |

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📧 联系方式

项目地址：https://github.com/Dove228/Code-Stats---Python-