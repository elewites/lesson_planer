#!/bin/bash

# Get the directory of the script (the directory containing this script)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define the relative path to your virtual environment's activate script
VENV_PATH="$SCRIPT_DIR/myenv/Scripts/activate"

# Activate the virtual environment
source "$VENV_PATH"

# Define the relative path to your main.py script
MAIN_PY_PATH="$SCRIPT_DIR/main.py"

# Install required packages from requirements.txt into the virtual environment
pip install -r "$SCRIPT_DIR/requirements.txt"

# Run the main.py script
python "$MAIN_PY_PATH"

# Deactivate the virtual environment (optional)
deactivate

