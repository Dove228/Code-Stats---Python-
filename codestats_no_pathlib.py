#!/usr/bin/env python3
"""
Code Stats - Single file version (no pathlib dependency)
"""

import argparse
import json
import os
import sys
import subprocess


class FileStats:
    def __init__(self, filepath, filename, language, total_lines, code_lines, comment_lines, blank_lines, file_size):
        self.filepath = filepath
        self.filename = filename
        self.language = language
        self.total_lines = total_lines
        self.code_lines = code_lines
        self.comment_lines = comment_lines
        self.blank_lines = blank_lines
        self.file_size = file_size

    def to_dict(self):
        return {
            "filepath": self.filepath,
            "filename": self.filename,
            "language": self.language,
            "total_lines": self.total_lines,
            "code_lines": self.code_lines,
            "comment_lines": self.comment_lines,
            "blank_lines": self.blank_lines,
            "file_size": self.file_size,
        }


class LanguageStats:
    def __init__(self):
        self.files_count = 0
        self.total_lines = 0
        self.code_lines = 0
        self.comment_lines = 0
        self.blank_lines = 0

    def add_file(self, file_stats):
        self.files_count += 1
        self.total_lines += file_stats.total_lines
        self.code_lines += file_stats.code_lines
        self.comment_lines += file_stats.comment_lines
        self.blank_lines += file_stats.blank_lines

    def to_dict(self):
        return {
            "files_count": self.files_count,
            "total_lines": self.total_lines,
            "code_lines": self.code_lines,
            "comment_lines": self.comment_lines,
            "blank_lines": self.blank_lines,
        }


class ProjectStats:
    def __init__(self, root_path):
        self.root_path = root_path
        self.file_stats = []
        self.language_stats = {}

    def add_file_stats(self, file_stats):
        self.file_stats.append(file_stats)
        
        if file_stats.language not in self.language_stats:
            self.language_stats[file_stats.language] = LanguageStats()
        self.language_stats[file_stats.language].add_file(file_stats)

    @property
    def total_files(self):
        return len(self.file_stats)

    @property
    def total_lines(self):
        return sum(f.total_lines for f in self.file_stats)

    @property
    def total_code_lines(self):
        return sum(f.code_lines for f in self.file_stats)

    @property
    def total_comment_lines(self):
        return sum(f.comment_lines for f in self.file_stats)

    @property
    def total_blank_lines(self):
        return sum(f.blank_lines for f in self.file_stats)

    @property
    def total_file_size(self):
        return sum(f.file_size for f in self.file_stats)

    @property
    def code_percentage(self):
        if self.total_lines > 0:
            return (self.total_code_lines / self.total_lines) * 100
        return 0.0

    def to_dict(self):
        return {
            "root_path": self.root_path,
            "total_files": self.total_files,
            "total_lines": self.total_lines,
            "total_code_lines": self.total_code_lines,
            "total_comment_lines": self.total_comment_lines,
            "total_blank_lines": self.total_blank_lines,
            "total_file_size": self.total_file_size,
            "code_percentage": self.code_percentage,
            "language_stats": {k: v.to_dict() for k, v in self.language_stats.items()},
            "file_stats": [f.to_dict() for f in self.file_stats],
        }


LANGUAGE_EXTENSIONS = {
    ".py": "Python", ".pyw": "Python",
    ".js": "JavaScript", ".jsx": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript",
    ".java": "Java",
    ".c": "C", ".h": "C",
    ".cpp": "C++", ".hpp": "C++", ".cc": "C++", ".cxx": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".php": "PHP",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".scala": "Scala",
    ".html": "HTML", ".htm": "HTML",
    ".css": "CSS", ".scss": "CSS",
    ".sql": "SQL",
    ".sh": "Shell", ".bash": "Shell",
    ".ps1": "PowerShell",
    ".yml": "YAML", ".yaml": "YAML",
    ".json": "JSON",
    ".md": "Markdown",
    ".lua": "Lua",
    ".pl": "Perl",
    ".r": "R",
    ".hs": "Haskell",
    ".m": "MATLAB",
    ".dart": "Dart",
    ".vue": "Vue",
    ".svelte": "Svelte",
}

