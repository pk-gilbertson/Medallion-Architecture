from pathlib import Path

from src.build_workbook import build_workbook
from src.workbook_inventory import default_candidate_path, inspect_workbook


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_inventory_reads_workbook() -> None:
    candidate = default_candidate_path()
    inventory = inspect_workbook(candidate)

    assert "sheet_names" in inventory
    assert "sheets" in inventory
    assert isinstance(inventory["sheet_names"], list)
    assert len(inventory["sheet_names"]) >= 1


def test_build_workbook_creates_dist_copy() -> None:
    source_path = default_candidate_path()
    output_path = build_workbook()

    assert output_path.exists()
    assert output_path.parent == REPO_ROOT / "workbook" / "dist"
    assert output_path.name == source_path.name
    assert output_path.stat().st_size == source_path.stat().st_size
