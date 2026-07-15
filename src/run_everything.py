import subprocess
import sys
from pathlib import Path


def run(command):
    print("\n$", " ".join(command))
    subprocess.run(command, check=True)


def main():
    project_root = Path(__file__).resolve().parents[1]
    python = sys.executable

    run(
        [
            python,
            "src/download_keyword_dataset.py",
            "--output-dir",
            "data/images",
            "--demo-dir",
            "data/demo_inputs",
            "--target-per-class",
            "150",
            "--clean",
        ]
    )
    run([python, "src/train_model.py"])
    run([python, "src/predict.py", "data/demo_inputs/demo_fruit_1.jpg"])
    run([python, "src/predict.py", "data/demo_inputs/demo_animal_1.jpg"])
    print(f"\nFinished in {project_root}")


if __name__ == "__main__":
    main()
