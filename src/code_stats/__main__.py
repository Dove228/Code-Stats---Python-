#!/usr/bin/env python3
"""
Code Stats - Python 代码统计工具
支持交互模式和命令行模式
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from .core.scanner import FileScanner
from .core.analyzer import CodeAnalyzer
from .core.stats import ProjectStats
from .core.complexity import ComplexityAnalyzer
from .exporters import JSONExporter, CSVExporter, MarkdownExporter
from .utils import Visualizer, GitAnalyzer, InteractiveCLI


def format_size(size_bytes: int) -> str:
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def print_stats(stats: ProjectStats, verbose: bool = False) -> str:
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
        
        sorted_langs = sorted(
            stats.language_stats.items(),
            key=lambda x: x[1].code_lines,
            reverse=True,
        )
        
        for lang, lang_stats in sorted_langs:
            percentage = (lang_stats.code_lines / stats.total_code_lines * 100) if stats.total_code_lines > 0 else 0
            lines.append(
                f"{lang:<15} {lang_stats.files_count:<8} "
                f"{lang_stats.code_lines:<10} {lang_stats.comment_lines:<10} "
                f"{percentage:>6.2f}%"
            )
    
    if verbose and stats.file_stats:
        lines.append("\n【文件详情】")
        lines.append("-" * 60)
        for file_stat in sorted(stats.file_stats, key=lambda x: x.code_lines, reverse=True)[:20]:
            lines.append(f"  {file_stat.filename:<30} {file_stat.code_lines:>6} 行  ({file_stat.language})")
        if len(stats.file_stats) > 20:
            lines.append(f"  ... 还有 {len(stats.file_stats) - 20} 个文件")
    
    lines.append("\n" + "=" * 60)
    
    return "\n".join(lines)


def print_complexity(complexity_stats_list) -> str:
    lines = []
    
    lines.append("\n【代码复杂度分析】")
    lines.append("-" * 60)
    lines.append(f"{'文件':<30} {'CC':<6} {'函数':<8} {'类':<8} {'最大CC':<8}")
    lines.append("-" * 60)
    
    sorted_stats = sorted(complexity_stats_list, key=lambda x: x.cyclomatic_complexity, reverse=True)[:15]
    
    for stats in sorted_stats:
        lines.append(
            f"{stats.path.name:<30} {stats.cyclomatic_complexity:<6} "
            f"{stats.function_count:<8} {stats.class_count:<8} {stats.max_complexity:<8}"
        )
    
    lines.append("-" * 60)
    
    return "\n".join(lines)


def print_git_stats(git_analyzer: GitAnalyzer) -> str:
    lines = []
    
    lines.append("\n【Git 统计】")
    lines.append("-" * 60)
    
    branch = git_analyzer.get_current_branch()
    if branch:
        lines.append(f"当前分支: {branch}")
    
    remote = git_analyzer.get_remote_url()
    if remote:
        lines.append(f"远程仓库: {remote}")
    
    author_stats = git_analyzer.get_commit_stats_by_author()
    if author_stats:
        lines.append("\n贡献者统计:")
        lines.append(f"{'作者':<20} {'提交数':<10} {'添加行':<10} {'删除行':<10}")
        lines.append("-" * 60)
        
        sorted_authors = sorted(author_stats.items(), key=lambda x: x[1]["commits"], reverse=True)[:10]
        
        for author, stats in sorted_authors:
            lines.append(
                f"{author:<20} {stats['commits']:<10} "
                f"{stats['lines_added']:<10} {stats['lines_deleted']:<10}"
            )
    
    lines.append("-" * 60)
    
    return "\n".join(lines)


def analyze_project(target_path: Path, exclude_dirs: set = None, include_only: set = None) -> ProjectStats:
    scanner = FileScanner(
        exclude_dirs=exclude_dirs,
        include_only=include_only,
    )
    analyzer = CodeAnalyzer(scanner=scanner)
    return analyzer.analyze_project(target_path, recursive=True)


def handle_choice(choice: str, options: dict):
    """处理用户选择"""
    target_path = Path(options["path"])
    exclude_dirs = options.get("exclude")
    lang_filter = options.get("lang")
    
    exclude_set = {".git", ".svn", "__pycache__"} if not exclude_dirs else None
    if exclude_dirs:
        exclude_set = {d.strip() for d in exclude_dirs.split(",")}
    
    include_set = None
    if lang_filter:
        include_set = {f".{ext.strip().lstrip('.')}" for ext in lang_filter.split(",")}
    
    print(f"\n  🔍 正在分析: {target_path}")
    
    try:
        stats = analyze_project(target_path, exclude_set, include_set)
        
        if choice == "1":
            result = print_stats(stats, verbose=False)
            print(result)
            
        elif choice == "2":
            result = print_stats(stats, verbose=True)
            print(result)
            
        elif choice == "3":
            result = print_stats(stats, verbose=False)
            print(result)
            
            print("\n  正在计算复杂度...")
            complexity_analyzer = ComplexityAnalyzer()
            files = [fs.path for fs in stats.file_stats]
            languages = [fs.language for fs in stats.file_stats]
            complexity_stats = complexity_analyzer.analyze_files(files, languages)
            
            result = print_complexity(complexity_stats)
            print(result)
            
        elif choice == "4":
            git_analyzer = GitAnalyzer(target_path)
            if git_analyzer.is_git_repo():
                result = print_git_stats(git_analyzer)
                print(result)
            else:
                print("\n  ⚠️  当前目录不是Git仓库，无法显示Git统计")
                result = print_stats(stats, verbose=False)
                print(result)
                
        elif choice == "5":
            result = print_stats(stats, verbose=False)
            print(result)
            
            print("\n  正在生成可视化图表...")
            visualizer = Visualizer(stats)
            print("\n" + visualizer.generate_summary_visualization())
            
        elif choice == "6":
            from .utils import InteractiveCLI
            cli = InteractiveCLI()
            export_format = cli.ask_export_format()
            output_name = f"code_stats_report.{export_format}"
            output_path = cli.ask_output_path(output_name)
            
            if export_format == "json":
                exporter = JSONExporter(stats)
                exporter.export(output_path)
            elif export_format == "csv":
                exporter = CSVExporter(stats)
                exporter.export(output_path)
                exporter.export_summary(output_path.with_suffix(".summary.csv"))
            elif export_format == "md":
                exporter = MarkdownExporter(stats)
                exporter.export(output_path)
            
            print(f"\n  ✅ 报告已保存到: {output_path}")
            
        elif choice == "7":
            result = print_stats(stats, verbose=True)
            print(result)
            
            print("\n  正在计算复杂度...")
            complexity_analyzer = ComplexityAnalyzer()
            files = [fs.path for fs in stats.file_stats]
            languages = [fs.language for fs in stats.file_stats]
            complexity_stats = complexity_analyzer.analyze_files(files, languages)
            
            result = print_complexity(complexity_stats)
            print(result)
            
            print("\n  正在生成Git统计...")
            git_analyzer = GitAnalyzer(target_path)
            if git_analyzer.is_git_repo():
                result = print_git_stats(git_analyzer)
                print(result)
            
            print("\n  正在生成可视化图表...")
            visualizer = Visualizer(stats)
            print("\n" + visualizer.generate_summary_visualization())
            
            output_name = "code_stats_full_report.json"
            output_path = Path.cwd() / output_name
            exporter = JSONExporter(stats)
            exporter.export(output_path)
            print(f"\n  💾 JSON报告已保存到: {output_path}")
        
        input("\n  按Enter键返回主菜单...")
        
    except KeyboardInterrupt:
        print("\n\n  操作已取消")
        input("\n  按Enter键返回主菜单...")
    except Exception as e:
        print(f"\n  ❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        input("\n  按Enter键返回主菜单...")


def run_interactive():
    """运行交互模式"""
    cli = InteractiveCLI()
    
    for options in cli.run():
        handle_choice(options["choice"], options)


def run_cli():
    """运行命令行模式"""
    parser = argparse.ArgumentParser(
        description="Code Stats - Python 代码统计工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument("path", nargs="?", help="要统计的目录或文件路径")
    parser.add_argument("-r", "--recursive", action="store_true", help="递归扫描子目录")
    parser.add_argument("-e", "--exclude", type=str, help="排除的目录 (逗号分隔)")
    parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    parser.add_argument("-f", "--format", type=str, default="json", help="输出格式: json, csv, md")
    parser.add_argument("-v", "--verbose", action="store_true", help="显示详细信息")
    parser.add_argument("--lang", type=str, help="只统计指定语言 (逗号分隔)")
    parser.add_argument("--complexity", action="store_true", help="显示代码复杂度分析")
    parser.add_argument("--git", action="store_true", help="显示Git统计信息")
    parser.add_argument("--visualize", action="store_true", help="显示可视化图表")
    
    args = parser.parse_args()
    
    if not args.path:
        print("❌ 请指定要统计的路径，或使用 --interactive 进入交互模式")
        print("\n使用说明:")
        print("  python code-stats.py .                    # 统计当前目录")
        print("  python code-stats.py /path/to/project     # 统计指定目录")
        print("  python code-stats.py --interactive         # 交互模式")
        sys.exit(1)
    
    target_path = Path(args.path).resolve()
    
    if not target_path.exists():
        print(f"❌ 路径不存在: {target_path}", file=sys.stderr)
        sys.exit(1)
    
    exclude_set = {".git", ".svn", "__pycache__"}
    if args.exclude:
        exclude_set.update({d.strip() for d in args.exclude.split(",")})
    
    include_set = None
    if args.lang:
        include_set = {f".{ext.strip().lstrip('.')}" for ext in args.lang.split(",")}
    
    print(f"正在分析: {target_path}")
    
    try:
        stats = analyze_project(target_path, exclude_set, include_set)
        
        result = print_stats(stats, args.verbose)
        print(result)
        
        if args.complexity:
            complexity_analyzer = ComplexityAnalyzer()
            files = [fs.path for fs in stats.file_stats]
            languages = [fs.language for fs in stats.file_stats]
            complexity_stats = complexity_analyzer.analyze_files(files, languages)
            result = print_complexity(complexity_stats)
            print(result)
        
        if args.git:
            git_analyzer = GitAnalyzer(target_path)
            if git_analyzer.is_git_repo():
                result = print_git_stats(git_analyzer)
                print(result)
        
        if args.visualize:
            visualizer = Visualizer(stats)
            print("\n" + visualizer.generate_summary_visualization())
        
        if args.output:
            output_path = Path(args.output)
            if args.format == "json" or output_path.suffix == ".json":
                exporter = JSONExporter(stats)
                exporter.export(output_path)
            elif args.format == "csv" or output_path.suffix == ".csv":
                exporter = CSVExporter(stats)
                exporter.export(output_path)
                exporter.export_summary(output_path.with_suffix(".summary.csv"))
            elif args.format == "md" or output_path.suffix in [".md", ".markdown"]:
                exporter = MarkdownExporter(stats)
                exporter.export(output_path)
            
            print(f"\n[OK] 统计结果已保存到: {output_path}")
        
    except KeyboardInterrupt:
        print("\n\n操作已取消", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"\n错误: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    if len(sys.argv) == 1 or "--interactive" in sys.argv:
        run_interactive()
    else:
        run_cli()


if __name__ == "__main__":
    main()
