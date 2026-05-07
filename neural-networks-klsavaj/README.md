[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/6gC0MtuE)
# Problem Set 6: From Logistic Regression to Neural Networks

## Overview

In this problem set, you will revisit the Maine bills dataset from the midterm using PyTorch. The goal is to connect what you know about logistic regression to the broader family of neural networks — understanding how a single-layer network is equivalent to logistic regression, and how adding layers and nonlinearities enables richer representations.

This assignment bridges the midterm dataset, the neural networks lecture, and the neural networks lab. By the end, you should be able to explain why neural networks are a generalization of logistic regression, and when (and why) the added complexity pays off.

## Setup

### Option A: uv (Recommended)

```bash
uv sync
source .venv/bin/activate
```

### Option B: pip

```bash
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

### Verify your environment

```bash
python sanity_check.py
```

## How to Run

Open `ps6-neural-networks.ipynb` in VS Code or Jupyter and run cells top to bottom. See [RUNNING_NOTEBOOKS.md](RUNNING_NOTEBOOKS.md) for detailed instructions.

## Submission

1. Complete all cells in `ps6-neural-networks.ipynb`
2. Commit and push your work: `git push`
3. Submit the repository link on Canvas

## Grading Rubric

| Criteria | Points |
|----------|--------|
| Code runs without errors, produces expected outputs | 10 |
| Code is technically correct, implements required functionality | 20 |
| Code is well-organized, readable, appropriately commented | 5 |
| Written responses are substantive, demonstrate reasoning | 15 |
| **Total** | **50** |

## References

- ISLP Ch. 10 §10.1–10.2, §10.7
- PML Ch. 13 §13.2–13.4

## Tips

- Start with Part 1 — if your logistic regression works, the neural network extensions are straightforward
- Keep your training loop modular (the `train_one_epoch` and `evaluate` helpers)
- CPU is fine — these models are small enough that GPU isn't needed
- Use the exact same train/test split for all models so results are comparable
- Watch your training curves — if training accuracy >> test accuracy, you're overfitting
