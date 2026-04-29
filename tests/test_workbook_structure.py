from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_required_folders_exist() -> None:
    required_dirs = [
        REPO_ROOT / "workbook",
        REPO_ROOT / "workbook" / "source",
        REPO_ROOT / "workbook" / "dist",
        REPO_ROOT / "workbook" / "releases",
        REPO_ROOT / "src",
        REPO_ROOT / "content",
        REPO_ROOT / "tests",
    ]
    for path in required_dirs:
        assert path.exists() and path.is_dir()


def test_candidate_workbook_exists() -> None:
    candidate = REPO_ROOT / "workbook" / "source" / "Enterprise_Medallion_Layer_Starter_Kit_Candidate.xlsx"
    assert candidate.exists() and candidate.is_file()
