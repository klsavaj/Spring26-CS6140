# Running Jupyter Notebooks

This guide explains how to run the Jupyter notebooks in this project using different methods.

## Prerequisites

Before running the notebooks, ensure your environment is set up correctly:

```bash
python sanity_check.py # Or uv run python sanity_check.py
```

This will verify that you have all required packages installed.

---

## Option A: Jupyter Notebook (Command Line)

Run Jupyter from your virtual environment:

### 1. Activate your virtual environment

**Using venv:**
```bash
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

**Using uv:**
```bash
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 2. Launch Jupyter

```bash
jupyter notebook
```

This will:
- Start a Jupyter server
- Open your default browser to `http://localhost:8888`
- Show a file browser where you can click on `.ipynb` files to open them

### 3. When finished

- Save your work in the notebook (File → Save)
- Close browser tabs
- Stop the server with `Ctrl+C` in the terminal
- Deactivate the virtual environment: `deactivate`

---

## Option B: VS Code

VS Code provides excellent Jupyter notebook support with inline execution.

### 1. Install the Jupyter extension

- Open VS Code
- Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
- Search for "Jupyter" by Microsoft
- Click Install

### 2. Open the notebook

- Open the `.ipynb` file in VS Code
- You'll see a notebook interface with cells

### 3. Select the kernel

- Click "Select Kernel" in the top-right corner
- Choose "Python Environments..."
- Select your virtual environment (should show the `.venv` path)
  - If using venv: Look for `.venv/bin/python` or `.venv\Scripts\python.exe`
  - If using uv: Same as above

### 4. Run cells

- Click the play button (▶) next to a cell to run it
- Or use `Shift+Enter` to run a cell and move to the next one
- Use `Ctrl+Enter` (Cmd+Enter on Mac) to run a cell without moving

### 5. Save

- VS Code auto-saves, but you can also use `Ctrl+S` (Cmd+S on Mac)

**Advantages:**
- No separate browser window needed
- Integrated with your development environment
- Better Git integration for viewing changes
- IntelliSense and autocomplete support

---

## Option C: Google Colab

Google Colab runs notebooks in the cloud, requiring no local setup. However, you'll need to manually upload and download files.

### 1. Upload the notebook

**Method 1: Direct upload**
- Go to [Google Colab](https://colab.research.google.com/)
- Click "Upload" in the file dialog
- Select your `.ipynb` file

**Method 2: From Google Drive**
- Upload the `.ipynb` file to Google Drive
- Right-click the file → Open with → Google Colaboratory

### 2. Check dependencies

Add this cell at the beginning of your notebook to verify packages:

```python
# Check installed versions
import sys
print(f"Python version: {sys.version}")

import numpy as np
import matplotlib

print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")
```

**Note:** Colab comes with numpy and matplotlib pre-installed, but versions may differ from your local environment.

### 3. Install specific versions (if needed)

If you need specific package versions matching your `pyproject.toml`, add:

```python
!pip install numpy>=2.4.0 matplotlib>=3.10.8
```

### 4. Run the notebook

- Click the play button (▶) next to cells, or
- Use `Ctrl+Enter` (Cmd+Enter on Mac) to run cells
- Use `Shift+Enter` to run and move to next cell

### 5. Download your completed work

**Download the notebook:**
- File → Download → Download .ipynb

**Download outputs/plots:**
- Right-click on a file in the file browser (left sidebar) → Download
- Or use code to save to Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')

# Save files to your Drive
plt.savefig('/content/drive/MyDrive/output.png')
```

### Important Notes for Colab

⚠️ **Colab sessions are temporary:**
- Sessions time out after inactivity (~90 minutes)
- All files and variables are lost when the session ends
- Always download your work before closing

⚠️ **Package versions may differ:**
- Colab's pre-installed packages may not match your local versions
- This could lead to different behavior or results
- Document any version-specific issues

⚠️ **No automatic sync:**
- Changes in Colab don't automatically sync back to your local files
- Remember to download the updated `.ipynb` file
- Consider using Google Drive mounting for better file management

---

## Troubleshooting

### "Kernel not found" or "No module named 'numpy'"

**In VS Code:**
- Make sure you selected the correct kernel (your `.venv` environment)
- Try reloading VS Code: Ctrl+Shift+P → "Developer: Reload Window"

**In Jupyter:**
- Ensure your virtual environment is activated before launching jupyter
- Verify packages are installed: `pip list | grep numpy`

### "ModuleNotFoundError" in VS Code

Your kernel might not be using the virtual environment:
```bash
# Re-install ipykernel in your venv
source .venv/bin/activate
pip install ipykernel
python -m ipykernel install --user --name=ps3-supervised-learning
```

Then select "ps3-supervised-learning" as your kernel in VS Code.

### Colab-specific issues

- If packages are missing: Add `!pip install <package>` cells at the top
- If session disconnects: Reconnect and re-run all cells from the top
- For large data files: Use Google Drive mounting instead of repeated uploads

