"""
Sanity check for PS5 environment.
Run this before starting the assignment to verify all dependencies are installed.

Usage:
    python sanity_check.py
"""

import sys

def check_version(module_name, import_name=None, min_version=None):
    """Check if a module is importable and optionally check its version."""
    import_name = import_name or module_name
    try:
        mod = __import__(import_name)
        version = getattr(mod, "__version__", "unknown")
        status = "OK"
        if min_version and version != "unknown":
            from packaging.version import Version
            if Version(version) < Version(min_version):
                status = f"WARN (have {version}, want >={min_version})"
        print(f"  {module_name:25s} {version:15s} {status}")
        return True
    except ImportError:
        print(f"  {module_name:25s} {'NOT FOUND':15s} FAIL")
        return False

def check_data():
    """Check if data files are present."""
    from pathlib import Path
    files = ["brfss_national.csv", "brfss_maine.csv"]
    all_found = True
    for f in files:
        path = Path(f)
        if path.exists():
            import os
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"  {f:25s} {size_mb:.1f} MB       OK")
        else:
            print(f"  {f:25s} {'MISSING':15s} FAIL")
            all_found = False
    return all_found

if __name__ == "__main__":
    print(f"Python {sys.version}\n")

    print("Checking packages:")
    packages = [
        ("pandas", "pandas", "2.0"),
        ("numpy", "numpy", "1.24"),
        ("matplotlib", "matplotlib", "3.7"),
        ("seaborn", "seaborn", "0.12"),
        ("scikit-learn", "sklearn", "1.4"),
        ("xgboost", "xgboost", "2.0"),
        ("lightgbm", "lightgbm", "4.0"),
        ("optuna", "optuna", "3.5"),
    ]

    all_ok = True
    for name, imp, ver in packages:
        if not check_version(name, imp, ver):
            all_ok = False

    print("\nChecking data files:")
    data_ok = check_data()

    print()
    if all_ok and data_ok:
        print("All checks passed. You're ready to start!")
    else:
        if not all_ok:
            print("Some packages are missing. Run: uv sync  (or: pip install -r requirements.txt)")
        if not data_ok:
            print("Data files missing. Copy brfss_national.csv and brfss_maine.csv from the Week 9 lab.")
        sys.exit(1)
