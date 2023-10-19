#!/bin/bash

# Run pyinstaller on main.py in the current directory
yes | pyinstaller main.py

# Create output and data directories inside the main directory within dist
OUTPUT_DIR="dist/main/output"
DATA_DIR="dist/main/data"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$DATA_DIR"

# Create lesson.docx in the output directory
touch "$OUTPUT_DIR/lesson.docx"

# Create data.json in the data directory with the specified data
DATA_JSON="$DATA_DIR/data.json"
echo '{
  "sentences": {
    "section1": [],
    "section2": [],
    "section3": []
  },
  "words": {
    "section1": [],
    "section2": [],
    "section3": []
  }
}' > "$DATA_JSON"

# Zip the main directory and place it inside dist
cd "dist"

