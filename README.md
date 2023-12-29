# SparkyStats
Converts excel stat sheets from NAQT-like Quizbowl tournaments to SQBS files.

## Requirements
You need to [install python](https://wiki.python.org/moin/BeginnersGuide/Download). Once python is installed (any version will probably do), install `omegaconf` and `openpyxl` using the following commands.
`pip install omegaconf`

`pip install openpyxl`

## How To
TODO: make this better when I fix my thing
1. Use this [template stats sheet](https://docs.google.com/spreadsheets/d/1Yn8gCP4u07dCtWf3WFvc6DgIOi5QNNsU8h6PP-bTbyI/edit#gid=156438897). Duplicate sheets and rename to anything. Other sheets can be used as well provided you create custom profiles in `tournament_settings.yaml`.
2. Adjust `tournament_settings.yaml` to fit your tournament's specifications.
3. Download sheets as excel sheets and move to stats_sheets.
4. Run `python -m read`.
