#!/usr/bin/env python3
"""
Sanity check script for CS6140 PS6 Neural Networks environment.
Verifies that the user is running in a virtual environment (venv or uv)
with required packages: numpy, matplotlib, scikit-learn, torch, and tensorboard.
"""

import sys
import os
from pathlib import Path
import re


def check_virtual_environment():
    """Check if running in a virtual environment (venv or uv)."""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    in_uv = os.environ.get('UV_PYTHON') is not None or \
            os.environ.get('VIRTUAL_ENV') is not None or \
            Path(sys.prefix).name == '.venv'
    return in_venv or in_uv, sys.prefix


def load_required_packages():
    """Load required packages from pyproject.toml."""
    pyproject_path = Path(__file__).parent / "pyproject.toml"
    if not pyproject_path.exists():
        print(f"   ⚠ WARNING: pyproject.toml not found at {pyproject_path}")
        return ['numpy', 'matplotlib', 'scikit-learn', 'torch', 'tensorboard']
    try:
        with open(pyproject_path, 'r') as f:
            content = f.read()
        in_dependencies = False
        packages = []
        for line in content.split('\n'):
            if 'dependencies = [' in line:
                in_dependencies = True
                continue
            if in_dependencies:
                if ']' in line:
                    break
                match = re.match(r'\s*"([a-zA-Z0-9_-]+)', line)
                if match:
                    packages.append(match.group(1))
        return packages if packages else ['numpy', 'matplotlib', 'scikit-learn', 'torch', 'tensorboard']
    except Exception as e:
        print(f"   ⚠ WARNING: Could not parse pyproject.toml: {e}")
        return ['numpy', 'matplotlib', 'scikit-learn', 'torch', 'tensorboard']


IMPORT_NAME_MAP = {
    'scikit-learn': 'sklearn',
}


def check_package(package_name):
    """Check if a package is installed and return its version."""
    import_name = IMPORT_NAME_MAP.get(package_name, package_name)
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, None


def main():
    """Run all sanity checks and report results."""
    print("=" * 60)
    print("CS6140 - PS6 Neural Networks Environment Check")
    print("=" * 60)
    print()
    all_checks_passed = True
    print("1. Checking virtual environment...")
    in_venv, prefix = check_virtual_environment()
    if in_venv:
        print(f"   ✓ Running in virtual environment")
        print(f"   Location: {prefix}")
    else:
        print(f"   ⚠ WARNING: Not running in a virtual environment")
        print(f"   Current Python prefix: {prefix}")
        print(f"   Recommended: Use a venv or uv environment for isolation")
    print()
    required_packages = load_required_packages()
    print("2. Checking required packages...")
    for package in required_packages:
        installed, version = check_package(package)
        if installed:
            print(f"   ✓ {package:14s} (version {version})")
        else:
            print(f"   ✗ {package:14s} NOT INSTALLED")
            all_checks_passed = False
    print()
    print("3. Checking GPU availability...")
    try:
        import torch
        if torch.cuda.is_available():
            print(f"   ✓ CUDA available: {torch.cuda.get_device_name(0)}")
        else:
            print(f"   ⚠ CUDA not available (CPU only)")
            print(f"   This assignment works fine on CPU")
    except ImportError:
        print(f"   ✗ Cannot check — torch not installed")
    print()
    print("=" * 60)
    if all_checks_passed:
        print("✓ All checks passed! Your environment is ready.")
        print("=" * 60)
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        print("=" * 60)
        print()
        print("To fix:")
        print("  Option A (uv — recommended):")
        print("     uv venv && source .venv/bin/activate && uv sync")
        print("  Option B (pip):")
        print("     python -m venv .venv && source .venv/bin/activate")
        print("     pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
