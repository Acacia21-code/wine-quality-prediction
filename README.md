# 🍷 Wine Quality Prediction using Machine Learning

## Description

This project uses Machine Learning to predict the quality of red wine based on its physicochemical properties. The model is trained using historical wine quality data and can predict the quality score of new wine samples.

The project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, model persistence, and making predictions using a saved model.

---

# Table of Contents

* Project Overview
* Objectives
* Dataset
* Technologies Used
* Machine Learning Workflow
* Project Structure
* Installation
* How to Run
* Model Performance
* Features
* What I Learned
* Future Improvements
* Requirements
* Author

---

# Project Overview

Wine quality can be influenced by several chemical properties such as acidity, sugar content, alcohol percentage, pH, and sulphates. Instead of manually estimating wine quality, this project uses a supervised machine learning model to learn patterns from historical data and predict the quality of unseen wine samples.

This project was developed to strengthen my understanding of the end-to-end machine learning process using Python and Scikit-learn.

---

# Objectives

The objectives of this project are to:

* Load and explore the wine quality dataset.
* Prepare the data for machine learning.
* Train a machine learning model.
* Evaluate the model's performance.
* Save the trained model using Joblib.
* Load the saved model for future predictions.
* Predict the quality of new wine samples.

---

# Dataset

The dataset contains physicochemical properties of red wine along with a quality score assigned by wine experts.

## Features

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

### Target Variable

* Quality

The target variable is the wine quality score predicted by the machine learning model.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Matplotlib 
* Seaborn 
* PyCharm
* Git
* GitHub

---

# Machine Learning Workflow

The project follows a standard machine learning workflow:

1. Import required libraries.
2. Load the dataset.
3. Explore and understand the data.
4. Clean and prepare the dataset.
5. Separate features and target variable.
6. Split the data into training and testing sets.
7. Train the machine learning model.
8. Evaluate model performance.
9. Save the trained model.
10. Load the saved model.
11. Predict the quality of new wine samples.

---

# Machine Learning Type

This project uses **Supervised Learning** because the dataset contains both input features and the correct quality scores used during training.

Depending on the model selected during training, this project predicts wine quality using a regression algorithm. Different regression algorithms can be compared to determine which one performs best before selecting the final model.

---

# Project Structure

```text
Wine-Quality-Prediction/
│
├── data/
│   └── winequality-red.csv
│
├── models/
│   └── wine_quality_model.joblib
│
├── train.py
├── predict.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Acacia21-code/Wine-Quality-Prediction.git
```

Navigate into the project folder:

```bash
cd Wine-Quality-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# How to Run

## Train the model

```bash
python train.py
```

The training script will:

* Load the dataset
* Train the machine learning model
* Evaluate the model
* Save the trained model

---

## Predict Wine Quality

Run:

```bash
python predict.py
```

Example output:

```text
Model loaded from wine_quality_model.joblib

Sample 1 predicted quality: 5.84

Sample 2 predicted quality: 6.41
```

---

# Features

* Data preprocessing
* Machine learning model training
* Model evaluation
* Save trained model using Joblib
* Load saved model
* Predict quality of new wine samples
* Clean and reusable Python code

---

# Model Evaluation

The trained model should be evaluated using appropriate regression metrics such as:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)
* R² Score

These metrics help determine how accurately the model predicts wine quality.

---

# What I Learned

Through this project, I learned:

* The complete machine learning workflow.
* The difference between supervised and unsupervised learning.
* How regression models predict numerical values.
* How to prepare datasets for machine learning.
* How to split data into training and testing sets.
* How to train and evaluate machine learning models.
* How to compare different algorithms to determine which performs best.
* How to save and load trained models using Joblib.
* How to make predictions using previously unseen data.
* The importance of reproducible and well-documented projects.

---

# Challenges

Some challenges encountered during the project included:

* Understanding the complete machine learning workflow.
* Learning when to use regression algorithms.
* Understanding model evaluation metrics.
* Organizing project files for GitHub.
* Learning how to save and reuse trained models.

These challenges provided valuable experience in practical machine learning development.

---

# Future Improvements

Possible improvements include:

* Compare multiple regression algorithms.
* Perform hyperparameter tuning.
* Build a Streamlit web application for predictions.
* Allow users to upload CSV files for batch predictions.
* Deploy the model online.
* Improve feature engineering.
* Add automated model evaluation reports.

---

# Requirements

Required Python packages:

```text
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# GitHub Topics

Recommended repository topics:

* python
* machine-learning
* scikit-learn
* pandas
* data-science
* regression
* predictive-modeling
* wine-quality
* joblib
* beginner-project

---

# Author

**Mbali Simelane**

Aspiring Data Scientist and Machine Learning Developer

This project was created as part of my machine learning learning journey and demonstrates the complete process of building, training, evaluating, and deploying a machine learning model using Python and Scikit-learn.
