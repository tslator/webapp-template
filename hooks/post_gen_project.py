#!/usr/bin/env python
"""Post-generation hook to set up the generated project."""

import sys

def main():
    """Main entry point."""
    print("Setup hook completed successfully!")
    print("Please run: make install")
    return 0

if __name__ == '__main__':
    sys.exit(main())
