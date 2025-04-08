import subprocess

# List of required packages
packages = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "xgboost",
    "lightgbm",
    "tensorflow",
    "keras",
    "opencv-python",
    "nltk",
    "spacy",
    "streamlit",
    "plotly"
]

# Install each package using pip
for package in packages:
    print(f"Installing {package}...")
    subprocess.check_call(["pip", "install", package])
