#!/usr/bin/env python3
"""
Sanity check script for CS6140 PS4 environment.
Verifies that the user is running in a virtual environment (venv or uv)
with required packages: numpy, matplotlib, scikit-learn, and ipykernel.
"""

import sys
import os
from pathlib import Path
import re


def check_virtual_environment():
    """Check if running in a virtual environment (venv or uv)."""
    # Check for venv
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

    # Check for uv environment by looking for UV_PYTHON or VIRTUAL_ENV
    in_uv = os.environ.get('UV_PYTHON') is not None or \
            os.environ.get('VIRTUAL_ENV') is not None or \
            Path(sys.prefix).name == '.venv'

    return in_venv or in_uv, sys.prefix


def load_required_packages():
    """Load required packages from pyproject.toml."""
    pyproject_path = Path(__file__).parent / "pyproject.toml"

    if not pyproject_path.exists():
        print(f"   ⚠ WARNING: pyproject.toml not found at {pyproject_path}")
        return ['numpy', 'matplotlib', 'scikit-learn', 'ipykernel']  # Fallback to defaults

    try:
        with open(pyproject_path, 'r') as f:
            content = f.read()

        # Find the dependencies section
        in_dependencies = False
        packages = []

        for line in content.split('\n'):
            if 'dependencies = [' in line:
                in_dependencies = True
                continue
            if in_dependencies:
                if ']' in line:
                    break
                # Extract package name from dependency string like "numpy>=2.0"
                match = re.match(r'\s*"([a-zA-Z0-9_-]+)', line)
                if match:
                    packages.append(match.group(1))

        return packages if packages else ['numpy', 'matplotlib', 'scikit-learn', 'ipykernel']

    except Exception as e:
        print(f"   ⚠ WARNING: Could not parse pyproject.toml: {e}")
        return ['numpy', 'matplotlib', 'scikit-learn', 'ipykernel']  # Fallback to defaults


def check_package(package_name):
    """Check if a package is installed and return its version."""
    try:
        module = __import__(package_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, None


def main():
    """Run all sanity checks and report results."""
    print("=" * 60)
    print("CS6140 Problem Set 4 - Environment Sanity Check")
    print("=" * 60)
    print()

    all_checks_passed = True

    # Check 1: Virtual environment
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

    # Check 2: Required packages
    required_packages = load_required_packages()
    print("2. Checking required packages...")

    for package in required_packages:
        installed, version = check_package(package)
        if installed:
            print(f"   ✓ {package:12s} (version {version})")
        else:
            print(f"   ✗ {package:12s} NOT INSTALLED")
            all_checks_passed = False
    print()

    # Final result
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
        print("  1. Create/activate a virtual environment:")
        print("     - venv: python -m venv .venv && source .venv/bin/activate")
        print("     - uv:   uv venv && source .venv/bin/activate")
        print("  2. Install required packages:")
        print("     - pip:  pip install numpy matplotlib scikit-learn ipykernel jupyter")
        print("     - uv:   uv pip install numpy matplotlib scikit-learn ipykernel jupyter")
        return 1


if __name__ == "__main__":
    sys.exit(main())
