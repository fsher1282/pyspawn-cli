#!/usr/bin/env python3
import argparse


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="A generic Python script template for Linux shell commands.")

    # Add arguments
    parser.add_argument("name", help="Your name or the input for the script.")
    parser.add_argument("-V", "--verbose", action="store_true", help="Increase output verbosity.")

    # Parse the command line arguments
    args = parser.parse_args()




