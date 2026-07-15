# Teacher Guide

## Audience

This lesson is designed for students around age 13 who already know some Python basics:

- Variables
- Lists
- Loops
- Functions
- Running Python files or notebook cells

## Learning Goals

By the end, students should understand:

- AI models learn from examples.
- Training data and test data must be separate.
- Images must be converted into numbers before a model can use them.
- A model can be saved and reused.
- Accuracy is measured on examples the model did not train on.
- More data helps, but noisy data can still reduce accuracy.

## Classroom Setup

Students should use Microsoft Visual Studio Code with the Python and Jupyter extensions.

Ask each student to open the repository folder in VS Code and run one setup script.

macOS or Linux:

```bash
bash scripts/setup_jupyter_env.sh
```

Windows PowerShell:

```powershell
.\scripts\setup_jupyter_env.ps1
```

Then they should open:

```text
notebooks/fruit_animal_classifier_walkthrough.ipynb
```

and select:

```text
Python (Farmdar Classification Training)
```

## Suggested One-Day Schedule

| Time | Activity |
|---|---|
| 30 min | Introduce classification, labels, training, testing |
| 30 min | Run setup and inspect the dataset folders |
| 60 min | Complete `starter/train_model_student.py` |
| 30 min | Run training and read the accuracy report |
| 45 min | Complete `starter/predict_student.py` |
| 30 min | Test new images and discuss wrong predictions |
| 45 min | Write the explanation document |
| 30 min | Present results |

## Model Choice

For a professional system, a convolutional neural network or transfer learning model such as MobileNet would usually be a better choice.

For this one-day student exercise, the completed implementation uses:

```python
RandomForestClassifier
```

Reason:

- It installs easily through scikit-learn.
- It trains quickly on a laptop.
- It avoids GPU setup.
- It is easier to explain than a neural network.
- It still demonstrates the full AI workflow.

## Dataset

The default classroom dataset contains:

- 150 fruit images
- 150 animal images
- 4 demo images outside the training folder

The image downloader uses keyword image requests from LoremFlickr. This is convenient for a classroom bootstrap, but it is not a production-grade data source. Some images may have clutter, watermarks, or surprising content. That is useful for teaching data quality.

## Discussion Questions

- Why do we keep test data separate?
- Why might a picture of fruit in a market be harder than a single fruit on a table?
- What happens if some labels are wrong?
- Is the measured accuracy good enough for a real company product?
- What would we change for a production classifier?