COMMENT_PATTERNS = {
    "Python": {"single": "#", "multi_start": '"""', "multi_end": '"""', "multi_alt": ("'''", "'''")},
    "JavaScript": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "TypeScript": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Java": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "C": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "C++": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "C#": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Go": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Rust": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Ruby": {"single": "#", "multi_start": "=begin", "multi_end": "=end"},
    "PHP": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Swift": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Kotlin": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Scala": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "HTML": {"single": None, "multi_start": "<!--", "multi_end": "-->"},
    "CSS": {"single": None, "multi_start": "/*", "multi_end": "*/"},
    "SQL": {"single": "--", "multi_start": "/*", "multi_end": "*/"},
    "Shell": {"single": "#"},
    "PowerShell": {"single": "#"},
    "YAML": {"single": "#"},
    "JSON": {"single": None},
    "Markdown": {"single": None},
    "Lua": {"single": "--", "multi_start": "--[[", "multi_end": "]]"},
    "Perl": {"single": "#"},
    "R": {"single": "#"},
    "Haskell": {"single": "--", "multi_start": "{-", "multi_end": "-}"},
    "MATLAB": {"single": "%"},
    "Dart": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Vue": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
    "Svelte": {"single": "//", "multi_start": "/*", "multi_end": "*/"},
}


