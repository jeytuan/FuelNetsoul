#!/bin/bash

# Activate the virtual environment
source ../venv/bin/activate

# Run the Fuel network scan
python ../src/fuel_scanner.py

# Run the Sway analyzer
python ../src/sway_analyzer.py

# Run exploit development scripts
python ../src/exploit_dev.py
