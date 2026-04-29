"""Safe starter build script for workbook packaging.

This script copies the baseline candidate workbook from workbook/source
into workbook/dist without applying major transformations.
"""

from __future__ import annotations

import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = REPO_ROOT / "workbook" / "source"
DIST_DIR = REPO_ROOT / "workbook" / "dist"
CANDIDATE_FILENAME = "Enterprise_Medallion_Layer_Starter_Kit_Candidate.xlsx"


def build_workbook() -> Path:
    """Copy the candidate workbook to workbook/dist and return destination path."""
    source_path = SOURCE_DIR / CANDIDATE_FILENAME
    if not source_path.exists():
        raise FileNotFoundError(f"Candidate workbook not found: {source_path}")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    destination_path = DIST_DIR / CANDIDATE_FILENAME

    # shutil.copy2 preserves timestamps/metadata while maintaining workbook bytes.
    shutil.copy2(source_path, destination_path)
    return destination_path


if __name__ == "__main__":
    output = build_workbook()
    print(f"Workbook copied to: {output}")
