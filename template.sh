#!/bin/bash

# 1. Project name
PROJECT_NAME="NotebookFusion"

# 2. Create folders
mkdir -p .github/workflows \
         src/$PROJECT_NAME \
         tests/unit \
         tests/integration

# 3. Create files
touch .github/workflows/.gitkeep \
      src/$PROJECT_NAME/__init__.py \
      tests/__init__.py \
      tests/unit/__init__.py \
      tests/integration/__init__.py \
      requirements.txt \
      setup.py \
      pyproject.toml \
      setup.cfg \
      tox.ini