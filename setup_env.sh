#!/bin/bash
# Setup script for Brains Agent

if [ -L ".venv" ]; then
    echo "Using existing symbolic link .venv -> $(readlink .venv)"
else
    echo "Creating virtual environment..."
    python3 -m venv venv
    ln -s venv .venv
fi

source .venv/bin/activate

echo "Installing/Updating dependencies..."
pip install -r requirements.txt pytest pytest-asyncio

echo "Setup complete. Use 'source .venv/bin/activate' to start."
