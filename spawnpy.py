#!/usr/bin/env python3
import argparse
import sys


def main(args):
    # Check if verbose mode is enabled
    if args.verbose:
        print("Verbose mode enabled.")

    # Placeholder for handling the custom input argument
    if args.custom_input is not None:
        print(f"Custom input provided: {args.custom_input}")
    else:
        print("No args provided.")

    # Your script's main logic here
    # ...


if __name__ == "__main__":
    # Create the parser
    # Replace the description for your project needs
    parser = argparse.ArgumentParser(description="A generic Python script template for Linux shell commands.")

    # Add or remove arguments as needed
    parser.add_argument("-V", "--verbose", help="Increase output verbosity.", action="store_true")

    parser.add_argument("-c", "--custom-input",
                        help="Edit to fit project", type=str)

    # Parse the command line arguments
    args = parser.parse_args()

    # Pass the arguments to the main function
    main(args)

