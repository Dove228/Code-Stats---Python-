import os
import sys
from pathlib import Path
from typing import Optional


class InteractiveCLI:
    def __init__(self):
        self.title = "╔══════════════════════════════════════════════════════════════╗"
        self.title2 = "║          Code Stats - 代码统计工具 v1.0                      ║"
        self.footer = "╚══════════════════════════════════════════════════════════════╝"
        
        self.options = {
            "1": ("快速统计", "快速扫描并显示基础统计信息"),
            "2": ("详细统计", "显示详细信息和文件详情"),
            "3": ("复杂度分析", "显示代码圈复杂度分析"),
            "4": ("Git统计", "显示Git仓库信息（需在Git仓库中使用）"),
            "5": ("可视化图表", "以ASCII图表显示统计结果"),
            "6": ("导出报告", "将结果导出为JSON/CSV/Markdown"),
            "7": ("完整分析", "包含所有高级功能的完整统计"),
            "0": ("退出程序", "退出Code Stats"),
        }
        
        self.export_formats = {
            "1": ("JSON", "json"),
            "2": ("CSV", "csv"),
            "3": ("Markdown", "md"),
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        self.clear_screen()
        print("\n")
        print(self.title)
        print(self.title2)
        print(self.footer)
        print()
    
    def print_menu(self):
        print("  请选择功能：\n")
        for key, (name, desc) in self.options.items():
            print(f"    [{key}] {name:<12} - {desc}")
        print()
    
    def get_choice(self, max_choice: str = "9") -> str:
        while True:
            choice = input("  请输入选项: ").strip()
            if choice in [str(i) for i in range(int(max_choice) + 1)]:
                return choice
            print(f"  ⚠️  无效选项，请输入 0-{max_choice}")
    
    def get_path_input(self) -> Optional[Path]:
        print("\n  " + "─" * 60)
        print("  📁 请输入要统计的文件夹路径")
        print("  💡 提示：可以直接拖拽文件夹到此处")
        print("  " + "─" * 60)
        
        path_input = input("\n  路径: ").strip().strip('"').strip("'")
        
        if not path_input:
            print("\n  ❌ 路径不能为空")
            return None
        
        path = Path(path_input)
        
        if not path.exists():
            print(f"\n  ❌ 路径不存在: {path}")
            return None
        
        if not path.is_dir():
            print(f"\n  ❌ 路径不是目录: {path}")
            return None
        
        return path.resolve()
    
    def ask_exclude_dirs(self) -> Optional[str]:
        print("\n  " + "─" * 60)
        print("  🚫 排除目录（可选）")
        print("  💡 多个目录用逗号分隔，留空跳过")
        print("  " + "─" * 60)
        
        exclude_input = input("\n  排除目录: ").strip()
        
        if exclude_input:
            return exclude_input
        return None
    
    def ask_language_filter(self) -> Optional[str]:
        print("\n  " + "─" * 60)
        print("  🔍 语言过滤（可选）")
        print("  💡 例如: python, javascript, cpp")
        print("  💡 留空则统计所有支持的语言")
        print("  " + "─" * 60)
        
        lang_input = input("\n  语言: ").strip()
        
        if lang_input:
            return lang_input
        return None
    
    def ask_export_format(self) -> str:
        print("\n  " + "─" * 60)
        print("  📄 选择导出格式")
        print("  " + "─" * 60)
        print()
        
        for key, (name, ext) in self.export_formats.items():
            print(f"    [{key}] {name}")
        print()
        
        choice = self.get_choice("3")
        return self.export_formats[choice][1]
    
    def ask_output_path(self, default_name: str) -> Path:
        print("\n  " + "─" * 60)
        print("  💾 输出路径（可选）")
        print(f"  💡 留空则保存在当前目录: {default_name}")
        print("  " + "─" * 60)
        
        path_input = input(f"\n  路径: ").strip().strip('"').strip("'")
        
        if path_input:
            return Path(path_input)
        else:
            return Path.cwd() / default_name
    
    def confirm_action(self, action: str) -> bool:
        print(f"\n  确认 {action}? [y/N]: ", end="")
        choice = input().strip().lower()
        return choice == 'y'
    
    def print_result(self, stats_text: str):
        print("\n")
        print("─" * 70)
        print(stats_text)
        print("─" * 70)
        input("\n  按Enter键继续...")
    
    def print_error(self, error_msg: str):
        print(f"\n  ❌ 错误: {error_msg}")
        input("\n  按Enter键继续...")
    
    def print_success(self, success_msg: str):
        print(f"\n  ✅ {success_msg}")
        input("\n  按Enter键继续...")
    
    def print_header(self, text: str):
        print(f"\n  {text}")
        print("  " + "─" * 60)
    
    def run(self):
        while True:
            self.print_banner()
            self.print_menu()
            
            choice = self.get_choice()
            
            if choice == "0":
                print("\n  👋 感谢使用 Code Stats，再见！\n")
                break
            
            # 获取路径
            target_path = self.get_path_input()
            if not target_path:
                continue
            
            # 获取额外选项
            exclude_dirs = self.ask_exclude_dirs()
            lang_filter = self.ask_language_filter()
            
            # 构建选项
            options = {
                "path": str(target_path),
                "choice": choice,
                "exclude": exclude_dirs,
                "lang": lang_filter,
            }
            
            yield options
    
    def get_menu_options(self, choice: str) -> dict:
        """返回当前选择的选项描述"""
        if choice in self.options:
            return {
                "name": self.options[choice][0],
                "desc": self.options[choice][1]
            }
        return {"name": "未知", "desc": ""}
