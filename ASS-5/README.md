# ASS-5: Ensemble Learning

## Assignment
Implement Stacking, AdaBoost, and majority Voting ensembles and compare them with base classifiers.

## Models
- Base models: SVM, Decision Tree, KNN, Gaussian Naive Bayes
- Stacking: base classifiers combined with Logistic Regression as meta-classifier
- AdaBoost: decision stump weak learner, 100 estimators, learning rate 0.5
- Voting: hard voting / majority voting

## Dataset
Kaggle Breast Cancer Wisconsin (Diagnostic) dataset: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
The notebook downloads the public dataset directly. After removing `id` and `Unnamed: 32`, it uses 569 samples and 30 numerical features. Diagnosis mapping: B = 0 (benign), M = 1 (malignant).

## Metrics
Accuracy, Precision, Recall, F1-Score, Log Loss, classification reports, confusion matrices, and comparison graphs.

## Run
Open `AIML_Ensemble_Learning_Assignment.ipynb` in Google Colab and run all cells from top to bottom.

## Screenshots
Add real screenshots of executed notebook outputs to the `SS/` folder.
