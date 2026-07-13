# Sample Project - Code Stats Demo

这是一个用于演示 **Code Stats** 代码统计工具的示例项目，包含多种编程语言的代码文件。

## 📁 项目结构

```
sample_project/
├── python/
│   └── app.py              # Python示例代码
├── javascript/
│   └── app.js              # JavaScript示例代码
├── typescript/
│   └── app.ts              # TypeScript示例代码
├── java/
│   └── Calculator.java     # Java示例代码
├── c/
│   └── main.c              # C语言示例代码
├── cpp/
│   └── main.cpp            # C++示例代码
├── go/
│   └── main.go             # Go示例代码
├── rust/
│   └── main.rs             # Rust示例代码
├── csharp/
│   └── Program.cs          # C#示例代码
├── html/
│   └── index.html          # HTML示例代码
├── css/
│   └── styles.css          # CSS示例代码
├── sql/
│   └── schema.sql          # SQL示例代码
└── README.md               # 本文件
```

## 🚀 使用方法

### 1. 快速统计整个示例项目

```bash
# 使用交互式模式
python codestats_no_pathlib.py

# 然后选择功能并输入路径：sample_project
```

### 2. 命令行模式

```bash
# 统计整个示例项目
python codestats_no_pathlib.py sample_project -r -v

# 只统计Python文件
python codestats_no_pathlib.py sample_project --lang python

# 统计多种语言
python codestats_no_pathlib.py sample_project --lang python,javascript,java

# 显示复杂度分析
python codestats_no_pathlib.py sample_project --complexity

# 可视化图表
python codestats_no_pathlib.py sample_project --visualize

# 导出报告
python codestats_no_pathlib.py sample_project -o report.json
```

## 📊 实际统计结果

使用 `python codestats_no_pathlib.py sample_project -v` 得到的统计结果：

```
============================================================
代码统计报告 - sample_project
============================================================

【总体统计】
  总文件数:        13
  总代码行数:      629
  有效代码行数:    408
  注释行数:        133
  空行数:          88
  代码占比:        64.86%
  总文件大小:      14.33 KB

【按语言统计】
------------------------------------------------------------
语言              文件数      代码行        注释行        占比
------------------------------------------------------------
Markdown        1        95         0           23.28%
CSS             1        65         8           15.93%
HTML            1        42         0           10.29%
C#              1        30         14           7.35%
SQL             1        28         8            6.86%
C++             1        22         14           5.39%
Go              1        19         6            4.66%
Java            1        19         20           4.66%
JavaScript      1        19         23           4.66%
TypeScript      1        19         17           4.66%
Rust            1        18         6            4.41%
C               1        17         11           4.17%
Python          1        15         6            3.68%

============================================================
```

## 🔧 测试功能

你可以使用这个示例项目测试以下功能：

1. **快速统计** - 一键查看代码行数统计
2. **详细统计** - 显示每个文件的详细信息
3. **复杂度分析** - 查看代码圈复杂度
4. **可视化图表** - 以ASCII图表显示语言分布
5. **报告导出** - 导出JSON/Markdown报告

## 📝 示例代码内容

每个示例文件都实现了一个简单的计算器类，包含：
- `add` 方法 - 加法运算
- `multiply` 方法 - 乘法运算
- 主函数 - 演示使用

## 🔗 项目地址

GitHub: https://github.com/Dove228/Code-Stats---Python-