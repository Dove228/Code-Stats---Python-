import json
from pathlib import Path
from typing import Union
from ..core.stats import ProjectStats


class JSONExporter:
    def __init__(self, stats: ProjectStats):
        self.stats = stats

    def export(self, output_path: Union[str, Path]) -> None:
        output_path = Path(output_path)
        data = self.stats.to_dict()
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def export_string(self) -> str:
        data = self.stats.to_dict()
        return json.dumps(data, indent=2, ensure_ascii=False)