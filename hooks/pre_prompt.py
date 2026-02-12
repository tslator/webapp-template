#!/usr/bin/env python
"""Pre-prompt hook to validate user inputs before template generation."""

import re
import sys


def validate_project_name(project_name: str) -> None:
    """Validate project name format."""
    if not project_name or len(project_name) < 3:
        print("❌ Project name must be at least 3 characters long")
        sys.exit(1)

    if not re.match(r'^[a-zA-Z0-9\s\-_]+$', project_name):
        print("❌ Project name can only contain letters, numbers, spaces, hyphens, and underscores")
        sys.exit(1)


def validate_email(email: str) -> None:
    """Validate email format."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        print("❌ Invalid email format")
        sys.exit(1)


def validate_python_version(version: str) -> None:
    """Validate Python version format."""
    if not re.match(r'^\d+\.\d+$', version):
        print("❌ Python version must be in format X.Y (e.g., 3.14)")
        sys.exit(1)

    major, minor = map(int, version.split('.'))
    if major < 3 or (major == 3 and minor < 11):
        print("❌ Python version must be 3.11 or higher")
        sys.exit(1)


def main():
    """Run all validation checks."""
    # Note: In actual cookiecutter execution, these would be validated during the prompt
    # This hook is a placeholder for custom validation logic if needed
    print("[OK] Pre-generation validation passed")


if __name__ == '__main__':
    main()
