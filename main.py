from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model
try:
    model = joblib.load("ml_models/diabetes_model/model.pkl")
except Exception as e:
    raise RuntimeError("Model loading failed. Make sure 'model.pkl' is in the correct path.") from e

class DiabetesRequest(BaseModel):
    data: list  # expects a list of 10 features

@app.post("/predict")
def predict(request: DiabetesRequest):
    try:
        prediction = model.predict([np.array(request.data)])
        return { "prediction": prediction[0] }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