def get_language_name(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    return LANGUAGE_EXTENSIONS.get(ext, "Unknown")


def should_exclude_dir(dir_name, exclude_dirs):
    dir_lower = dir_name.lower()
    for exclude in exclude_dirs:
        exclude_lower = exclude.lower()
        if exclude_lower in dir_lower or dir_lower == exclude_lower:
            return True
    return False


def is_binary_extension(file_path):
    binary_exts = {
        ".exe", ".dll", ".so", ".dylib", ".a", ".lib", ".o", ".obj",
        ".pyc", ".pyo", ".pyd", ".whl", ".egg",
        ".zip", ".tar", ".gz", ".7z", ".rar",
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".svg",
        ".mp3", ".mp4", ".wav", ".avi", ".mov", ".mkv",
        ".db", ".sqlite", ".sqlite3",
        ".class", ".jar", ".war", ".ear",
    }
    ext = os.path.splitext(file_path)[1].lower()
    return ext in binary_exts


def scan_directory(root_path, recursive=True, exclude_dirs=None, include_only=None):
    files = []
    exclude_set = exclude_dirs or {
        ".git", ".svn", ".hg", "__pycache__", "node_modules",
        "venv", "env", ".venv", ".env", "build", "dist",
        ".idea", ".vscode", ".vs", "target", "bin", "obj",
    }
    
    try:
        if recursive:
            for dirpath, dirnames, filenames in os.walk(root_path):
                dirnames[:] = [d for d in dirnames if not should_exclude_dir(d, exclude_set)]
                
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    
                    if is_binary_extension(filepath):
                        continue
                    
                    if include_only:
                        ext = os.path.splitext(filepath)[1].lower()
                        if ext not in include_only:
                            continue
                    
                    files.append(filepath)
        else:
            for filename in os.listdir(root_path):
                filepath = os.path.join(root_path, filename)
                if os.path.isfile(filepath) and not is_binary_extension(filepath):
                    files.append(filepath)
    except Exception:
        pass
    
    return sorted(files)


def analyze_file(file_path):
    language = get_language_name(file_path)
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except:
        return FileStats(file_path, os.path.basename(file_path), language, 0, 0, 0, 0, 0)

    lines = content.split("\n")
    total_lines = len(lines)
    code_lines = 0
    comment_lines = 0
    blank_lines = 0
    in_multi_comment = False
    
    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            blank_lines += 1
            continue
        
        patterns = COMMENT_PATTERNS.get(language, {})
        single_comment = patterns.get("single")
        multi_start = patterns.get("multi_start")
        multi_end = patterns.get("multi_end")
        
        if multi_start and multi_end:
            if not in_multi_comment:
                if stripped.startswith(multi_start):
                    if stripped.endswith(multi_end) and stripped != multi_start:
                        comment_lines += 1
                    else:
                        in_multi_comment = True
                        comment_lines += 1
                elif single_comment and stripped.startswith(single_comment):
                    comment_lines += 1
                else:
                    code_lines += 1
            else:
                comment_lines += 1
                if multi_end in stripped:
                    in_multi_comment = False
        elif single_comment:
            if stripped.startswith(single_comment):
                comment_lines += 1
            else:
                code_lines += 1
        else:
            code_lines += 1
    
    try:
        file_size = os.path.getsize(file_path)
    except:
        file_size = 0

    return FileStats(
        file_path, os.path.basename(file_path), language,
        total_lines, code_lines, comment_lines, blank_lines, file_size
    )


def analyze_project(root_path, recursive=True, exclude_dirs=None):
    project_stats = ProjectStats(root_path)
    files = scan_directory(root_path, recursive, exclude_dirs)
    
    for filepath in files:
        file_stats = analyze_file(filepath)
        project_stats.add_file_stats(file_stats)
    
    return project_stats


class JSONExporter:
    def __init__(self, stats):
        self.stats = stats
    
    def export(self, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.stats.to_dict(), f, indent=2, ensure_ascii=False)


class MarkdownExporter:
    def __init__(self, stats):
        self.stats = stats
    
    def export(self, output_path):
        content = self.generate_report()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    
    def generate_report(self):
        lines = []
        lines.append("# Code Statistics Report")
        lines.append("")
        lines.append(f"**Project Path:** `{self.stats.root_path}`")
        lines.append("")
        
        lines.append("## Summary")
        lines.append("")
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        lines.append(f"| Total Files | {self.stats.total_files} |")
        lines.append(f"| Total Lines | {self.stats.total_lines} |")
        lines.append(f"| Code Lines | {self.stats.total_code_lines} |")
        lines.append(f"| Comment Lines | {self.stats.total_comment_lines} |")
        lines.append(f"| Blank Lines | {self.stats.total_blank_lines} |")
        lines.append(f"| Code Percentage | {self.stats.code_percentage:.2f}% |")
        lines.append("")
        
        if self.stats.language_stats:
            lines.append("## Statistics by Language")
            lines.append("")
            lines.append("| Language | Files | Code Lines | Percentage |")
            lines.append("|----------|-------|------------|------------|")
            for lang, lang_stats in sorted(self.stats.language_stats.items(), key=lambda x: x[1].code_lines, reverse=True):
                percentage = (lang_stats.code_lines / self.stats.total_code_lines * 100) if self.stats.total_code_lines > 0 else 0
                lines.append(f"| {lang} | {lang_stats.files_count} | {lang_stats.code_lines} | {percentage:.2f}% |")
            lines.append("")
        
        return "\n".join(lines)


class Visualizer:
    def __init__(self, stats):
        self.stats = stats
    
    def generate_summary_visualization(self):
        lines = []
        lines.append("CODE STATISTICS VISUALIZATION")
        lines.append("=" * 70)
        lines.append("")
        
        data = {lang: stats.code_lines for lang, stats in self.stats.language_stats.items()}
        if data:
            max_val = max(data.values())
            lines.append("Code Lines by Language")
            lines.append("")
            for lang, val in sorted(data.items(), key=lambda x: x[1], reverse=True):
                bar_len = int((val / max_val) * 50)
                bar = "█" * bar_len
                percentage = (val / sum(data.values())) * 100
                lines.append(f"{lang:<15} {bar:<50} {val:>8} ({percentage:>5.1f}%)")
        
        lines.append("")
        lines.append("=" * 70)
        return "\n".join(lines)


class GitAnalyzer:
    def __init__(self, repo_path):
        self.repo_path = repo_path
    
    def _run_git(self, args):
        try:
            result = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=self.repo_path)
            if result.returncode == 0:
                return result.stdout
        except:
            pass
        return None
    
    def is_git_repo(self):
        return os.path.exists(os.path.join(self.repo_path, ".git"))
    
    def get_current_branch(self):
        output = self._run_git(["branch", "--show-current"])
        return output.strip() if output else None
    
    def get_commit_stats_by_author(self):
        output = self._run_git(["log", "--max-count=100", "--pretty=format:%H|%an|%ad|%s", "--date=short", "--numstat"])
        if not output:
            return {}
        
        author_stats = {}
        for line in output.split("\n"):
            if "|" in line:
                parts = line.split("|")
                if len(parts) >= 2:
                    author = parts[1]
                    if author not in author_stats:
                        author_stats[author] = {"commits": 0, "lines_added": 0, "lines_deleted": 0}
                    author_stats[author]["commits"] += 1
        return author_stats


