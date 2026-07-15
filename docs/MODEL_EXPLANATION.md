# How The Completed Program Works

## 1. Data Collection

Images are stored in class folders:

```text
data/images/animal/
data/images/fruit/
```

The folder name is used as the answer label.

## 2. Feature Extraction

The program cannot train directly on a normal image file. It first converts each image into numbers.

For each image, `src/common.py` creates:

- A small 16x16 pixel version of the image
- A red color histogram
- A green color histogram
- A blue color histogram
- Average color values
- Color spread values

These numbers become one row of training data.

## 3. Train/Test Split

`src/train_model.py` uses:

```python
train_test_split(..., test_size=0.2, stratify=labels)
```

That means:

- 80% of images train the model
- 20% of images test the model
- Both classes stay balanced in the split

With 300 images:

- 240 train images
- 60 test images

## 4. Model

The model is:

```python
RandomForestClassifier
```

A random forest is a group of decision trees. Each tree makes a prediction, then the forest combines the votes.

## 5. Evaluation

After training, the model predicts the labels for the test images.

The report includes:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Reports are saved in:

```text
reports/test_results.txt
reports/confusion_matrix.csv
reports/train_test_split.json
```

## 6. Saving The Model

The trained model is saved with `joblib`:

```text
models/fruit_animal_classifier.joblib
```

This means prediction can run later without retraining.
