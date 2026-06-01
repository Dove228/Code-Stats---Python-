from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict


@dataclass
class ComplexityStats:
    path: Path
    language: str
    cyclomatic_complexity: int
    function_count: int
    class_count: int
    max_complexity: int
    avg_complexity: float

    @property
    def filepath(self) -> str:
        return str(self.path)

    def to_dict(self) -> Dict:
        return {
            "path": self.filepath,
            "language": self.language,
            "cyclomatic_complexity": self.cyclomatic_complexity,
            "function_count": self.function_count,
            "class_count": self.class_count,
            "max_complexity": self.max_complexity,
            "avg_complexity": round(self.avg_complexity, 2),
        }


class ComplexityAnalyzer:
    def __init__(self):
        self.decision_keywords = {
            "python": ["if", "elif", "for", "while", "and", "or", "try", "except", "with"],
            "javascript": ["if", "else", "for", "while", "switch", "case", "catch", "?"],
            "java": ["if", "else", "for", "while", "switch", "case", "catch", "try"],
            "c": ["if", "else", "for", "while", "switch", "case", "goto"],
            "cpp": ["if", "else", "for", "while", "switch", "case", "goto", "catch"],
            "go": ["if", "else", "for", "switch", "case", "select"],
            "rust": ["if", "else", "for", "while", "loop", "match"],
        }

    def analyze_file(self, file_path: Path, language: str) -> ComplexityStats:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception:
            return ComplexityStats(
                path=file_path,
                language=language,
                cyclomatic_complexity=0,
                function_count=0,
                class_count=0,
                max_complexity=0,
                avg_complexity=0.0,
            )

        lang_lower = language.lower()
        keywords = self.decision_keywords.get(lang_lower, [])

        lines = content.split("\n")
        complexity = 1
        function_count = 0
        class_count = 0
        function_complexities = []

        for line in lines:
            stripped = line.strip()
            
            if not stripped or stripped.startswith("#") or stripped.startswith("//"):
                continue

            for keyword in keywords:
                if keyword in stripped:
                    complexity += 1

            if lang_lower == "python":
                if "def " in stripped:
                    function_count += 1
                    func_complexity = self._calculate_function_complexity(stripped, keywords)
                    function_complexities.append(func_complexity)
                if "class " in stripped:
                    class_count += 1
            elif lang_lower in ["javascript", "java", "c", "cpp"]:
                if "function " in stripped or "(" in stripped and "{" in stripped:
                    function_count += 1
                if "class " in stripped:
                    class_count += 1
            elif lang_lower == "go":
                if "func " in stripped:
                    function_count += 1
            elif lang_lower == "rust":
                if "fn " in stripped:
                    function_count += 1

        max_complexity = max(function_complexities) if function_complexities else complexity
        avg_complexity = sum(function_complexities) / len(function_complexities) if function_complexities else complexity

        return ComplexityStats(
            path=file_path,
            language=language,
            cyclomatic_complexity=complexity,
            function_count=function_count,
            class_count=class_count,
            max_complexity=max_complexity,
            avg_complexity=avg_complexity,
        )

    def _calculate_function_complexity(self, first_line: str, keywords: List[str]) -> int:
        complexity = 1
        for keyword in keywords:
            if keyword in first_line:
                complexity += 1
        return complexity

    def analyze_files(self, file_paths: List[Path], languages: List[str]) -> List[ComplexityStats]:
        results = []
        for file_path, language in zip(file_paths, languages):
            results.append(self.analyze_file(file_path, language))
        return results