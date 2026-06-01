import json
import yaml
from pathlib import Path
from typing import Set, Optional, Dict, Any


class Config:
    def __init__(
        self,
        exclude_dirs: Optional[Set[str]] = None,
        exclude_files: Optional[Set[str]] = None,
        include_only: Optional[Set[str]] = None,
        output_format: str = "json",
        verbose: bool = False,
        recursive: bool = True,
        show_complexity: bool = False,
        show_git_stats: bool = False,
        show_visualization: bool = False,
    ):
        self.exclude_dirs = exclude_dirs or set()
        self.exclude_files = exclude_files or set()
        self.include_only = include_only or set()
        self.output_format = output_format
        self.verbose = verbose
        self.recursive = recursive
        self.show_complexity = show_complexity
        self.show_git_stats = show_git_stats
        self.show_visualization = show_visualization

    @classmethod
    def from_file(cls, config_path: Path) -> "Config":
        if not config_path.exists():
            return cls()

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                if config_path.suffix in [".yaml", ".yml"]:
                    data = yaml.safe_load(f)
                else:
                    data = json.load(f)

            return cls(
                exclude_dirs=set(data.get("exclude_dirs", [])),
                exclude_files=set(data.get("exclude_files", [])),
                include_only=set(data.get("include_only", [])),
                output_format=data.get("output_format", "json"),
                verbose=data.get("verbose", False),
                recursive=data.get("recursive", True),
                show_complexity=data.get("show_complexity", False),
                show_git_stats=data.get("show_git_stats", False),
                show_visualization=data.get("show_visualization", False),
            )
        except Exception:
            return cls()

    @classmethod
    def find_config(cls, root_path: Path) -> "Config":
        config_names = [
            ".codestats",
            ".codestats.json",
            ".codestats.yaml",
            ".codestats.yml",
            "codestats.json",
            "codestats.yaml",
            "codestats.yml",
        ]

        for name in config_names:
            config_path = root_path / name
            if config_path.exists():
                return cls.from_file(config_path)

        return cls()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "exclude_dirs": list(self.exclude_dirs),
            "exclude_files": list(self.exclude_files),
            "include_only": list(self.include_only),
            "output_format": self.output_format,
            "verbose": self.verbose,
            "recursive": self.recursive,
            "show_complexity": self.show_complexity,
            "show_git_stats": self.show_git_stats,
            "show_visualization": self.show_visualization,
        }

    def save(self, config_path: Path) -> None:
        data = self.to_dict()

        with open(config_path, "w", encoding="utf-8") as f:
            if config_path.suffix in [".yaml", ".yml"]:
                yaml.dump(data, f, default_flow_style=False)
            else:
                json.dump(data, f, indent=2)


DEFAULT_CONFIG = Config(
    exclude_dirs={
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
    },
    recursive=True,
    verbose=False,
)