#!/usr/bin/env python3
import argparse


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Generates a generic Python script for Linux shell commands.")

    # Get Script name
    parser.add_argument("-n", "--script-name", help="Name of the generated Python script file.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Handle case where user adds .py extension
    if args.script_name[-3:] == '.py':
        script_name = args.script_name
    else:
        script_name = args.script_name + '.py'

    try:
        with open('template.py', 'r') as template_file:  # Open template file
            contents = template_file.readlines()

        with open(script_name, 'x') as new_file:  # Create new file and write contents
            for content in contents:
                new_file.write(content)

        print(f"Script {script_name} was created successfully.")

    except FileExistsError:
        print(f"Error: The file '{script_name}' already exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


