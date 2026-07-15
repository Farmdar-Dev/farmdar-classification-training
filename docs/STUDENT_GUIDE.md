# Student Guide: Fruit or Animal Classifier

## Your Mission

Build a Python program that looks at a picture and predicts whether it shows a fruit or an animal.

You will:

1. Look at the image dataset.
2. Split the images into training data and testing data.
3. Train a machine learning model.
4. Test how accurate it is.
5. Save the model.
6. Use the saved model to classify a new image.

## VS Code Setup

Open the project folder in Microsoft Visual Studio Code.

Run the setup script once.

macOS or Linux:

```bash
bash scripts/setup_jupyter_env.sh
```

Windows PowerShell:

```powershell
.\scripts\setup_jupyter_env.ps1
```

Then open:

```text
notebooks/fruit_animal_classifier_walkthrough.ipynb
```

Choose this kernel:

```text
Python (Farmdar Classification Training)
```

Run the cells from top to bottom.

## Important Idea

A computer does not understand a picture the way a person does. A picture is made of pixels. Each pixel has numbers for color.

The program turns every image into a list of numbers:

- A tiny 16x16 version of the image
- A summary of the colors in the image
- The average color
- How much the colors vary

The model learns patterns in those numbers.

## Files You Will Edit

Use these starter files:

```text
starter/train_model_student.py
starter/predict_student.py
```

The completed answer is in:

```text
src/train_model.py
src/predict.py
```

Try the starter first. Use the completed files only if you get stuck.

## Step 1: Build Or Inspect The Data

The images are arranged like this:

```text
data/images/animal/
data/images/fruit/
```

The folder name is the label. If an image is inside `animal`, the correct answer is animal.

## Step 2: Train The Model

Run:

```bash
python starter/train_model_student.py
```

If you are using the completed version:

```bash
python src/train_model.py
```

The program should:

- Load all image paths
- Create labels: `animal` or `fruit`
- Split into 80% training and 20% testing
- Train a `RandomForestClassifier`
- Print the test accuracy
- Save the model

## Step 3: Test A New Image

Run:

```bash
python starter/predict_student.py data/demo_inputs/demo_fruit_1.jpg
```

Completed version:

```bash
python src/predict.py data/demo_inputs/demo_fruit_1.jpg
```

## What To Write In Your Explanation

Your document should answer:

1. What problem were you solving?
2. What were the two classes?
3. How many images did you use?
4. What does training mean?
5. Why did you test on images the model did not train on?
6. What model did you choose?
7. What accuracy did you get?
8. What kinds of images might confuse the model?
