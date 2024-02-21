from dataclasses import dataclass
from pathlib import Path



# The dataclass decorator is used for automatically adding generated special methods such as __init__() and __repr__() to user-defined classes.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path