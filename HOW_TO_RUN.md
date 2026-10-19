# PFAS_SAT — Setup & Run Guide

PFAS Systems Analysis Tool. Source: https://github.com/ch00226855/PFAS_SAT

## Requirements

- [Anaconda or Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Python **3.9 or newer** (do NOT use Python 3.7 — the app will fail to install/run)

## One-time setup

Open a terminal and run:

```bash
git clone https://github.com/ch00226855/PFAS_SAT.git
cd PFAS_SAT
conda create --name pfas python=3.11
conda activate pfas
pip install -e .
```

This creates a conda environment named `pfas` and installs PFAS_SAT along with
all its dependencies (PySide6 for the GUI, pandas, plotly, graphviz, matplotlib,
seaborn, jupyter, etc.), as listed in `setup.py`.

`pip install -e .` only installs the **Python** `graphviz` bindings - it does NOT
install the actual Graphviz software (the `dot` executable) that those bindings
call out to. Without it, the process-network diagram in the "Define System" tab
silently fails to render/update (the Python call fails, prints a warning to the
terminal, and the old image is left on screen). Install it separately:

```bash
brew install graphviz        # macOS
# or: conda install -c conda-forge graphviz
# or: sudo apt install graphviz   # Debian/Ubuntu
```

Verify with `dot -V` after activating the `pfas` environment.

## Running the tool

Every time you want to open PFAS_SAT:

```bash
conda activate pfas
cd PFAS_SAT
python run.py
```

This launches the PFAS_SAT desktop GUI application.

## Troubleshooting

- **`ModuleNotFoundError: No module named 'PySide6'`** — the environment doesn't
  have the dependencies installed. Re-run `pip install -e .` from inside the
  `PFAS_SAT` folder while the `pfas` environment is active.
- **Package won't install / import errors** — check your Python version with
  `python --version`. It must be 3.9+. If your conda environment was created
  with an older Python (e.g. 3.7), delete it and recreate it:
  ```bash
  conda deactivate
  conda env remove --name pfas
  conda create --name pfas python=3.11
  conda activate pfas
  pip install -e .
  ```
- **Nothing happens / no window appears** — give it a few seconds, the GUI can
  take a moment to start. Check the terminal for error output.
