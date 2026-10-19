# PFAS_SAT project notes

- GitHub remotes: `origin` = https://github.com/feiniaoyeye/PFAS_SAT.git (the user's fork,
  push target), `upstream` = https://github.com/ch00226855/PFAS_SAT.git (original project,
  do not push here unless asked).
- Run the app with: `conda activate pfas && cd PFAS_SAT && python run.py` (see HOW_TO_RUN.md).
  Do NOT use the old `PFAS_SAT` conda env (Python 3.7) — it's deprecated and will fail to
  import PySide6. Use the `pfas` env (Python 3.11).
- **After making a fix or change to this codebase, commit it and `git push origin main`**
  so the user always has the latest version when they reopen the project on this or any
  other machine. No need to ask for confirmation each time for straightforward bug fixes —
  this was explicitly requested by the user. Still use judgment: don't push unfinished/
  experimental work-in-progress, and mention in chat what was committed and pushed.
- Only commit tracked source files relevant to the change — exclude generated/runtime
  artifacts (`__pycache__/`, `*.egg-info/`, `Network`, `Network.png`, `sankey.html`,
  `sankey.JSON`, `output_figures/`, `.DS_Store`).
