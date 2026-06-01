from pathlib import Path
from typing import Optional
from .stats import FileStats, ProjectStats
from .languages import LanguageRegistry, get_language_by_extension, get_language_name
from .scanner import FileScanner


class CodeAnalyzer:
    def __init__(self, scanner: Optional[FileScanner] = None):
        self.scanner = scanner or FileScanner()

    def analyze_file(self, file_path: Path) -> FileStats:
        language = get_language_name(file_path.suffix)
        config = get_language_by_extension(file_path.suffix)

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            file_size = len(content.encode("utf-8"))
        except Exception:
            return FileStats(
                path=file_path,
                language=language,
                total_lines=0,
                code_lines=0,
                comment_lines=0,
                blank_lines=0,
                file_size=0,
            )

        lines = content.split("\n")
        total_lines = len(lines)

        if config:
            code_lines, comment_lines, blank_lines = self._analyze_lines(
                lines, config
            )
        else:
            code_lines, comment_lines, blank_lines = self._analyze_plain_text(lines)

        return FileStats(
            path=file_path,
            language=language,
            total_lines=total_lines,
            code_lines=code_lines,
            comment_lines=comment_lines,
            blank_lines=blank_lines,
            file_size=file_size,
        )

    def _analyze_plain_text(self, lines: list[str]) -> tuple[int, int, int]:
        code_lines = 0
        comment_lines = 0
        blank_lines = 0

        for line in lines:
            stripped = line.strip()
            if not stripped:
                blank_lines += 1
            else:
                code_lines += 1

        return code_lines, comment_lines, blank_lines

    def _analyze_lines(
        self, lines: list[str], config
    ) -> tuple[int, int, int]:
        code_lines = 0
        comment_lines = 0
        blank_lines = 0

        in_multiline_comment = False
        single_comment = config.single_line_comment
        ml_start = config.multi_line_comment_start
        ml_end = config.multi_line_comment_end
        has_ml_comments = bool(ml_start and ml_end)

        for line in lines:
            stripped = line.strip()

            if not stripped:
                blank_lines += 1
                continue

            if has_ml_comments:
                if in_multiline_comment:
                    if ml_end in stripped:
                        if stripped.count(ml_start) > stripped.count(ml_end):
                            pass
                        else:
                            in_multiline_comment = False
                            comment_lines += 1
                    else:
                        comment_lines += 1
                    continue

                if ml_start in stripped:
                    if ml_end in stripped:
                        if stripped.count(ml_start) == stripped.count(ml_end):
                            if single_comment and single_comment in stripped:
                                if stripped.index(ml_start) < stripped.index(
                                    single_comment
                                ):
                                    comment_lines += 1
                                else:
                                    code_lines += 1
                            else:
                                comment_lines += 1
                        elif stripped.endswith(ml_end) and stripped.count(ml_start) == 1:
                            comment_lines += 1
                        else:
                            in_multiline_comment = True
                            comment_lines += 1
                    else:
                        in_multiline_comment = True
                        comment_lines += 1
                    continue

            if single_comment and stripped.startswith(single_comment):
                comment_lines += 1
                continue

            code_lines += 1

        return code_lines, comment_lines, blank_lines

    def analyze_project(
        self,
        root_path: Path,
        recursive: bool = True,
        exclude_dirs: Optional[set[str]] = None,
    ) -> ProjectStats:
        if exclude_dirs:
            scanner = FileScanner(exclude_dirs=exclude_dirs)
        else:
            scanner = self.scanner

        files = scanner.scan_directory(root_path, recursive)

        project_stats = ProjectStats(root_path=root_path)

        for file_path in files:
            file_stats = self.analyze_file(file_path)
            project_stats.add_file_stats(file_stats)

        return project_stats

    def analyze_files(self, file_paths: list[Path]) -> list[FileStats]:
        return [self.analyze_file(file_path) for file_path in file_paths]
