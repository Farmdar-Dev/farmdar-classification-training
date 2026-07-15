# Fruit or Animal Image Classifier

This is a one-day Python project for young interns. The goal is to build a program that classifies an input image as either:

- `animal`
- `fruit`

The project includes:

- 150 fruit images and 150 animal images in `data/images`
- 4 separate demo images in `data/demo_inputs`
- A completed trained implementation in `src`
- Student starter files in `starter`
- Teacher and student notes in `docs`
- A saved trained model at `models/fruit_animal_classifier.joblib`

## Setup For VS Code And Jupyter

Open this repository folder in Microsoft Visual Studio Code.

Install the recommended extensions when VS Code prompts you:

- Python
- Jupyter

Then run the setup script.

macOS or Linux:

```bash
bash scripts/setup_jupyter_env.sh
```

Windows PowerShell:

```powershell
.\scripts\setup_jupyter_env.ps1
```

After setup, open:

```text
notebooks/fruit_animal_classifier_walkthrough.ipynb
```

Select this Jupyter kernel:

```text
Python (Farmdar Classification Training)
```

Then run the notebook cells from top to bottom.

## Script Quick Start

You can also run these commands from this folder:

```bash
python src/train_model.py
python src/predict.py data/demo_inputs/demo_fruit_1.jpg
python src/predict.py data/demo_inputs/demo_animal_1.jpg
```

To rebuild everything from scratch:

```bash
python src/run_everything.py
```

## Project Structure

```text
data/images/animal/       training and testing images for animal
data/images/fruit/        training and testing images for fruit
data/demo_inputs/         images outside the training folder
models/                   saved trained model
reports/                  accuracy report and train/test split
src/                      completed implementation
starter/                  student TODO templates
docs/                     classroom notes
notebooks/                VS Code Jupyter walkthrough
scripts/                  environment setup scripts
```

## Current Result

The completed implementation trains on 80% of the 300-image dataset and tests on the remaining 20%.

Current saved run:

- Training images: 240
- Testing images: 60
- Accuracy: 76.7%

This is intentionally not presented as magic. The model is good enough for a one-day lesson, and the remaining mistakes are useful for discussion about data quality, noisy labels, and why real AI systems need stronger datasets and models.
