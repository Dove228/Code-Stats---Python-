import subprocess
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class GitCommitStats:
    commit_hash: str
    author: str
    date: str
    message: str
    files_changed: int
    lines_added: int
    lines_deleted: int

    def to_dict(self) -> Dict:
        return {
            "commit_hash": self.commit_hash,
            "author": self.author,
            "date": self.date,
            "message": self.message,
            "files_changed": self.files_changed,
            "lines_added": self.lines_added,
            "lines_deleted": self.lines_deleted,
        }


class GitAnalyzer:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.git_available = self._check_git()

    def _check_git(self) -> bool:
        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                cwd=self.repo_path,
            )
            return result.returncode == 0
        except Exception:
            return False

    def _run_git_command(self, args: List[str]) -> Optional[str]:
        if not self.git_available:
            return None

        try:
            result = subprocess.run(
                ["git"] + args,
                capture_output=True,
                text=True,
                cwd=self.repo_path,
            )
            if result.returncode == 0:
                return result.stdout
            return None
        except Exception:
            return None

    def is_git_repo(self) -> bool:
        git_dir = self.repo_path / ".git"
        return git_dir.exists()

    def get_current_branch(self) -> Optional[str]:
        output = self._run_git_command(["branch", "--show-current"])
        return output.strip() if output else None

    def get_commit_history(self, limit: int = 50) -> List[GitCommitStats]:
        if not self.is_git_repo():
            return []

        output = self._run_git_command([
            "log",
            f"--max-count={limit}",
            "--pretty=format:%H|%an|%ad|%s",
            "--date=short",
            "--numstat",
        ])

        if not output:
            return []

        commits = []
        lines = output.split("\n")
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            if "|" in line:
                parts = line.split("|")
                if len(parts) >= 4:
                    commit_hash = parts[0]
                    author = parts[1]
                    date = parts[2]
                    message = parts[3]

                    files_changed = 0
                    lines_added = 0
                    lines_deleted = 0

                    i += 1
                    while i < len(lines) and lines[i].strip() and "|" not in lines[i]:
                        stat_line = lines[i].strip()
                        stat_parts = stat_line.split()
                        if len(stat_parts) >= 3:
                            try:
                                added = int(stat_parts[0]) if stat_parts[0] != "-" else 0
                                deleted = int(stat_parts[1]) if stat_parts[1] != "-" else 0
                                lines_added += added
                                lines_deleted += deleted
                                files_changed += 1
                            except ValueError:
                                pass
                        i += 1

                    commits.append(GitCommitStats(
                        commit_hash=commit_hash,
                        author=author,
                        date=date,
                        message=message,
                        files_changed=files_changed,
                        lines_added=lines_added,
                        lines_deleted=lines_deleted,
                    ))
            else:
                i += 1

        return commits

    def get_commit_stats_by_author(self) -> Dict[str, Dict]:
        commits = self.get_commit_history(limit=1000)
        
        author_stats = {}
        for commit in commits:
            if commit.author not in author_stats:
                author_stats[commit.author] = {
                    "commits": 0,
                    "lines_added": 0,
                    "lines_deleted": 0,
                    "files_changed": 0,
                }
            author_stats[commit.author]["commits"] += 1
            author_stats[commit.author]["lines_added"] += commit.lines_added
            author_stats[commit.author]["lines_deleted"] += commit.lines_deleted
            author_stats[commit.author]["files_changed"] += commit.files_changed

        return author_stats

    def get_file_history(self, file_path: Path) -> List[Dict]:
        if not self.is_git_repo():
            return []

        relative_path = file_path.relative_to(self.repo_path)
        output = self._run_git_command([
            "log",
            "--follow",
            "--pretty=format:%H|%an|%ad",
            "--date=short",
            str(relative_path),
        ])

        if not output:
            return []

        history = []
        for line in output.split("\n"):
            if "|" in line:
                parts = line.split("|")
                if len(parts) >= 3:
                    history.append({
                        "commit": parts[0],
                        "author": parts[1],
                        "date": parts[2],
                    })

        return history

    def get_remote_url(self) -> Optional[str]:
        output = self._run_git_command(["remote", "get-url", "origin"])
        return output.strip() if output else None