"""Student starter file for classifying one new image."""

import argparse
from pathlib import Path
import sys

import joblib
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.common import extract_features


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--model-path", default="models/student_model.joblib")
    args = parser.parse_args()

    package = joblib.load(args.model_path)
    model = package["model"]
    class_names = package["class_names"]

    # TODO 1: extract features from args.image.
    # TODO 2: ask the model for probabilities.
    # TODO 3: print the best class and confidence.


if __name__ == "__main__":
    main()
