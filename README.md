# Enterprise Medallion Layer Starter Kit Workbook Repository

This repository manages the **Enterprise Medallion Layer Starter Kit** workbook as a baseline artifact plus repeatable automation around it.

## Repository workflow

- `workbook/source/` contains the manually approved **candidate workbook** and is treated as the source of truth.
- `workbook/dist/` contains generated working outputs created by scripts.
- `workbook/releases/` contains approved, versioned release workbooks.

## Automation approach

- Python + `openpyxl` should be used for repeatable workbook updates where possible.
- Automated scripts should make small, reviewable changes and preserve workbook structure.
- Excel desktop review is still required for final visual QA before release.

## Quick start

1. Create a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Run `python src/workbook_inventory.py` to inspect the candidate workbook.
4. Run `python src/build_workbook.py` to create an initial copy in `workbook/dist/`.
5. Run `pytest` to validate structure and scaffolding.
