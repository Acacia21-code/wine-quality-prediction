# Wine Quality Prediction - Automated ML Pipeline

## Project Overview

This project demonstrates an end-to-end automated machine learning pipeline to predict the quality of red wine based on physicochemical tests. The pipeline includes data loading, preprocessing, model training, evaluation, and saving the trained model for future use.

The model is built using a Random Forest Regressor and the popular [Wine Quality Dataset (Red Wine)](https://archive.ics.uci.edu/ml/datasets/wine+quality) from the UCI Machine Learning Repository.

---

## Features

- Automated data loading from CSV file
- Data preprocessing with feature scaling
- Model training using Random Forest regression
- Model evaluation with Mean Squared Error (MSE) and R² score
- Saving the trained model pipeline for reuse
- Separate script for loading the saved model and making predictions on new data

---

## Project Structure

---

## Requirements

- Python 3.7 or higher
- Packages:
  - pandas
  - scikit-learn
  - joblib

Install dependencies using pip:

```bash
pip install pandas scikit-learn joblib