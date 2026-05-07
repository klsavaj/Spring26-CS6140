
# CS6140 Problem Set 1

**Please refer to Canvas for the assignment due date.**

## Acknowledgements

This assignment is an adaptation of an assignment shared by Prof. Jonathan Mwaura.

## Step 0. Disable AI Assistance

- For these first assignments, you MUST turn off AI code assistance in your IDE (if applicable)
– Per the course policy, you may use AI tools (e.g., ChatGPT, Claude) for brainstorming, checking definitions,
or if you get stuck on a something that is hard to debug
– However, if AI tools are used, you must include a short note with your submission describing
how they were used and citing them (like you would cite a classmate who gave you help with the assignment)
– Failure to disclose AI assistance will be treated as an academic integrity violation

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
   Location: /home/philip/src/cs6140/ps1-linear-algebra/.venv

2. Checking required packages...
   ✓ ipykernel    (version 7.1.0)
   ✓ matplotlib   (version 3.10.8)
   ✓ numpy        (version 2.4.0)

============================================================
✓ All checks passed! Your environment is ready.
============================================================
```

## Step 2. Notebook

This assignment is in the form of an IPython notebook (a.k.a. a "Jupyter notebook" or just a "notebook"). If you are new to working with notebooks, I've included a very brief guide at [RUNNING_NOTEBOOKS.md](./RUNNING_NOTEBOOKS.md) with a few different ways to get started.

**To complete the assignment, fill out the notebook to the best of your ability.**

## Step 3. Submission

When your assignment is complete, you MUST:

1. Commit and push your code with `git`
2. Go to the assignment in Canvas and enter the link to your repository.
3. Answer any additional ungraded questions I included in Canvas. (For instance, there will always be a space for you to cite students or AI assistance you received on the assignment.)
