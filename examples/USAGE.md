# 使用指南 - Usage Guide

## 🚀 快速开始

### 方法1：交互式运行

```bash
# 双击运行
CodeStats.bat

# 或命令行
python codestats_no_pathlib.py
```

运行后会显示主菜单：

```
============================================================
      Code Stats - 代码统计工具
============================================================

  请选择功能：

    [1] 快速统计       - 快速扫描并显示基础统计信息
    [2] 详细统计       - 显示详细信息和文件详情
    [3] 复杂度分析     - 显示代码圈复杂度分析
    [4] Git统计        - 显示Git仓库信息
    [5] 可视化图表     - 以ASCII图表显示统计结果
    [6] 导出报告       - 将结果导出为JSON/Markdown
    [7] 完整分析       - 包含所有高级功能
    [0] 退出程序       - 退出

  请输入选项:
```

### 方法2：命令行模式

```bash
# 基本用法
python codestats_no_pathlib.py /path/to/project

# 递归扫描
python codestats_no_pathlib.py /path/to/project -r

# 详细输出
python codestats_no_pathlib.py /path/to/project -v

# 组合使用
python codestats_no_pathlib.py /path/to/project -r -v --complexity --git
```

## 📊 功能详解

### 1. 快速统计

```bash
python codestats_no_pathlib.py /path/to/project -r
```

输出示例：
```
┌─────────────────────────────────────────────┐
│          代码统计结果                        │
├─────────────────────────────────────────────┤
│ 总文件数:        42                         │
│ 总代码行数:      8,523                      │
│ 有效代码行数:    7,128                      │
│ 注释行数:        834                        │
│ 空行数:          561                        │
│ 代码占比:        83.6%                      │
└─────────────────────────────────────────────┘
```

### 2. 详细统计

```bash
python codestats_no_pathlib.py /path/to/project -r -v
```

输出包含每个文件的详细信息。

### 3. 复杂度分析

```bash
python codestats_no_pathlib.py /path/to/project --complexity
```

输出示例：
```
┌─────────────────────────────────────────────┐
│          复杂度分析结果                      │
├─────────────────────────────────────────────┤
│ 文件               CC    函数  类            │
├─────────────────────────────────────────────┤
│ main.py           24      8    2           │
│ utils.py          12      5    1           │
│ total             36     13    3           │
└─────────────────────────────────────────────┘
```

### 4. Git统计

```bash
python codestats_no_pathlib.py /path/to/project --git
```

输出示例：
```
┌─────────────────────────────────────────────┐
│          Git仓库统计                        │
├─────────────────────────────────────────────┤
│ 当前分支:        main                       │
│ 远程仓库:        origin                     │
│ 提交次数:        28                         │
│ 贡献者:          3                          │
│ 最近提交:        2024-01-15                │
└─────────────────────────────────────────────┘
```

### 5. 可视化图表

```bash
python codestats_no_pathlib.py /path/to/project --visualize
```

输出示例：
```
┌─────────────────────────────────────────────┐
│          语言分布图表                      │
├─────────────────────────────────────────────┤
│ Python    ████████████████████  4,234行    │
│ JavaScript██████████            2,156行    │
│ HTML      ████                  892行      │
│ CSS       ██                    423行      │
└─────────────────────────────────────────────┘
```

### 6. 导出报告

```bash
# 导出JSON
python codestats_no_pathlib.py /path/to/project -o report.json

# 导出Markdown
python codestats_no_pathlib.py /path/to/project -o report.md

# 导出CSV
python codestats_no_pathlib.py /path/to/project -o report.csv
```

### 7. 完整分析

```bash
python codestats_no_pathlib.py /path/to/project --full
```

一次性运行所有功能并生成完整报告。

## 🔧 参数说明

| 参数 | 简写 | 说明 |
|------|------|------|
| `--recursive` | `-r` | 递归扫描子目录 |
| `--verbose` | `-v` | 显示详细信息 |
| `--complexity` | | 启用复杂度分析 |
| `--git` | | 启用Git统计 |
| `--visualize` | | 显示可视化图表 |
| `--full` | | 完整分析（所有功能） |
| `--output <file>` | `-o` | 导出报告到文件 |
| `--exclude <dirs>` | `-e` | 排除指定目录 |
| `--lang <langs>` | | 只统计指定语言 |
| `--help` | `-h` | 显示帮助信息 |

## 📁 目录排除

```bash
# 排除单个目录
python codestats_no_pathlib.py . -e node_modules

# 排除多个目录
python codestats_no_pathlib.py . -e node_modules,dist,build

# 使用逗号分隔
python codestats_no_pathlib.py . -e "__pycache__,*.pyc"
```

## 🌐 语言过滤

```bash
# 只统计Python文件
python codestats_no_pathlib.py . --lang python

# 统计多种语言
python codestats_no_pathlib.py . --lang python,js,html

# 语言代码参考
# python, javascript, typescript, java, c, cpp, csharp, go, rust, ruby, php, swift, kotlin, scala, html, css, sql, shell
```

## 📝 实用技巧

### 技巧1：拖拽文件夹

在交互式模式下，可以直接将文件夹拖拽到命令行窗口，自动填充路径。

### 技巧2：快速统计当前目录

```bash
python codestats_no_pathlib.py .
```

### 技巧3：批量统计

```bash
# 统计多个目录
python codestats_no_pathlib.py dir1 dir2 dir3

# 使用通配符
python codestats_no_pathlib.py src/*
```

### 技巧4：保存报告

```bash
# 保存到文件
python codestats_no_pathlib.py . -r -o report.json

# 同时显示和保存
python codestats_no_pathlib.py . -r -v | tee output.txt
```

## 🔍 常见问题

### Q: 为什么统计结果不包含某些文件？

**A:** 工具会自动排除：
- 二进制文件（.exe, .dll, .zip, .pdf等）
- 隐藏文件和目录（以.开头）
- 临时文件和缓存目录

### Q: 如何统计特定类型的文件？

**A:** 使用 `--lang` 参数指定语言：
```bash
python codestats_no_pathlib.py . --lang python
```

### Q: 如何排除目录？

**A:** 使用 `-e` 参数：
```bash
python codestats_no_pathlib.py . -e node_modules,__pycache__
```

### Q: 支持哪些语言？

**A:** 支持30+种编程语言，包括Python, JavaScript, Java, C/C++, C#, Go, Rust, Ruby, PHP等。

## 🔗 项目地址

GitHub: https://github.com/Dove228/Code-Stats---Python-