import csv
from pathlib import Path
from typing import Union, List
from ..core.stats import ProjectStats, FileStats


class CSVExporter:
    def __init__(self, stats: ProjectStats):
        self.stats = stats

    def export(self, output_path: Union[str, Path]) -> None:
        output_path = Path(output_path)
        
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            
            writer.writerow([
                "File Path",
                "Language",
                "Total Lines",
                "Code Lines",
                "Comment Lines",
                "Blank Lines",
                "File Size (Bytes)",
            ])
            
            for file_stat in self.stats.file_stats:
                writer.writerow([
                    file_stat.filepath,
                    file_stat.language,
                    file_stat.total_lines,
                    file_stat.code_lines,
                    file_stat.comment_lines,
                    file_stat.blank_lines,
                    file_stat.file_size,
                ])

    def export_summary(self, output_path: Union[str, Path]) -> None:
        output_path = Path(output_path)
        
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            
            writer.writerow([
                "Language",
                "Files Count",
                "Total Lines",
                "Code Lines",
                "Comment Lines",
                "Blank Lines",
                "Percentage",
            ])
            
            for lang, lang_stats in self.stats.language_stats.items():
                percentage = (lang_stats.code_lines / self.stats.total_code_lines * 100) if self.stats.total_code_lines > 0 else 0
                writer.writerow([
                    lang,
                    lang_stats.files_count,
                    lang_stats.total_lines,
                    lang_stats.code_lines,
                    lang_stats.comment_lines,
                    lang_stats.blank_lines,
                    f"{percentage:.2f}%",
                ])