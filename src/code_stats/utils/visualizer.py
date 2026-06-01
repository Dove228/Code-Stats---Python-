from typing import Dict, List
from ..core.stats import ProjectStats


class Visualizer:
    def __init__(self, stats: ProjectStats):
        self.stats = stats

    def generate_bar_chart(self, data: Dict[str, int], title: str, width: int = 50) -> str:
        if not data:
            return f"{title}\n(no data)"

        max_value = max(data.values())
        if max_value == 0:
            return f"{title}\n(no data)"

        lines = [title, ""]
        
        for label, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
            bar_length = int((value / max_value) * width)
            bar = "█" * bar_length
            percentage = (value / sum(data.values())) * 100 if sum(data.values()) > 0 else 0
            lines.append(f"{label:<15} {bar:<{width}} {value:>8} ({percentage:>5.1f}%)")

        return "\n".join(lines)

    def generate_language_chart(self) -> str:
        data = {
            lang: stats.code_lines
            for lang, stats in self.stats.language_stats.items()
        }
        return self.generate_bar_chart(data, "Code Lines by Language")

    def generate_directory_chart(self, top_n: int = 10) -> str:
        data = {}
        sorted_dirs = sorted(
            self.stats.directory_stats.items(),
            key=lambda x: x[1].code_lines,
            reverse=True,
        )[:top_n]
        
        for dirpath, dir_stats in sorted_dirs:
            short_path = dirpath.replace(str(self.stats.root_path), "")
            if short_path.startswith("/") or short_path.startswith("\\"):
                short_path = short_path[1:]
            if not short_path:
                short_path = "."
            data[short_path] = dir_stats.code_lines

        return self.generate_bar_chart(data, "Code Lines by Directory")

    def generate_pie_chart_text(self, data: Dict[str, int], title: str) -> str:
        if not data:
            return f"{title}\n(no data)"

        total = sum(data.values())
        if total == 0:
            return f"{title}\n(no data)"

        lines = [title, ""]

        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        
        for label, value in sorted_data:
            percentage = (value / total) * 100
            lines.append(f"{label:<20} {percentage:>6.2f}%  ({value} lines)")

        return "\n".join(lines)

    def generate_summary_visualization(self) -> str:
        lines = []
        
        lines.append("=" * 70)
        lines.append("CODE STATISTICS VISUALIZATION")
        lines.append("=" * 70)
        lines.append("")
        
        lines.append(self.generate_language_chart())
        lines.append("")
        lines.append("-" * 70)
        lines.append("")
        lines.append(self.generate_directory_chart())
        lines.append("")
        lines.append("=" * 70)
        
        return "\n".join(lines)

    def generate_complexity_chart(self, complexity_data: List[Dict]) -> str:
        if not complexity_data:
            return "Complexity Analysis\n(no data)"

        lines = ["Complexity Analysis", ""]
        lines.append(f"{'File':<30} {'CC':<6} {'Funcs':<8} {'Classes':<8}")
        lines.append("-" * 60)

        sorted_data = sorted(complexity_data, key=lambda x: x.get("cyclomatic_complexity", 0), reverse=True)[:15]
        
        for item in sorted_data:
            filename = item.get("path", "").split("/")[-1].split("\\")[-1]
            cc = item.get("cyclomatic_complexity", 0)
            funcs = item.get("function_count", 0)
            classes = item.get("class_count", 0)
            lines.append(f"{filename:<30} {cc:<6} {funcs:<8} {classes:<8}")

        return "\n".join(lines)