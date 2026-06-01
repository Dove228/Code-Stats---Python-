# Code Stats 构建指南

## 快速开�?
### 运行方式

1. **双击运行**（推荐）
   ```bash
   双击 CodeStats.bat
   ```

2. **命令行运�?*
   ```bash
   python codestats_no_pathlib.py
   ```

3. **带参数运�?*
   ```bash
   python codestats_no_pathlib.py /path/to/project -v -o report.json
   ```

## 项目结构

```
code-stats/
├── codestats_no_pathlib.py  # 主程序（单文件版本）
├── CodeStats.bat           # 启动脚本
├── src/code_stats/         # 源代码目录（开发版�?├── examples/               # 使用示例
├── tests/                  # 测试目录
├── README.md               # 项目文档
├── LICENSE                 # MIT许可�?├── build.py                # 构建脚本
├── build.bat               # 批处理构建脚�?└── requirements.txt        # 依赖列表
```

## 构建说明

### 当前状�?
由于系统环境中存在旧�?`pathlib` 包冲突，PyInstaller 暂时无法使用�?
### 使用现有脚本

当前推荐使用 `codestats_no_pathlib.py`，该版本不依赖外部的 `pathlib` 包�?
### 手动打包（需要管理员权限�?
如果需要打包成独立 exe�?
```bash
# 以管理员身份运行命令提示�?
# 删除冲突的pathlib文件
del D:\Anaconda\Lib\site-packages\pathlib.py
rmdir D:\Anaconda\Lib\site-packages\pathlib-1.0.1.dist-info /s /q

# 安装PyInstaller
pip install pyinstaller

# 打包
pyinstaller --onefile --console --name CodeStats codestats_no_pathlib.py

# 移动生成的exe
move dist\CodeStats.exe .
```

## 依赖要求

- Python 3.8+
- 标准库即可运行（无需额外依赖�?
## 开发模�?
```bash
# 安装依赖（如果需要）
pip install -r requirements.txt

# 运行开发版
python -m code_stats
```

## 注意事项

1. **运行方式**：当前推荐使�?`CodeStats.bat` 或直接运�?`codestats_no_pathlib.py`
2. **环境要求**：需要安�?Python 3.8+
3. **打包限制**：由于系统环境限制，暂时无法打包成独�?exe
4. **源代�?*：完整源代码位于 `src/code_stats/` 目录

## 更多信息

- 项目文档：[README.md](README.md)
- 使用示例：[examples/USAGE.md](examples/USAGE.md)
- 项目结构：[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
