# Agent Instructions

- Preserve files in `workbook/source/` unless explicitly instructed otherwise.
- Never overwrite the candidate workbook.
- Prefer small, reviewable changes.
- Use `openpyxl` for workbook inspection and repeatable edits.
- Keep workbook usability first: clear tabs, readable widths, frozen headers, instructional rows, dropdowns, print-friendly layout, and protected/hidden helper areas where appropriate.
- Add or update tests when changing sheet names, required columns, dropdowns, formulas, validations, or workbook structure.
- Before making large workbook changes, inspect the workbook and summarize the proposed approach.
- Do not attempt a full workbook rebuild unless explicitly asked.
