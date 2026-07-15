import argparse
from pathlib import Path

import joblib
import numpy as np

from common import extract_features


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="Path to a new image to classify")
    parser.add_argument("--model-path", default="models/fruit_animal_classifier.joblib")
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        raise FileNotFoundError(image_path)

    package = joblib.load(args.model_path)
    model = package["model"]
    class_names = package["class_names"]

    features = extract_features(image_path).reshape(1, -1)
    probabilities = model.predict_proba(features)[0]
    best_index = int(np.argmax(probabilities))

    print(f"Image: {image_path}")
    print(f"Prediction: {class_names[best_index]}")
    print(f"Confidence: {probabilities[best_index]:.1%}")
    print("")
    print("All scores:")
    for class_name, probability in zip(class_names, probabilities):
        print(f"  {class_name}: {probability:.1%}")


if __name__ == "__main__":
    main()
