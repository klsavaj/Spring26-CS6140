
# Problem Set 5: Trees, Forests, and Boosting

## Overview

Build a heart disease risk scoring module using decision trees, random forests, and gradient boosted trees. Compare multiple implementations, tune hyperparameters with Optuna, and write a report recommending a model for production deployment.

**Total points:** 60 (40 notebook + 20 report)

## Deliverables

1. `cs6140-problem-set-5.ipynb` — completed notebook that runs end-to-end
2. `REPORT.md` — written report with analysis, tables, and figures

## Setup

### 1. Install dependencies

```bash
# Recommended
uv sync

# Alternative
pip install -r requirements.txt
```

### 2. Get the data

Copy `brfss_national.csv` and `brfss_maine.csv` from the Week 9 lab into this directory:

```bash
cp /path/to/lab/brfss_national.csv .
cp /path/to/lab/brfss_maine.csv .
```

### 3. Verify your environment

```bash
python sanity_check.py
```

## Running the Notebook

See [RUNNING_NOTEBOOKS.md](../RUNNING_NOTEBOOKS.md) for detailed instructions on running Jupyter notebooks via the command line, VS Code, or Google Colab.

## AI Policy

You **may and are encouraged** to use AI tools for **plotting and visualization code**. Make your figures as clear and polished as you can.

All **written analysis, interpretation, and the report** must be your own work.
