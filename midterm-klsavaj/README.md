
# CS6140 Midterm: Maine Legislative Bills Analysis

## Overview

In this midterm, you will analyze a dataset of bills from the Maine 132nd Legislature. The dataset contains numeric vector embeddings of bill titles and contents, along with metadata including committee assignments.

## Structure

| File | Description |
|------|-------------|
| `0-data-preparation.ipynb` | How the dataset was built — pre-executed, read only |
| `1-eda-clustering.ipynb` | Exploratory data analysis, dimensionality reduction, and clustering |
| `2-logistic-regression.ipynb` | Implement logistic regression from scratch |
| `3-model-comparison.ipynb` | Model comparison with SVM |
| `4-best-classifier.ipynb` | Open-ended: build the best classifier you can |

I recommend that you start by reading through each notebook in order, but you can work on them in any order you like. The notebooks are designed to be run end-to-end, but you can also run individual cells if you want to experiment.

Each notebook will be graded out of 25 points, for a total of 100 points. The grading rubric is as follows:
- 5 points: Code runs without errors and produces all expected outputs based on the todos
- 5 points: Code is technically correct and implements the required functionality
- 5 points: Code is well-organized, readable, and appropriately commented
- 10 points: Written responses are substantive, demonstrate reasoning, and answer the questions posed in the notebook

Note that more points are allocated to written responses and code comments than to technical execution - this emphasizes the importance of communication and reasoning in data science, not just raw performance numbers. This is particularly the case in modern AI-driven workflows, where you can quickly fix technical bugs but the real skill is in interpreting results, troubleshooting, and communicating your process.

## Allowed Resources

**Unlike the problem sets, you may NOT use any external resources except the following:**
- Python library documentation (scikit-learn, NumPy, pandas, matplotlib, seaborn, UMAP, etc.)
- The two textbooks for the course (ISLP in particular may help if you need reminders of specific concepts)
- All assignments, lecture materials, and other documents from Canvas

If you are stuck, PLEASE message me and Rohan for assistance. We are happy to help you troubleshoot technical issues, clarify concepts, or give you hints on how to approach the problems. The midterm is meant to be challenging, but it should not be frustrating — we want you to learn and demonstrate your skills, not struggle with technical bugs or misunderstandings.

## Collaboration Policy

This likely goes without saying, but you may not discuss the midterm with anyone else in the class, and you may not share your code or written responses with anyone else. You may ask me or Rohan for help, but you may not ask for help from other students or share your work with them. This is an individual assignment, and all work must be your own.

## Office Hours

Given low attendance at the regular office hours, I will instead be doing office hours by appointment throughout the week. Please email me or Rohan to set up a time if you want to meet. My work schedule is somewhat flexible this week, so I can likely accommodate most times.

## Late Submissions

I will honor the 24-hour late submission window as stated in the syllabus, but I encourage you to submit as early as possible to avoid any last-minute technical issues. If you have an emergency that prevents you from submitting on time, please contact me as soon as possible. **You cannot use your four late days on the midterm.**

## Setup

```bash
uv sync
python sanity_check.py
```

Or with pip:

```bash
pip install -r requirements.txt
python sanity_check.py
```
