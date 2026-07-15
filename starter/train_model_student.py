"""Student starter file.

Goal:
1. Load images from data/images/animal and data/images/fruit.
2. Split them into 80% training and 20% testing.
3. Train a model.
4. Print the test accuracy.
5. Save the trained model.
"""

from pathlib import Path
import sys

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.common import image_files, make_feature_matrix


DATA_DIR = Path("data/images")
MODEL_PATH = Path("models/student_model.joblib")


def main():
    paths = []
    labels = []
    class_names = ["animal", "fruit"]

    # TODO 1: loop through each class folder and collect image paths.
    # Hint: use image_files(DATA_DIR / class_name)

    # TODO 2: split paths and labels into train and test sets.
    # Hint: train_test_split(..., test_size=0.2, stratify=labels)

    # TODO 3: turn images into features using make_feature_matrix.

    # TODO 4: create and train this model.
    model = RandomForestClassifier(n_estimators=500, random_state=0)

    # TODO 5: predict the test set and print the accuracy.

    # TODO 6: save {"model": model, "class_names": class_names}.
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "class_names": class_names}, MODEL_PATH)


if __name__ == "__main__":
    main()
