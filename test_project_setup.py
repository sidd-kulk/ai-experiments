"""Script to test the project structure and imports."""

import importlib
import os
import sys
from pathlib import Path


def check_file_exists(filepath):
    """Check if a file exists and print the result."""
    path = Path(filepath)
    exists = path.exists()
    status = "✅" if exists else "❌"
    print(f"{status} {filepath}")
    return exists


def check_import(module_name):
    """Check if a module can be imported and print the result."""
    try:
        module = importlib.import_module(module_name)
        print(f"✅ Import successful: {module_name}")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {module_name} - {e}")
        return False


def main():
    """Run all checks."""
    print("Checking project structure...")
    
    # Check key files
    files_to_check = [
        "pyproject.toml",
        "setup.py",
        "requirements.txt",
        "Makefile",
        "README.md",
        ".gitignore",
        "src/ai_experiments/__init__.py",
        "src/ai_experiments/utils.py",
        "src/ai_experiments/models/__init__.py",
        "src/ai_experiments/models/base.py",
        "tests/__init__.py",
        "tests/test_utils.py"
    ]
    
    all_files_exist = all(check_file_exists(f) for f in files_to_check)
    
    # Check imports
    print("\nChecking imports...")
    modules_to_check = [
        "ai_experiments",
        "ai_experiments.utils",
        "ai_experiments.models",
        "ai_experiments.models.base"
    ]
    
    # First ensure src is in path if running script directly
    if os.path.exists("src") and "src" not in sys.path:
        sys.path.insert(0, "src")
        
    all_imports_work = all(check_import(m) for m in modules_to_check)
    
    # Try using some functionality
    print("\nTesting functionality...")
    try:
        from ai_experiments.utils import setup_logger
        logger = setup_logger()
        logger.info("Logger test successful")
        print("✅ Logger functionality works")
        functionality_works = True
    except Exception as e:
        print(f"❌ Logger functionality failed: {e}")
        functionality_works = False
        
    # Summary
    print("\nSummary:")
    print(f"Files check: {'PASS' if all_files_exist else 'FAIL'}")
    print(f"Imports check: {'PASS' if all_imports_work else 'FAIL'}")
    print(f"Functionality check: {'PASS' if functionality_works else 'FAIL'}")
    
    overall = all([all_files_exist, all_imports_work, functionality_works])
    print(f"\nOverall project structure check: {'PASS' if overall else 'FAIL'}")
    
    if overall:
        print("\nYour project structure looks good! Next steps:")
        print("1. Run 'make install' to install the package")
        print("2. Run 'make test' to run the test suite")
        print("3. Start implementing your AI experiments")
    

if __name__ == "__main__":
    main()
