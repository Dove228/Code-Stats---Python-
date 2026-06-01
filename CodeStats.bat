@echo off
chcp 936 >nul
cd /d "%~dp0"

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║          Code Stats - 代码统计工具                          ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo   📁 请输入要统计的文件夹路径
echo   💡 提示：可以直接拖拽文件夹到此处
echo   → 直接输入路径或拖拽文件夹
echo.

python codestats_no_pathlib.py %*