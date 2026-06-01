from pathlib import Path
from typing import List, Set, Optional


class FileScanner:
    def __init__(
        self,
        exclude_dirs: Optional[Set[str]] = None,
        exclude_files: Optional[Set[str]] = None,
        include_only: Optional[Set[str]] = None,
    ):
        self.exclude_dirs = exclude_dirs or {
            ".git",
            ".svn",
            ".hg",
            "__pycache__",
            "node_modules",
            "venv",
            "env",
            ".venv",
            ".env",
            "build",
            "dist",
            ".idea",
            ".vscode",
            ".vs",
            "target",
            "bin",
            "obj",
            "packages",
            ".tox",
            ".pytest_cache",
            ".mypy_cache",
            ".ruff_cache",
            ".coverage",
            "htmlcov",
            ".eggs",
            "*.egg-info",
            ".DS_Store",
            "Thumbs.db",
        }
        
        # 常见二进制文件扩展名
        self.binary_extensions = {
            ".exe", ".dll", ".so", ".dylib", ".a", ".lib", ".o", ".obj",
            ".pyc", ".pyo", ".pyd", ".whl", ".egg",
            ".zip", ".tar", ".gz", ".7z", ".rar",
            ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
            ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".svg",
            ".mp3", ".mp4", ".wav", ".avi", ".mov", ".mkv",
            ".db", ".sqlite", ".sqlite3",
            ".class", ".jar", ".war", ".ear",
        }
        
        self.exclude_files = exclude_files or {
            ".gitignore",
            ".gitattributes",
            ".editorconfig",
            "package-lock.json",
            "yarn.lock",
            "pnpm-lock.yaml",
            "poetry.lock",
            "requirements.txt",
            "setup.py",
            "setup.cfg",
            "pyproject.toml",
            "MANIFEST.in",
            ".travis.yml",
            ".github",
            "LICENSE",
            "LICENSE.txt",
            "LICENSE.md",
        }
        self.include_only = include_only

    def should_exclude_dir(self, dir_name: str) -> bool:
        dir_lower = dir_name.lower()
        for exclude in self.exclude_dirs:
            exclude_lower = exclude.lower()
            if exclude_lower in dir_lower or dir_lower == exclude_lower:
                return True
            if exclude_lower.startswith("*") and dir_lower.endswith(
                exclude_lower[1:]
            ):
                return True
        return False

    def should_exclude_file(self, file_name: str) -> bool:
        file_lower = file_name.lower()
        for exclude in self.exclude_files:
            exclude_lower = exclude.lower()
            if exclude_lower == file_lower:
                return True
            if exclude_lower.startswith("*") and file_lower.endswith(
                exclude_lower[1:]
            ):
                return True
        return False
    
    def is_binary_extension(self, file_path: Path) -> bool:
        ext = file_path.suffix.lower()
        return ext in self.binary_extensions

    def is_valid_file(self, file_path: Path) -> bool:
        if self.should_exclude_file(file_path.name):
            return False
        
        if self.is_binary_extension(file_path):
            return False

        if self.include_only:
            ext = file_path.suffix.lower()
            if ext not in self.include_only and file_path.name not in self.include_only:
                return False

        return True

    def scan_directory(
        self, root_path: Path, recursive: bool = True
    ) -> List[Path]:
        files = []

        try:
            if recursive:
                for item in root_path.rglob("*"):
                    if item.is_file() and self.is_valid_file(item):
                        in_excluded_dir = False
                        for parent in item.parents:
                            if self.should_exclude_dir(parent.name):
                                in_excluded_dir = True
                                break
                        if not in_excluded_dir:
                            files.append(item)
            else:
                for item in root_path.iterdir():
                    if item.is_file() and self.is_valid_file(item):
                        files.append(item)
        except PermissionError:
            pass
        except Exception:
            pass

        return sorted(files)

    def scan_paths(
        self, paths: List[Path], recursive: bool = True
    ) -> List[Path]:
        all_files = []
        for path in paths:
            if path.is_file():
                if self.is_valid_file(path):
                    all_files.append(path)
            elif path.is_dir():
                all_files.extend(self.scan_directory(path, recursive))
        return all_files
