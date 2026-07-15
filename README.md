# Fruit or Animal Image Classifier

This is a one-day Python project for young interns. The goal is to build a program that classifies an input image as either:

- `animal`
- `fruit`

The project includes:

- A generated sample image dataset in `data/images`
- Demo images in `data/demo_inputs`
- A completed trained implementation in `src`
- Student starter files in `starter`
- Teacher and student notes in `docs`
- A Jupyter walkthrough for Microsoft Visual Studio Code

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

Run these commands from this folder:

```bash
python src/run_everything.py
```

Or, if the dataset/model already exist:

```bash
python src/train_model.py
python src/predict.py data/demo_inputs/demo_fruit_1.jpg
python src/predict.py data/demo_inputs/demo_animal_1.jpg
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

The completed implementation trains on 80% of the image dataset and tests on the remaining 20%.

The default build collects:

- 150 fruit images
- 150 animal images
- 4 demo images outside the training folder

The model is intentionally not presented as magic. It is good enough for a one-day lesson, and the remaining mistakes are useful for discussion about data quality, noisy labels, and why real AI systems need stronger datasets and models.
