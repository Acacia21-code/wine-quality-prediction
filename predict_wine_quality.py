import joblib
import pandas as pd

def load_model(model_path='wine_quality_model.joblib'):
    """
    Load the saved model pipeline from disk.
    """
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")
    return model

def predict_quality(model, input_data):
    """
    Predict wine quality given input features.
    input_data: pandas DataFrame with the same features used in training.
    """
    predictions = model.predict(input_data)
    return predictions

def main():
    # Load the trained model pipeline
    model = load_model()

    # Example new data: replace these values with your own samples
    new_samples = pd.DataFrame({
        'fixed acidity': [7.4, 6.0],
        'volatile acidity': [0.7, 0.3],
        'citric acid': [0.0, 0.4],
        'residual sugar': [1.9, 2.5],
        'chlorides': [0.076, 0.05],
        'free sulfur dioxide': [11, 15],
        'total sulfur dioxide': [34, 40],
        'density': [0.9978, 0.995],
        'pH': [3.51, 3.3],
        'sulphates': [0.56, 0.7],
        'alcohol': [9.4, 10.5]
    })

    # Predict quality scores
    predicted_qualities = predict_quality(model, new_samples)

    # Print predictions
    for i, quality in enumerate(predicted_qualities):
        print(f"Sample {i+1} predicted quality: {quality:.2f}")

if __name__ == "__main__":
    main()

