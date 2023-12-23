# SparkyStats
Converts excel stat sheets from NAQT-like Quizbowl tournaments to SQBS files.

## Requirements
`pip install xlrd==1.2.0`

## How To
1. Use https://docs.google.com/spreadsheets/d/1Yn8gCP4u07dCtWf3WFvc6DgIOi5QNNsU8h6PP-bTbyI/edit#gid=156438897 as a template stats sheet. Duplicate sheets and rename to anything. Change rosters only in the roster sheet.
2. Download stats as excel sheets and move to stats_sheets.
3. Run `python -m read`.
