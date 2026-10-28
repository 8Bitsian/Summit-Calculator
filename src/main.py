# Standard Library Imports
import sys

from app import run

if __name__ == "__main__":
    """'main.py' is the entry point for the program."""
    print(f"Running {__name__}\n")
    sys.exit(run())
    print("Closing program...")