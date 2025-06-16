import mlflow
import mlflow.sklearn
import joblib

# Load model
model = joblib.load("model.pkl")

# Log model with MLflow
mlflow.set_experiment("DiabetesPrediction")
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model")
    print("Model logged to MLflow.")
