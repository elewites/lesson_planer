#!/bin/bash

# Define the path to your virtual environment's activate script
VENV_PATH="C:/Users/elewi/repos/LessonPlanner/myenv/Scripts/activate"

# Activate the virtual environment
source "$VENV_PATH"

# Define the path to your main.py script
MAIN_PY_PATH="C:/Users/elewi/repos/LessonPlanner/src/main.py"

# Install required packages from requirements.txt into the virtual environment
pip install -r "C:/Users/elewi/repos/LessonPlanner/requirements.txt"

# Run the main.py script
python "$MAIN_PY_PATH"

# Deactivate the virtual environment (optional)
deactivate
