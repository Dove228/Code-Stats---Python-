# Code Stats - Python 代码统计工具

一个功能强大的交互式代码统计工具，支持30+种编程语言的代码分析、复杂度分析、可视化报告和Git集成。

## ✨ 核心特性

### 🚀 交互式界面
- **数字键快捷选择**：按1-7快速选择功能
- **拖拽支持**：可直接拖拽文件夹到输入框
- **中文字符界面**：全中文提示，易于使用
- **无需命令行**：双击即可运行

### 📊 统计功能
- **快速统计**：一键查看代码行数统计
- **详细统计**：显示完整的文件详情
- **复杂度分析**：圈复杂度(CC)、函数/类计数
- **Git统计**：分支、贡献者、提交历史
- **可视化图表**：ASCII条形图展示分布
- **报告导出**：JSON/Markdown格式
- **完整分析**：一次运行包含所有功能

### 🌐 支持语言
支持30+种编程语言，包括：
Python, JavaScript, TypeScript, Java, C/C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin, Scala, HTML, CSS, SQL, Shell等

## 📦 安装使用

### 方法 1：双击运行（推荐）

1. **运行**
   ```bash
   # 双击运行批处理文件
   CodeStats.bat
   ```

2. **使用**
   - 程序启动后显示菜单
   - 按数字键选择功能（1-7）
   - 输入要统计的文件夹路径

### 方法 2：命令行模式

```bash
# 基本统计
python codestats_no_pathlib.py C:\path\to\project

# 详细模式
python codestats_no_pathlib.py C:\path\to\project -v

# 导出报告
python codestats_no_pathlib.py C:\path\to\project -o report.json
```

### 方法 3：开发模式

```bash
# 运行测试脚本
python test_run.py
```

## 🎮 使用说明

### 交互模式

运行程序后，会显示主菜单：

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

### 功能说明

| 按键 | 功能 | 说明 |
|------|------|------|
| `1` | 快速统计 | 基础统计信息 |
| `2` | 详细统计 | 包含文件详情列表 |
| `3` | 复杂度分析 | 圈复杂度统计 |
| `4` | Git统计 | 仓库信息（需要Git仓库） |
| `5` | 可视化图表 | ASCII条形图 |
| `6` | 导出报告 | JSON/Markdown格式 |
| `7` | 完整分析 | 所有功能一次运行 |
| `0` | 退出 | 关闭程序 |

## 📁 项目文件

```
code-stats/
├── codestats_no_pathlib.py  # 主程序（不使用pathlib）
├── CodeStats.bat           # 启动批处理文件
├── codestats_single.py     # 单文件版本（使用pathlib）
├── src/code_stats/         # 源代码目录
├── test_run.py             # 测试脚本
├── build.py                # 打包脚本
├── build.bat               # 构建脚本
└── README.md               # 项目文档
```

## 🛠️ 打包说明

### 当前状态

由于系统环境中存在旧版pathlib包冲突，PyInstaller暂时无法使用。

### 解决方案

1. **使用现有脚本**（推荐）
   - `codestats_no_pathlib.py` 已移除pathlib依赖
   - 双击 `CodeStats.bat` 即可运行
   - 需要安装Python 3.8+

2. **手动打包（需要管理员权限）**
   ```bash
   # 需要先以管理员身份删除冲突文件：
   # del D:\Anaconda\Lib\site-packages\pathlib.py
   # rmdir D:\Anaconda\Lib\site-packages\pathlib-1.0.1.dist-info /s /q
   
   # 然后运行打包脚本
   python build.py
   ```

## 📊 示例输出

```
正在分析: C:\Users\Example\Project

============================================================
代码统计报告 - C:\Users\Example\Project
============================================================

【总体统计】
  总文件数:        31
  总代码行数:      2233
  有效代码行数:    1990
  注释行数:        96
  空行数:          147
  代码占比:        89.12%
  总文件大小:      52.20 KB

【按语言统计】
------------------------------------------------------------
语言              文件数      代码行        注释行        占比
------------------------------------------------------------
C++             31       1990       96         100.00%
------------------------------------------------------------
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 👤 作者

Dove228

## 🔗 相关链接

- GitHub仓库: https://github.com/Dove228/first_try
- 问题反馈: https://github.com/Dove228/first_try/issues