class ComplexityAnalyzer:
    def analyze_files(self, files, languages):
        results = []
        for filepath, language in zip(files, languages):
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                lines = content.split("\n")
                complexity = 1
                func_count = 0
                class_count = 0
                
                for line in lines:
                    stripped = line.strip()
                    if not stripped:
                        continue
                    
                    keywords = ["if", "elif", "for", "while", "and", "or", "try", "except"]
                    for kw in keywords:
                        if kw in stripped.lower():
                            complexity += 1
                    
                    if "def " in stripped or "function " in stripped or "fn " in stripped:
                        func_count += 1
                    if "class " in stripped:
                        class_count += 1
                
                results.append({
                    "path": filepath,
                    "language": language,
                    "cyclomatic_complexity": complexity,
                    "function_count": func_count,
                    "class_count": class_count,
                    "max_complexity": complexity,
                    "avg_complexity": float(complexity) / max(func_count, 1),
                })
            except:
                pass
        return results


class InteractiveCLI:
    def __init__(self):
        self.options = {
            "1": ("快速统计", "快速扫描并显示基础统计信息"),
            "2": ("详细统计", "显示详细信息和文件详情"),
            "3": ("复杂度分析", "显示代码圈复杂度分析"),
            "4": ("Git统计", "显示Git仓库信息"),
            "5": ("可视化图表", "以ASCII图表显示统计结果"),
            "6": ("导出报告", "将结果导出为JSON/Markdown"),
            "7": ("完整分析", "包含所有高级功能"),
            "0": ("退出程序", "退出"),
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        self.clear_screen()
        print("\n")
        print("=" * 60)
        print("      Code Stats - 代码统计工具")
        print("=" * 60)
        print()
    
    def print_menu(self):
        print("  请选择功能：\n")
        for key, (name, desc) in self.options.items():
            print(f"    [{key}] {name:<12} - {desc}")
        print()
    
    def get_choice(self):
        while True:
            choice = input("  请输入选项: ").strip()
            if choice in self.options:
                return choice
            print("  无效选项，请重新输入")
    
    def get_path_input(self):
        print("\n  请输入要统计的文件夹路径")
        path_input = input("  路径(直接输入或拖拽文件夹) : ").strip().strip('"').strip("'")
        if not path_input:
            print("  路径不能为空")
            return None
        
        if not os.path.exists(path_input):
            print(f"  路径不存在: {path_input}")
            return None
        if not os.path.isdir(path_input):
            print(f"  路径不是目录: {path_input}")
            return None
        
        return os.path.abspath(path_input)
    
    def run(self):
        while True:
            self.print_banner()
            self.print_menu()
            choice = self.get_choice()
            
            if choice == "0":
                print("\n  感谢使用 Code Stats，再见！\n")
                break
            
            target_path = self.get_path_input()
            if not target_path:
                input("\n  按Enter键继续...")
                continue
            
            yield {"choice": choice, "path": target_path}


def format_size(size_bytes):
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def print_stats(stats, verbose=False):
    lines = []
    lines.append("=" * 60)
    lines.append(f"代码统计报告 - {stats.root_path}")
    lines.append("=" * 60)
    lines.append("\n【总体统计】")
    lines.append(f"  总文件数:        {stats.total_files}")
    lines.append(f"  总代码行数:      {stats.total_lines}")
    lines.append(f"  有效代码行数:    {stats.total_code_lines}")
    lines.append(f"  注释行数:        {stats.total_comment_lines}")
    lines.append(f"  空行数:          {stats.total_blank_lines}")
    lines.append(f"  代码占比:        {stats.code_percentage:.2f}%")
    lines.append(f"  总文件大小:      {format_size(stats.total_file_size)}")
    
    if stats.language_stats:
        lines.append("\n【按语言统计】")
        lines.append("-" * 60)
        lines.append(f"{'语言':<15} {'文件数':<8} {'代码行':<10} {'注释行':<10} {'占比':<8}")
        lines.append("-" * 60)
        for lang, lang_stats in sorted(stats.language_stats.items(), key=lambda x: x[1].code_lines, reverse=True):
            percentage = (lang_stats.code_lines / stats.total_code_lines * 100) if stats.total_code_lines > 0 else 0
            lines.append(f"{lang:<15} {lang_stats.files_count:<8} {lang_stats.code_lines:<10} {lang_stats.comment_lines:<10} {percentage:>6.2f}%")
    
    if verbose and stats.file_stats:
        lines.append("\n【文件详情】")
        lines.append("-" * 60)
        for file_stat in sorted(stats.file_stats, key=lambda x: x.code_lines, reverse=True)[:20]:
            lines.append(f"  {file_stat.filename:<30} {file_stat.code_lines:>6} 行")
    
    lines.append("\n" + "=" * 60)
    return "\n".join(lines)


def handle_choice(choice, options):
    target_path = options["path"]
    
    print(f"\n  正在分析: {target_path}")
    
    try:
        stats = analyze_project(target_path, recursive=True)
        
        if choice == "1":
            print(print_stats(stats, verbose=False))
        
        elif choice == "2":
            print(print_stats(stats, verbose=True))
        
        elif choice == "3":
            print(print_stats(stats, verbose=False))
            print("\n【代码复杂度分析】")
            print("-" * 60)
            complexity_analyzer = ComplexityAnalyzer()
            files = [fs.filepath for fs in stats.file_stats]
            languages = [fs.language for fs in stats.file_stats]
            complexity_results = complexity_analyzer.analyze_files(files, languages)
            for res in sorted(complexity_results, key=lambda x: x["cyclomatic_complexity"], reverse=True)[:10]:
                print(f"{os.path.basename(res['path']):<30} CC:{res['cyclomatic_complexity']:<4} Funcs:{res['function_count']:<4}")
        
        elif choice == "4":
            git_analyzer = GitAnalyzer(target_path)
            if git_analyzer.is_git_repo():
                print("\n【Git统计】")
                print("-" * 60)
                print(f"当前分支: {git_analyzer.get_current_branch()}")
                author_stats = git_analyzer.get_commit_stats_by_author()
                if author_stats:
                    print("\n贡献者统计:")
                    for author, stats_data in author_stats.items():
                        print(f"  {author}: {stats_data['commits']} 次提交")
            else:
                print("\n  当前目录不是Git仓库")
                print(print_stats(stats, verbose=False))
        
        elif choice == "5":
            print(print_stats(stats, verbose=False))
            print("\n" + Visualizer(stats).generate_summary_visualization())
        
        elif choice == "6":
            print(print_stats(stats, verbose=False))
            print("\n【导出报告】")
            print("1. JSON")
            print("2. Markdown")
            fmt_choice = input("选择格式 (1/2): ").strip()
            if fmt_choice == "1":
                exporter = JSONExporter(stats)
                exporter.export("code_stats_report.json")
                print("  报告已保存到: code_stats_report.json")
            else:
                exporter = MarkdownExporter(stats)
                exporter.export("code_stats_report.md")
                print("  报告已保存到: code_stats_report.md")
        
        elif choice == "7":
            print(print_stats(stats, verbose=True))
            
            print("\n【代码复杂度分析】")
            complexity_analyzer = ComplexityAnalyzer()
            files = [fs.filepath for fs in stats.file_stats]
            languages = [fs.language for fs in stats.file_stats]
            complexity_results = complexity_analyzer.analyze_files(files, languages)
            for res in sorted(complexity_results, key=lambda x: x["cyclomatic_complexity"], reverse=True)[:10]:
                print(f"{os.path.basename(res['path']):<30} CC:{res['cyclomatic_complexity']:<4}")
            
            print("\n【可视化图表】")
            print(Visualizer(stats).generate_summary_visualization())
            
            exporter = JSONExporter(stats)
            exporter.export("code_stats_full_report.json")
            print("\n  JSON报告已保存")
        
        input("\n  按Enter键返回主菜单...")
        
    except Exception as e:
        print(f"\n  错误: {e}")
        import traceback
        traceback.print_exc()
        input("\n  按Enter键返回主菜单...")


def main():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Code Stats")
        parser.add_argument("path", nargs="?", default=".", help="路径")
        parser.add_argument("-v", "--verbose", action="store_true")
        parser.add_argument("-o", "--output", help="输出文件")
        
        args = parser.parse_args()
        
        target_path = args.path
        stats = analyze_project(target_path, recursive=True)
        print(print_stats(stats, verbose=args.verbose))
        
        if args.output:
            if args.output.endswith(".json"):
                exporter = JSONExporter(stats)
            else:
                exporter = MarkdownExporter(stats)
            exporter.export(args.output)
            print(f"\n报告已保存到: {args.output}")
    else:
        cli = InteractiveCLI()
        for options in cli.run():
            handle_choice(options["choice"], options)


if __name__ == "__main__":
    main()
