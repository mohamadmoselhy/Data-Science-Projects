import shutil
import os

# Path to the virtual environment
venv_path = "venv"

# Remove the venv directory if it exists
if os.path.exists(venv_path):
    shutil.rmtree(venv_path)
    print("✅ Virtual environment removed.")
else:
    print("⚠️ No virtual environment found at:", venv_path)