# pyspawn-cli
`pyspawn-cli` is a command-line tool Creates a generic template for Python Shell commands

## Installation

Before installing `pyspawn-cli`, ensure you have Python installed on your system.


To install `spawnPy`, clone the repository to your local machine and navigate to the project directory:

``` bash
git clone https://github.com/fsher1282/pyspawn-cli/tree/main
cd pyspawn-cli
```

Make the main script executable:
``` bash
chmod +x spawnPy.py
```

Optionally, you can add the spawnPy directory to your PATH to run spawnPy from any location on your system. Add the following line to your .bashrc, .zshrc, or equivalent shell configuration file:
``` bash
export PATH="$PATH:/path/to/pyspawn-cli"
```
Replace /path/to/spawnPy with the actual path to the spawnPy directory.

## Usage
To generate a new Python script, use the following command:
``` bash
spawnPy -n "new_script_name"
```

Replace "new_script_name" with the desired name of your Python script. If you do not include the .py extension, spawnPy will automatically append it.

# Options
. -n, --script-name: Specifies the name of the new Python script to be generated.

## Example
To create a new Python script named hello_world.py, run:
``` bash
spawnPy -n "hello_world"
```
This will generate a new file named hello_world.py in the current directory, pre-filled with the template code.

## Customizing the Template
The default script template is located in template.py within the spawnPy directory. You can modify this template to include any default code or import statements you frequently use.

