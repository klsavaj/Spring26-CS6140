
# CS6140 Problem Set 3

**Please refer to Canvas for the assignment due date.**

## Overview

This problem set focuses on supervised learning with real-world data. You'll work with 2024 Maine presidential election results joined with US Census demographic data to train regression and classification models using scikit-learn.

## Step 0. AI Policy

- For this assignment, you MAY use AI tab-complete but you must NOT use AI to generate substantive content (e.g., code, text, or analysis).
- You MAY discuss your answers to the reflection questions with classmates, but you must NOT use AI tools to help you answer them.
- Regardless, **if AI tools are used, you must include a short note with your submission describing
how they were used and citing them (like you would cite a classmate who gave you help with the assignment)**
- Failure to disclose AI assistance will be treated as an academic integrity violation

## Step 1. Setup

Create a Python environment for the assignment and install the dependencies from `pyproject.toml` or `requirements.txt`. You can verify your setup by running:

```sh
python sanity_check.py # Or uv run python sanity_check.py
```

If you are set up correctly, you should see something like:

```
============================================================
CS6140 - Environment Sanity Check
============================================================

1. Checking virtual environment...
   ✓ Running in virtual environment
   Location: /path/to/your/.venv

2. Checking required packages...
   ✓ ipykernel    (version ...)
   ✓ matplotlib   (version ...)
   ✓ numpy        (version ...)
   ✓ pandas       (version ...)
   ✓ scikit-learn (version ...)
   ✓ openpyxl     (version ...)
   ✓ requests     (version ...)

============================================================
✓ All checks passed! Your environment is ready.
============================================================
```

## Step 2. Download the Data

Run the data download script to fetch and prepare the dataset:

```sh
python download_data.py # Or uv run python download_data.py
```

This will download election results from the Maine Secretary of State and demographic data from the US Census Bureau, then produce `maine_election_data.csv`.

## Step 3. Check Your Assigned Models

Each student has been assigned a specific **regressor** and **classifier** to use for Problems 2 and 3. Your assignments are in the `ASSIGNED_MODELS.md` file. You MUST use the models you were assigned — using different models for these problems will result in lost points. (You may use any model you like for Problem 4.)

## Step 4. Notebook

This assignment is in the form of an IPython notebook (a.k.a. a "Jupyter notebook" or just a "notebook"). If you are new to working with notebooks, I've included a very brief guide at [RUNNING_NOTEBOOKS.md](./RUNNING_NOTEBOOKS.md) with a few different ways to get started.

**To complete the assignment, fill out the notebook to the best of your ability.**

## Step 5. Submission

When your assignment is complete, you MUST:

1. Commit and push your code with `git`
2. Go to the assignment in Canvas and enter the link to your repository.
3. Answer any additional ungraded questions I included in Canvas. (For instance, there will always be a space for you to cite students or AI assistance you received on the assignment.)
