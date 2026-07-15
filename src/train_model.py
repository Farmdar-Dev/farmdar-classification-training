import argparse
import csv
import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

from common import IMAGE_SIZE, image_files, make_feature_matrix


def load_dataset(data_dir):
    data_dir = Path(data_dir)
    class_dirs = sorted(path for path in data_dir.iterdir() if path.is_dir())
    class_names = [path.name for path in class_dirs]

    paths = []
    labels = []
    for label, class_dir in enumerate(class_dirs):
        for path in image_files(class_dir):
            paths.append(path)
            labels.append(label)

    if len(class_names) < 2:
        raise ValueError("Expected at least two class folders, such as animal and fruit.")
    if len(paths) < len(class_names) * 5:
        raise ValueError("Need more images. Run the downloader or add pictures first.")

    return paths, np.array(labels), class_names


def write_confusion_matrix(path, matrix, class_names):
    with Path(path).open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["actual \\ predicted", *class_names])
        for class_name, row in zip(class_names, matrix):
            writer.writerow([class_name, *row.tolist()])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data/images")
    parser.add_argument("--model-path", default="models/fruit_animal_classifier.joblib")
    parser.add_argument("--report-dir", default="reports")
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--random-state", type=int, default=7)
    parser.add_argument("--model-random-state", type=int, default=0)
    args = parser.parse_args()

    report_dir = Path(args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    Path(args.model_path).parent.mkdir(parents=True, exist_ok=True)

    paths, labels, class_names = load_dataset(args.data_dir)
    print(f"Loaded {len(paths)} images from {len(class_names)} classes: {class_names}")

    train_paths, test_paths, y_train, y_test = train_test_split(
        paths,
        labels,
        test_size=args.test_size,
        random_state=args.random_state,
        stratify=labels,
    )

    print(f"Training images: {len(train_paths)}")
    print(f"Testing images: {len(test_paths)}")
    print("Extracting training features...")
    x_train = make_feature_matrix(train_paths)
    print("Extracting testing features...")
    x_test = make_feature_matrix(test_paths)

    model = RandomForestClassifier(
        n_estimators=500,
        random_state=args.model_random_state,
        class_weight="balanced",
    )

    print("Training model...")
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(
        y_test, predictions, target_names=class_names, zero_division=0
    )
    matrix = confusion_matrix(y_test, predictions)

    package = {
        "model": model,
        "class_names": class_names,
        "image_size": IMAGE_SIZE,
        "feature_version": 1,
    }
    joblib.dump(package, args.model_path)

    split_info = {
        "class_names": class_names,
        "train_count": len(train_paths),
        "test_count": len(test_paths),
        "test_size": args.test_size,
        "random_state": args.random_state,
        "model_random_state": args.model_random_state,
        "train_files": [str(path) for path in train_paths],
        "test_files": [str(path) for path in test_paths],
    }
    (report_dir / "train_test_split.json").write_text(
        json.dumps(split_info, indent=2), encoding="utf-8"
    )
    (report_dir / "test_results.txt").write_text(
        f"Accuracy: {accuracy:.3f}\n\n{report}", encoding="utf-8"
    )
    write_confusion_matrix(report_dir / "confusion_matrix.csv", matrix, class_names)

    print(f"Accuracy: {accuracy:.3f}")
    print(report)
    print(f"Saved model to {args.model_path}")
    print(f"Saved reports to {report_dir}")


if __name__ == "__main__":
    main()
