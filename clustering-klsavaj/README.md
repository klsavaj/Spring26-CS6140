
# CS6140 Problem Set 4: K-Means Algorithm Variants

**Please refer to Canvas for the assignment due date.**

## Overview

In this assignment, you will implement and compare three important K-Means variants:

1. **Lloyd's Algorithm** (1957/1982) - The standard batch algorithm
2. **Elkan's Algorithm** (2003) - An optimized batch algorithm using triangle inequality
3. **Mini-Batch K-Means** (2010) - An online/incremental algorithm for large-scale data

## Step 0. Setup

Create a Python environment for the assignment and install the dependencies from `pyproject.toml`. You can verify your setup by running:

```sh
python -c "import sklearn; import numpy; import matplotlib; print('✓ All packages imported successfully')"
# Or: uv run python -c "..."
```

## Step 1. Notebook

This assignment is in the form of a Jupyter notebook. Open `cs6140-problem-set-4.ipynb` and complete all TODO sections.

**Assignment Structure:**
- **Problem 1-3**: Implement Lloyd's, Elkan's, and Mini-Batch K-Means using scikit-learn
- **Problem 4**: Compare algorithms theoretically and verify implementation correctness
- **Problem 5**: Measure and compare runtime performance
- **Problem 6**: Apply the Elbow method to determine optimal number of clusters

## Step 2. Submission

When your assignment is complete, you MUST:

1. Commit and push your code with `git`
2. Go to the assignment in Canvas and enter the link to your repository
3. Answer any additional ungraded questions in Canvas (e.g., citing AI assistance)

## Key Concepts

- **Batch vs. Online Algorithms**: Lloyd's and Elkan's process all data before updating; Mini-Batch processes small batches
- **Exact vs. Approximate Solutions**: Lloyd's and Elkan's produce identical results; Mini-Batch is approximate
- **Time Complexity**: All are O(nKd) per iteration, but Elkan's optimizes with triangle inequality
- **Incremental Learning**: Mini-Batch uniquely supports `partial_fit()` for streaming data

## Resources

- [scikit-learn KMeans Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [scikit-learn MiniBatchKMeans Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
- Lloyd, S.P. (1982). ["Least squares quantization in PCM."](https://hal.science/hal-04614938v1/file/Lloyd1982.pdf) IEEE Trans. IT, 28(2), 129-137
- Elkan, C. (2003). ["Using the Triangle Inequality to Accelerate k-Means."](https://cdn.aaai.org/ICML/2003/ICML03-022.pdf) ICML
- Sculley, D. (2010). ["Web-scale k-means clustering."](https://dl.acm.org/doi/pdf/10.1145/1772690.1772862) WWW
