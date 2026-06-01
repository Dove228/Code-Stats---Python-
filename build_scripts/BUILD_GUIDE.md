# 构建指南 - Build Guide

## 📦 构建说明

本项目支持多种方式运行和构建。

## 🚀 运行方式

### 方式1：直接运行（推荐）

```bash
# 双击运行启动脚本
CodeStats.bat

# 或使用命令行
python codestats_no_pathlib.py
```

### 方式2：使用模块方式

```bash
cd d:\Project\01
python -m code_stats
```

### 方式3：命令行模式

```bash
# 统计指定目录
python codestats_no_pathlib.py /path/to/project

# 带参数运行
python codestats_no_pathlib.py /path/to/project -r -v --complexity
```

## 📁 构建脚本说明

### build.bat

批处理构建脚本，用于创建启动脚本和清理旧文件。

**功能：**
- 清理旧的可执行文件
- 创建启动脚本 `CodeStats.bat`
- 显示构建完成信息

**运行方式：**
```bash
build.bat
```

### build.py

Python构建脚本，提供更强大的构建功能。

**功能：**
- 清理旧构建产物
- 创建启动脚本
- 支持PyInstaller打包（需安装PyInstaller）
- 生成发布包

**运行方式：**
```bash
python build.py
```

## 📦 使用PyInstaller打包

### 安装PyInstaller

```bash
pip install pyinstaller
```

### 打包命令

```bash
# 基本打包
pyinstaller --onefile --console codestats_no_pathlib.py

# 指定输出名称
pyinstaller --onefile --console --name CodeStats codestats_no_pathlib.py

# 使用spec文件
pyinstaller code_stats.spec
```

### 注意事项

⚠️ **当前已知问题**：
- 由于系统环境中存在旧版 `pathlib` 包冲突，PyInstaller可能无法正常工作
- 建议使用 `CodeStats.bat` 方式运行

### 解决冲突

如果需要打包成exe，可以尝试删除冲突文件：

```bash
del D:\Anaconda\Lib\site-packages\pathlib.py
rmdir D:\Anaconda\Lib\site-packages\pathlib-1.0.1.dist-info /s /q
```

## 📁 构建产物

| 文件 | 说明 |
|------|------|
| `CodeStats.bat` | 启动脚本 |
| `codestats_no_pathlib.py` | 主程序 |
| `dist/CodeStats.exe` | 打包后的可执行文件（可选） |

## 🔧 环境要求

| 项目 | 要求 |
|------|------|
| Python | 3.8+ |
| 操作系统 | Windows/Linux/macOS |
| 依赖 | 标准库（无需额外安装） |

## 📝 常见问题

### Q: 运行时提示找不到Python？

**A:** 确保Python已添加到系统PATH，或使用完整路径：
```bash
"C:\Program Files\Python39\python.exe" codestats_no_pathlib.py
```

### Q: 如何打包成独立exe？

**A:** 参见上面的PyInstaller打包说明。如果遇到pathlib冲突，需要先解决冲突。

### Q: 如何在其他电脑上使用？

**A:** 复制以下文件到目标电脑即可：
- `codestats_no_pathlib.py`
- `CodeStats.bat`

确保目标电脑已安装Python 3.8+。

## 🔗 项目地址

GitHub: https://github.com/Dove228/Code-Stats---Python-