# Running Jupyter Notebooks

This guide explains how to run the Jupyter notebook for this assignment.

---

## Option A: VS Code (Recommended)

VS Code provides excellent Jupyter notebook support with inline execution.

### 1. Install the Jupyter extension

- Open VS Code
- Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
- Search for "Jupyter" by Microsoft
- Click Install

### 2. Open the notebook

- Open `ps6-neural-networks.ipynb` in VS Code
- You'll see a notebook interface with cells

### 3. Select the kernel

- Click "Select Kernel" in the top-right corner
- Choose "Python Environments..."
- Select your virtual environment (should show the `.venv` path)

### 4. Run cells

- Click the play button next to a cell to run it
- Or use `Shift+Enter` to run a cell and move to the next one
- Use `Ctrl+Enter` (Cmd+Enter on Mac) to run a cell without moving

---

## Option B: Jupyter Notebook (Command Line)

### 1. Activate your virtual environment

```bash
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 2. Launch Jupyter

```bash
jupyter notebook
```

This will start a Jupyter server and open your browser to `http://localhost:8888`.

### 3. When finished

- Save your work (File > Save)
- Stop the server with `Ctrl+C` in the terminal

---

## Troubleshooting

### "Kernel not found" or "No module named 'numpy'"

**In VS Code:**
- Make sure you selected the correct kernel (your `.venv` environment)
- Try reloading VS Code: Ctrl+Shift+P > "Developer: Reload Window"

**In Jupyter:**
- Ensure your virtual environment is activated before launching Jupyter
- Verify packages are installed: `pip list | grep numpy`

### "No module named 'torch'" on local machine

PyTorch can be large to install locally. If you have trouble:
- Follow the [official PyTorch install guide](https://pytorch.org/get-started/locally/) for your platform
- CPU-only install is sufficient for this assignment
